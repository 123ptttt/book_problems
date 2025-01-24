"""
使用斜杠来连接路径的时候， 必须要有Path对象
"""
from pathlib import Path

print(Path('spam') / 'break' / 'sdasd')

print(Path('spam') / Path('C/code/python'))

