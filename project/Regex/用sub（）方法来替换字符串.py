import re

nameRegex = re.compile(r'Argent \w+')
mo = nameRegex.sub('CENSODED', 'Argent sagas is a beautiful day') #sub方法是返回一个字符串
print(mo)

#也可用\1,\2,\3来替换第（1， 2， 3）的分组
agentRegex = re.compile(r'Argent (\w)\w*')
mo = agentRegex.sub('\1****','Argent sagas is a beautiful')
print(mo)