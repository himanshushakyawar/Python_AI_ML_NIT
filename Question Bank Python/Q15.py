'''
15.Write a program that calculate number of 
lowercase, uppercase and numbers alphabets.

string method:
islower()
isupper()
isdigit()

'''

n = input()
upper=0
lower=0
digit=0
for i in n:
    if i.isupper()==True:
        upper+=1
    if i.islower()==True:
        lower+=1
    if i.isdigit()==True:
        digit+=1

print("Uppercase characters: ",upper)
print("Lowercase characters: ",lower)
print("Number: ", digit)









