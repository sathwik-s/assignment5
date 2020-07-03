# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:23:27 2020

@author: SATHWIK
"""


  
lst = []
num = int(input('Number of elements in the list: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))