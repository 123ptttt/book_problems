"""
read_text（）用来将文件中的字符以字符串的形式给出
write_text()用来向文件中写入字符
"""

from pathlib import Path

p = Path('spam.txt')
p.write_text('hello, world!!!')
print(len(p.read_text()))