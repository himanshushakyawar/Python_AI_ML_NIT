'''
Create a dictionary from the following keys:

'''


dict = {'Name': [], 'Class': [], 'Age':[]}

for n in range(5):
    dict['Name'].append(input("Enter Name : "))
    dict['Class'].append(input("Enter Class : "))
    dict['Age'].append(input("Enter Age : "))

print(dict)
