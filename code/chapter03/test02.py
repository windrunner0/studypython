import re

f = open("./index.html","r",encoding='UTF-8')
content = f.read()
f.close()

#print(content)

#title = re.search("<title>(.*?)</title>",content)
title = re.compile(r'<title>(.*?)</title>')
print(title)
print(title.findall(content))
#if title:
#    print(title)
#    print("标题："+title.group())


alist = re.findall('<a href="https://(.*?)">(.*?)</a>',content)

for ov in alist:
    print(ov[1]+":"+ov[0])
