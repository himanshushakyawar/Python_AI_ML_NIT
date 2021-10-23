#Write a program to replace the given word
#X with Y from a string

string = input("Enter the string")
x,y = map(str,input().split(' '))
string = string.replace(x,y) #string.replace() doesnt affect the original string
print(string)