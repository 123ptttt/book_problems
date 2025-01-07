"""
返回一个bool值，如果字符串中只包含字符和数字， 并且非空， 则返回True
"""
spam = 'helloworld'
print(spam.isalnum())

spam = 'helloworld123'
print(spam.isalnum())

spam = 'helloworld '
print(spam.isalnum())