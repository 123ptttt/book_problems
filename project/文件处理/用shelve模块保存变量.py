import shelve

"""
类似于数据库， 但是操作的形式和字典差不多
"""

shelfFile = shelve.open('mydata')
cats = ['zopihe', 'jary', 'bob', 'alice']
shelfFile['cats'] = cats
shelfFile.close()


shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print(shelfFile.keys())
for key in shelfFile.keys():
    print(key)
print(shelfFile.values())