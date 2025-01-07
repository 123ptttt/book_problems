import pyinputplus as pyip

#'limit = 2' signifies that a number can be input at most 2 times
response = pyip.inputNum(limit=2)
print(response)

#'timeout = 12' signifies that you should input a number within 12 seconds
response = pyip.inputNum(timeout=12)
print(response)

#'default = 'N\A'' signifies that you can receive a default response of 'N\A' if you break the rule
response = pyip.inputNum(limit=2 ,default='N\A')
print(response)