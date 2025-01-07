import pyinputplus as pyip

#允许接受的字符串列表， 即使要输入的是数字和字符
#we accpte a list of strings, even if  they contain a mix of numbers and letters
response = pyip.inputNum(allowRegexes=[r'(I|A)+', r'zero'])
print(response)

#不允许接受的字符串列表
response = pyip.inputNum(blockRegexes=[r'(I|A)+', r'zero'])
print(response)