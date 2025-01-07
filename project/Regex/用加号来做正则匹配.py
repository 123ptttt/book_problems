"""
和星号差不多， 不过是前面的分组(也可以是单个字符什么的)要出现一次或者多次

如果要出现+号， 则需要使用转义字符
"""
import re

AddRegex = re.compile(r'Bat(wo)+man')
mo = AddRegex.search('Batwowowowoman')
print(mo.group())