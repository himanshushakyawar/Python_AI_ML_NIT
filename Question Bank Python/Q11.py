'''
Write a program that accepts N values and
print it as a list
Input : 5 1 2 3 4 5
Output :[1, 2, 3, 4, 5]
'''
# Alternative One
# lis_len = list(map(int,input().split()))
# lis_len.pop(0)
# print(lis_len)

#Alernative Two
lis_len = list(input().split())
lis = []
for i in range(1,int(lis_len[0])+1):
    lis.append(int(lis_len[i]))
print(lis)

