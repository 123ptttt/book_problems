"""
\d 可以匹配0-9以内的任何数字
\D 可以匹配除了数字之外的任何字符
\w 可以匹配任何字母，数字，下划线
\W 可以匹配字母，数字，下划线以外的字符
\s 可以匹配空格，制表符，换行符
\S 可以匹配空格，制表符，换行符以外的字符
"""
import re

xmaRegex = re.compile(r'\d+\s\w+')
mo = xmaRegex.findall('12 asdfg, 20 asdfasf')
print(mo)
# \d+ 匹配一个或者多个数字
# \s 匹配一个空格或制表符或换行符
# \w+ 匹配一个或者多个字母

#通配字符，可以匹配除了换行符以外的任何一个字符， 但是只能匹配一个字符
atRegex = re.compile(r'.at')
mo = atRegex.findall('cat fat flat sat bat')
print(mo)

#当向re.compile()中传入re.DOTALL，则.可以匹配换行符
atRegex = re.compile(r'.at', re.DOTALL)
mo = atRegex.search('\nat')
print(mo.group())