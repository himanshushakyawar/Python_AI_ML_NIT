'''
Write a program to calculate the numbers between
X and Y which are divisible by 5 and 13 but not divisible 
by 10 separated by space.'''

X, Y = map(int, input().split())
count =0
for i in range(X,Y):
    if (i%5==0 and i%13==0) and i%10!=0:
        count+=1
        print(i)

