import re

#贪心的匹配
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
mo = nameRegex.search('First name: peng Last name: teng')
print(type(mo))
print(mo.group(1))

#非贪心的匹配
nonRegex = re.compile(r'<.*?>')
mo = nonRegex.search('<To serve you> the man>')
print(mo)

nonRegex = re.compile(r'<.*>') #匹配一个左括号， 任意字符， 一个右括号
mo = nonRegex.search('<To serve you> the man>')
print(mo)

#当向compile中传递一个参数re.DOTALL，此时就能匹配所有的字符了
nonRegex = re.compile(r'.*', re.DOTALL)
mo = nonRegex.search('saf\nsad')
print(mo)
