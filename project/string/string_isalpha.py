"""
返回一个bool， 如果字符串全是字母没有其他任何的字符， 并且非空， 则返回True
"""
spam = 'helloworld'
print(spam.isalpha())

spam = 'hello world123'
print(spam.isalpha())

spam = ''
print(spam.isalpha())