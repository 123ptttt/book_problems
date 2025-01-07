import re

#会匹配第一次出现的分组
heroregex = re.compile(r'Bateime|Tina Fey')
mo = heroregex.search('Bateime Tina Fey')
print(mo.group())

mo1 = heroregex.search('Tina Fey Bateime')
print(mo1.group())

batregex = re.compile(r'Bat(mobile|phone|ssss)')
mo2 = batregex.search('Batphone Phtoe ssaga')
print(mo2.group())
print(mo2.group(1))
