"""
文本对齐， 意思是将其放在字符串为（）的字符串中， 向左（右）对齐
"""
spam = 'hello world'
s = spam.ljust(20, '-')
print(s)

spam = 'hello world'
s = spam.rjust(30, '-')
print(s)

