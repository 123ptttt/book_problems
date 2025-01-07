"""
可以自定义函数， 如果不符合也可以自定义回复
"""
import pyinputplus as pyip

def adduptoten(nums):
    numslist = list(nums)
    for i, digit in enumerate(numslist):
        numslist[i] = int(digit)
    if sum(numslist) != 10:
        raise Exception('the digits do not sum to 10')
    return int(nums)

response = pyip.inputCustom(adduptoten)
print(response)
