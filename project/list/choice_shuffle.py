"""
多列表里面的元素进行随机的排序， 原列表不变
"""
import random

pets = ['cat', 'dog', 'horse', 'sheep']
random.shuffle(pets)
print(pets)