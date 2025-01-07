import pyinputplus as pyip

#the valuse should be between 1 and 100
response = pyip.inputNum('Enter a number: ', min = 1, max = 100)
print(response)

#the values should be greater Than 4
#使用lessthan关键字也是同理
response = pyip.inputNum('Enter a number: ', greaterThan=4)
print(response)