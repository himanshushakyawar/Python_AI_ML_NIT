'''

Write a program to find the Nth number of a
Arthematic Progression when initial number(a)
and difference(d) are given.
Input: 4 2 3
output: 11

'''


n = int(input())
a = int(input())
d = int(input())

num = a +(n-1)*d
print(num)