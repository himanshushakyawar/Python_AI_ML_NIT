'''Write a program which accepts a string from console 
and print the words in reverse order.
Input : Hello my name is XYZ
Output : XYZ is name my hello
'''

sen = input().split()

for i in sen:
    print(i[::-1], end=" ")