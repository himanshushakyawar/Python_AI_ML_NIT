'''
Write a program to generate prime numbers from 1 to 1000
and save them to a text file. Read N lines of the previous files.

'''
with open('Sample.txt', 'wt') as filesample:
    for num in range(1,1000):
        prime = False
        for i in range(2,num):
            if num%i==0:
                prime = False
                break
            else:
                prime = True
        if prime == True:
            filesample.write(str(num)+ '\n')

N = int(input())        
fopen = open("Sample.txt", 'r')
fopen.readlines(N)     
fopen.close()


        
             