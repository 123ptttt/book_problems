import os

"""
p = 'C:\code\python\书上的例题\project\Colltaz.py'
print(os.path.getsize(p)) #获得文件中的字节数
print(os.listdir('C:\code\python\书上的例题\project')) #获得字符串列表
"""
textile = 0
for text in os.listdir('/project'):
    textile += os.path.getsize(os.path.join('/project', text))
print(textile)
