"""
join是将列表变成字符串， 而split是将字符串变成列表， 两者是相反的
"""
spam = ['spam', 'eggs', 'bacon']
s = ', '.join(spam)
print(s)

spam = ('ac sv as wd wasc')
s = spam.split(' ')
print(s)