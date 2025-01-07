import pyinputplus as pyip

#输入的数只能是整数
#response = pyip.inputInt()
#print(response)

#输入的类型是int或者是float， 看是否有小数点
#response = pyip.inputNum()
#print(response)

#输入为字符串
response = pyip.inputStr()
print(type(response))
print(help(pyip))

#还有很多， 用到再学