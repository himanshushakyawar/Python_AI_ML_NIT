'''
Write a program to generate a seqence of
N numbers of a geometric progression when 
intial number (a) and common ratio(r) is given.
print the sequence as a list.

Input:
Output:

Gp = a + a*r +a*r^2

'''
N,a,r = map(int,input().split())
list=[]
for i in range(0,N):
    list.append(a*(r**i))
print(list)


