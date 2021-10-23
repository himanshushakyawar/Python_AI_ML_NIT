'''
Write a program to generate the following pattern
    *    
   ***   
  *****
 *******
*********

'''

# for i in range(1,10,2):
#     print('{0:^9}'.format("*"*i))

# Alternative
for i in range(1,10,2):
    print(" "*(4-i//2) +"*"*i)  