#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: wenbin
@file: 100-Skills.py
@time: 2021/07/17/15/28
"""
# skill-01
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")

