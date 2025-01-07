"""
如果想要忽略掉正则表达式中的注释和空格，向re.compile()中传入re.VERBOSE作为第二个参数
"""

import  re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

#可以改成以下形式

phoneRegex = re.compile(r"""
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)? #separator
    \d{3} #first 3 digits
    (\s|-|\.) #separator
    \d{4} #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
""", re.VERBOSE)