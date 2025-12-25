
# WAP to print "hello world"
# print("hello world")

# wap to add two numbers
# a = 3
# b = 4
# sum = a + b
# print(sum)

# wap to input two numbers and find their sum
# num1 = int(input("enter a number"))
# num2 = int(input("enter another number"))

# print( num1 + num2)

# wap to check if a number is odd or even

# num1 = int(input("enter a number"))

# if(num1 %2 == 0):
    
#     print('even number')
    
# else:
#     print('odd')

# 5) same question but using a function
# num1 = int(input('enter a number'))

# def check(num1):
#     if(num1 %2 == 0):
    
#         print('even number')
    
#     else:
#         print('odd')

# check(num1)


# 6) wap to take an input 'n' and print upto n.
# n = int(input('enter a number:'))
# for i in range(0,n+1):
#     print(i)

# 7) wap to find the sum of odd numbers upto n using function

def calc():
    n = int(input('enter a number'))
    sum = 0
    for i in range(0,n+1):
        if(i % 2 != 0):
            sum += i
    return sum

print(f"sum of odd numbers: {calc()}")


#wap to find whether a number is palindrome or not.
# Method 1:
# def calc():
#     num = int(input('enter a number'))
#     temp = num
#     rev = 0
#     while(num > 0):
#         rem = num % 10
#         rev = rev * 10 + rem
#         num = num // 10
    
#     if(temp == rev):
#         print("palindrome")
#     else:
#         print("not palindrome")

# calc()

# 9) wap to input two coordinates and find the distance between them

# import math
# x1 = int(input('enter x1 '))
# x2 = int(input('enter x2 '))
# y1 = int(input('enter y1 '))
# y2 = int(input('enter y2 '))

# def calc(x1,x2,y1,y2):
#     xValue = math.pow(x2 - x1,2)
#     yValue = math.pow(y2 - y1,2)
#     distance = math.sqrt(xValue + yValue)
#     print(round(distance))

# calc(x1,x2,y1,y2)


# import datetime
# curr = datetime.datetime.now()
# name = input("enter the name:")
# address = input("enter the address:")
# dob = int(input("enter ur dob:"))
# age = curr.year - dob

# if(age >= 18):
#     print(f"the person is eligible, name: {name} age: {age} address: {address}")
# else:
#     print(f"the person is not eligible, name: {name} age: {age} address: {address}")