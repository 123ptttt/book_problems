spam = [-1, 0, 1, 2, 3, 4, 5, 6]
spam.sort()
print(spam)

spam = ['abb', 'cd', 'ed', 'fga', 'sss', 'aac']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = ['a', 'A', 'Z', 'z']
spam.sort(key=str.lower)
print(spam)