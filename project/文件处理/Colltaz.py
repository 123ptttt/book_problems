"""
import sys
def Colltaz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number // 2 + 1
print("Enter the number")
num = int(input())
while True:
    num = Colltaz(num)
    if num == 1:
        print(num)
        sys.exit()
    print(num)

"""
import sys
def Colltaz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number // 2 + 1
print("Enter the number")
try:
    num = int(input())
    while True:
        num = Colltaz(num)
        if num == 1:
            print(num)
            sys.exit()
        print(num)
except ValueError:
    print("please enter an integer")


