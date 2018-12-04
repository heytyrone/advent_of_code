# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:49:36 2018
12.2.18
Advent of Code Day 1
@author: Tyrone
"""

file1 = open('inputDay1.txt', "r")
data = file1.readlines()
sum = 0
for line in data:
    sum = sum + int(line)
print(sum)

file1.close()