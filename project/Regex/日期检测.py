import re

dateRegex = re.compile(r"""(^.*?)
    ((0|1)?\d) #one or two digit for the month
    ((0|1|2|3)?\d) #for the day
    (([10-29])\d\d) #for the year
""")