import re

#花括号里面可以是单个数字
heRegex = re.compile(r'(Ha){3}')
print(type(heRegex))
mo = heRegex.search('HaHaHa')
print(mo.group())
print(type(mo))

mo1 = heRegex.search('Ha')
print(type(mo1))

#花括号里面也可是一个范围
heRegex = re.compile(r'(Ha){2,4}')
mo2 = heRegex.search('HaHa')
print(mo2.group())

#贪心匹配
#正则表达式默认会匹配最长的字符串
heRegex = re.compile(r'(Ha){2,5}')
mo = heRegex.search('HaHaHaHaHa')
print(mo.group()) #2，3，4都是有效的， 但是匹配了5

#非贪心的匹配
heRegex = re.compile(r'(ha){2,4}?')
mo = heRegex.search('hahaha')
print(mo.group())
