#Write a program to find sum of digit 
#from a given integer number N.

#Alternative 1
# num  = list(input())
# sum=0
# for i in range(0,len(num)):
#     sum = sum + int(num[i])
# print(sum)

#Alternative 2
N = int(input())
N_sum = 0
while N :
    N_sum = N_sum + N%10
    N = N//10
print(N_sum) 

