'''
Write a program to concatenate the following dictionaries
dict1 = {'A':10, 'B':20}
dict2 = {'C':30, 'D':40}
dict3 = {'E':50, 'F':60}
'''

dict1 = {'A':10, 'B':20}
dict2 = {'C':30, 'D':40}
dict3 = {'E':50, 'F':60}


dict={}
dict.update(dict1)
dict.update(dict2)
dict.update(dict3)
print(dict)