"""
返回一个类似列表的东西， 当不是列表， 不可以修改， 没有append（）方法
类似的还有values（）， items（）方法
"""
spam = {'name': 'pengteng', 'age': 45}
for key in spam.keys():
    print(key)

s = spam.keys()
print(s)