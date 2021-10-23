#Write a program to find factorial of a given number N

# inp = int(input())
# fact = 1
# for i in range(1,inp+1):
#     fact = fact*i
# print(fact)


#Alternative 
# import math

# inp = int(input())
# print(math.factorial(inp))

# Alternative

inp = int(input())
fact =1
while inp:
    fact =fact*inp
    inp = inp -1
print(fact)
