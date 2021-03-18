#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Thur Mar 18 2021

@author: jinjialiu
'''
# # Code fragment from page 15
# print('Yankee rule!')
# print('But not in Boston!')
# print('Yankee rule,', 'but not in Boston!')

# # Code fragment from page 19
# pi = 3
# radius = 11
# area = pi * (radius**2)
# radius = 14

# # Code fragment from page 20
# a = 3.14159
# b = 11.2
# c = a*(b**2)
# diameter = 11.2
# pi = 3.14159
# area = pi*(diameter**2)

# # Code fragment from page 21
# side = 1 # length of sides of a unit square
# radius = 1 # radius of a unit circle
# # subtract area of unit circle from area of unit square
# area_circle = pi*radius**2
# area_square = side*side
# difference = area_square - area_circle

# x, y = 2, 3
# x, y = y, x
# print('x =', x)
# print('y =', y)

# # Code fragments from page 23
# if x % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
# print('Done with conditional')

# x = 1111111111111111111111111111 + 22222222222222222222222 +\
#     333333333333333333333333333

# # Code fragments from page 24
# x = 1111111111111111111111111111 + 22222222222222222222222 +\
#     333333333333333333333333333

# x = (1111111111111111111111111111 + 22222222222222222222222 +
#      333333333333333333333333333)

# if x % 2 == 0:
#     if x % 3 == 0:
#         print('Divisible by 2 and 3')
#     else:
#         print('Divisible by 2 and not by 3')
# elif x % 3 == 0:
#     print('Divisible by 3 and not by 2')

# Test setup for following Code
x = 1
y = 2
z = 3

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

# Code fragments from page 25
if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    print(max(x, y, z))
if x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
    print(max(x, y))
if x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    print(max(x, z))
if x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
    print(max(y, z))
if x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
    print(x)
if x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
    print(y)
if x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
    print(z)
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print(min(x, y, z))

answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)

# Code fragement from page 26
print((x if x > z else z) if x > y else (y if y > z else z))

# Code fragment from page 29
num = 30000000
fraction = 1/2
print(num*fraction, 'is', fraction*100, '%', 'of', num)
print(num*fraction, 'is', str(fraction*100) + '%', 'of', num)

# Code fragments from page 30
print(int(num*fraction), 'is', str(fraction*100) + '%', 'of', num)
