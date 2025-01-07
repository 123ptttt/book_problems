from pathlib import Path
import os
"""
p = Path('C:\code\python\project\Colltaz.py')

#根文件夹
print(p.anchor)
print(type(p.drive))
#返回到是一个Path对象， 而不是字符串
print(type(p.parent))
#文件名， 由主干名（stem）和后缀名（suffix）组成
print(p.name)
print(p.stem)
print(p.suffix)
"""
"""
#parents属性， 父节点的级别
p = Path.cwd()
print(p)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
"""
p = 'C:\code\python\project\Colltaz.py'
print(os.path.basename(p))
print(os.path.dirname(p))
print(os.path.split(p)) #返回的是元组
print(p.split(os.sep)) #返回一个列表