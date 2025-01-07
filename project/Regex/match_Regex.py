import re

match_Regex = re.compile(r'(Alice|Bob|Carol).(eats|pets|throws).(apples|cats|baseballs)')
mo = match_Regex.findall('Alice eats apples')
print(mo)