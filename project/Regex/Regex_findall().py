import re

#在没有分组的情况下， findall（）返回一个字符串列表
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('123-456-7894 is 213-654-4654')
print(mo)

#在有分组的情况下， 会返回一个元祖, 分组中的元素就是字符串的子字符串
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('123-456-7894 is 321-654-8745')
print(mo)

phoneNumRegex = re.compile('(\d\d\d)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('123-456-7898')
print(mo)

"""
与search的比较：
1,
search方法放回的是一个Match对象， 有group方法
findall()方法是返回一个元祖或者是一个字符串列表

2,
search方法只找到第一个匹配的对象
findall方法会找到全部都对象
"""