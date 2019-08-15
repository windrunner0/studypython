import os,time
import requests
from urllib.parse import urlencode
from urllib.request import urlretrieve

def getPage(offset):
    '''爬取指定url页面信息'''
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def getImages(json):
    '''解析获取图片信息'''
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            for image in image_list:
                yield {
                    'image': image.get('url'),
                    'title': title
                }

def saveImage(item):
    '''储存图片'''
    # 处理每组图片的存储路径
    path = os.path.join("./mypic/",item.get('title'))
    if not os.path.exists(path):
        os.mkdir(path)

    # 拼装原图和目标图片的路径即名称
    local_image_url = item.get('image')
    image_url = "http:"+local_image_url.replace('list','large')
    save_pic = path+"/"+local_image_url.split("/").pop()+".jpg"

    # 使用urllib中urlretrieve直接存储图片
    urlretrieve(image_url,save_pic)

def main(offset):
    ''' 主程序函数，负责调度执行爬虫处理 '''
    json = getPage(offset)
    for item in getImages(json):
        print(item)
        saveImage(item)

# 判断当前执行是否为主程序运行，并遍历调用主函数爬取数据
if __name__ == '__main__':
    #main(0)
    for i in range(5):
        main(offset=i*20)
        time.sleep(1)