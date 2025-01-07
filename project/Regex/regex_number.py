import re

phoneNumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumregex.search('My number is 123-456-7890, is 456-123-7890')
print(mo.group()),
