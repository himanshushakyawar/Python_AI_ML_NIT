#Write a program to generate the following pattern
# for given depth N.
'''input: 5
Output: 
    *     
   ***
  *****
 *******
*********
'''
# Alternative 1
# depth = int(input())
# inp =2*depth
# for i in range(1,inp+1,2):
#     print('{0:^{1}}'.format("*"*i,inp)) 

#Alternative 2
depth = int(input())
inp = 2*depth
for i in range(1,inp,2):
    print(" "*(inp-i//2 - 1) + "*"*i)
