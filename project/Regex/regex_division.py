"""
可以使用括号对字符串进行分组， 用下标来表示那一组
"""
import re

phoneNumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumregex.search('my phone number is 123-564-4567')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))

#groups方法来一次得到所有的分组
print(mo.groups())
a, b = mo.groups()
print(a)
print(b)