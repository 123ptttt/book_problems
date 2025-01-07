#大小写在正则表达式中很重要， 如果要忽略大小写的话， 那么就要向re.compile中传递re.IGNORECASE或re.I作为第二个参数
import re

robocop = re.compile('robocop', re.IGNORECASE)
mo = robocop.search('Robocop is part man')
print(mo.group())
