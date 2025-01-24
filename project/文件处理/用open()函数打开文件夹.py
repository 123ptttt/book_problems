from pathlib import Path

helloFile = open('/project/文件处理/spam.txt', 'r+')
#以字符串的形式读出
#content = helloFile.read()
#print(content)
#以字符串列表的形式读出每一行
hellocontent = helloFile.readlines()
print(hellocontent)