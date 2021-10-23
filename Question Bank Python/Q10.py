'''
Write a program to generate the following out
input : None

output: 
1

2 3

3 4 5

4 5 6 7

5 6 7 8 9

'''
for i in range(0,6):
    # print(i+1, end=" ")
    for j in range(i):
        print(i+j, end=" ")
    print("\n")
    
