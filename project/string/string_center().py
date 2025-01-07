"""
如果字符数目不够的话， 会自动填充还可以自己定义填充的字符， 默认是空格
"""
spam = 'hello'
s = spam.center(30, '-')
print (s)