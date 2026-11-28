# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:06:11 2026

@author: sri4s
"""

###In this task, we would like for you to appreciate the usefulness of the groupby() 
##function of itertools . To read more about this function, Check this out .

##You are given a string S Suppose a character 'c' occurs consecutively X times in the string.
## Replace these consecutive occurrences of the character 'c' with (x,c) in the string.

s = input()

count = 1
result = []

for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count = count+1
    else:
        result.append((count, s[i-1]))
        count = 1
result.append((count, s[-1]))

print(result)

from itertools import groupby
s = input()
result = []

for key, group in groupby(s):
    result.append((len(list(group)), key))

print(result)    