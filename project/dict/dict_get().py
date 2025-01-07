"""
无需判断是否在字典里， 有两个参数（key， 默认值（如果不存在key， 则使用这个默认值））
"""
spam = {'fruit': 'apple', 'age': 15}
print('i have ' + str(spam.get('age', 20)) + ' years old')
print('i have ' + str(spam.get('sss', 20)) + ' years old')