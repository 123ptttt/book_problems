"""
返回一个列表，分隔符之前的文本， 分隔符， 分隔符之后的文本
"""
spam = 'hello, world'
s = spam.partition(' ')
print(s)

spam = 'hello, world'
s = spam.partition('o')
print(s)