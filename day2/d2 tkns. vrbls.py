# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:33:36 2026

@author: sri4s
"""

print("Assign multiple values to multiple variables")

num1,num2,num3 = 10, 20, 30
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)

print(id(num1))
print(id(num2))
print(id(num3))

print("all variable refernces are: ", id(num1), id(num2), id(num3))

print("assign single value to multiple varibles")

num4 = num5 = num6 = 40
print("num4", num4)
print("num5", num5)
print("num6", num6)
print("memory locations for num4, num5, num6", id(num4), id(num5), id(num6))

print(" if the assigned varible values > 255")

num4 = num5 = num6 = 300
print("num4", num4)
print("num5", num5)
print("num6", num6)
print("memory locations for num4, num5, num6", id(num4), id(num5), id(num6))

num4 = 300
num5 = 300
num6 = 300

print("memory locations for num4, num5, num6", id(num4), id(num5), id(num6))

print("swaping of two numbers")
a , b = 10,20
print("before swaping")
print(a ,b, id(a),id(b))
a,b = b,a
print("after swAPing")
print(a ,b, id(a),id(b))




























