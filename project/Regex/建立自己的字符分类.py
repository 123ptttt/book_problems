import re

#可以在中括号里面自己定义自己想要找的符号， 但是用普通的正规符号就有点不太行了
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('asad safag asnonag asdjnakg asfasg.')
print(mo)

numRegex = re.compile(r'[0-9a-z]')
mo = numRegex.findall('2sac a1sc, asd4ac asda551')
print(mo)

#将^加进来就是匹配除了0-9a-z以外的字符
numRegex = re.compile(r'[^0-9a-z]')
mo = numRegex.findall('2sac a1sc, asd4ac asda551')
print(mo)