from pathlib import Path
import os

#星号代表任意多个字符， 类似与正则表达式一样的
p = Path('C:\code\python\书上的例题\project')
print(list(p.glob('*.py')))

#问号代表匹配任意单个字符
p = Path('C:\code\python\书上的例题\project')
print(list(p.glob('tes?.py')))
#list(p.glob('*.?x?'))
#list(p.glob('*.txt'))
#类似的