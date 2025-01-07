import re

#必须要以hello开头的字符串
beginwithworld = re.compile('^hello')
mo = beginwithworld.search('hello world')
print(mo)
print(mo.group())

#必须要以数字结尾的字符串
endnumRegex = re.compile('\d$')
mo = endnumRegex.search('ssadasd is 45')
print(mo)
print(mo.group())