"""
*号之前的分组可以有无数次和零次
"""
import re
BatRegex = re.compile(r'Bat(wo)*man')
mo = BatRegex.search('Batwowowowowoman')
print(mo.group())
