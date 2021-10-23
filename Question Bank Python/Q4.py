#Write a program generate N number of 
#Fibbonacci series seperated by space.
#N = N+ (N-1)

# N = int(input())
# i = 0
# j = 0
# while j < N:
#     j = j+i
#     i +=1
#     print(j, end=" ")

#Alternative, Fibbonacci of length N
N = int(input()) 
val = N
fib =[0,1]
while len(fib) < val :
    fib.append(fib[-1]+fib[-2])
print(fib)
