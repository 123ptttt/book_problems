"""
返回一个（key， value）的元组
"""
spam = {'name': 'job', 'age': 42}
for i in spam.items():
    print(i)

for key, value in spam.items():
    print(key, value, sep=',')

s = spam.items()
print(s)

print(type(s))
