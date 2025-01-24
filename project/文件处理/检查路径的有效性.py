"""
Path.exists()判断路径是否存在 == os.path.exists()
Path.is_file()判断路径是否存在， 并且是否是一个文件 == os.path.isfile()
Path.is_dir()判断路径是否存在， 并且是否是一个文件夹 == os.path.isdir()
"""
from pathlib import Path
import os
winDir = Path('C:\code\python')
notExistDit = Path("C:\code\python\sasdasdasdasdassd")
calcFile = Path('/project/文件处理/test.py')
print(winDir.exists())
print(winDir.is_file())
print(winDir.is_dir())
print(os.path.exists(winDir))
print(os.path.isfile(winDir))
print(os.path.isdir(winDir))
print(notExistDit.exists())
print(calcFile.exists())
print(calcFile.is_file())
print(calcFile.is_dir())
dDrive = Path('D:')
print(dDrive.exists())