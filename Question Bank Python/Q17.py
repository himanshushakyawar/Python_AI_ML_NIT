'''


Write a program that accepte a sequence of
numbers and print the numbers after sorting 
them separated by comma.

Input: 5 2 3 7 4
Output: 2,3,4,5,7


'''

N = int(input())
lis=[]
for i in range(0,N):
    lis.append(int(input()))
lis.sort()
print(lis)




