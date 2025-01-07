"""
?的作用就是可以决定？前面的是要还是不要， 可以要也可以不要
"""
import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('i am a Batman')
print(mo1.group())

mo2 = batRegex.search('i am a Batwoman')
print(mo2.group())

#也可以选中分不分组
batRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = batRegex.search('my number is 123-564-7987')
print(mo1.group())

mo2 = batRegex.search('my number is 564-7987')
print(mo2.group())