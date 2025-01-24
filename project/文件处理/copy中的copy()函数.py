import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam)) #2675159690624分配的内存
cheese = copy.copy(spam)
print(id(cheese)) #1746573741760分配的内存， 和之前的指向不一样了， 说明创建了一个新的列表
cheese[1] = 'C'
print(spam) #因此修改cheese的时候， spam不会变