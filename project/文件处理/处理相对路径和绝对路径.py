from pathlib import Path
import os

#判断是否是绝对路径 is_absolute()方法， 如果是绝对路径的话，返回True
print(Path.cwd().is_absolute())
#True
print(Path('python\project').is_absolute())
#False


print(Path.cwd())
print((Path.cwd() / 'test.py').is_absolute())

#os提供的方法 os.path.abspath(path)
print(os.path.abspath('..')) #获得绝对的路径的字符串形式

#判断是否是绝对路径， 如果是的话就返回True os.path.isabs(path)
print(os.path.isabs('..'))
print(os.path.isabs(os.path.abspath('pathlib_Path_usage.py')))

#os.path.relpath(path, start)， 将返回从开始路径到path的相对路径的字符串形式，
#如果没有开始路径，则将当前的目录文件夹当做是开始路径
print(os.path.relpath('C:\code\python\project', 'C:'))