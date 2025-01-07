"""
删除字符串中的空格，
"""
spam = '  hello world   '
#消除左边的空格
s = spam.lstrip()
print(s)
#消除右边的空格
s = spam.rstrip()
print(s)
#消除全部的空格， 其中strip（）可以制定两边需要删除的字符
s = spam.strip()
print(s)

spam = 'aaaSamps'
s = spam.strip('Sa')
print(s)