import re

nameRegex = re.compile(r'[A-Z][A-Za-z]+.Nakamoto')
mo = nameRegex.findall('Satoshi Nakamoto, Alice Nakamoto, satoshi Nakamoto, Nakatomo, Mr. Nakatomo')
print(mo)