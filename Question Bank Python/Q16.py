'''


Write a program to find whether
a given string is palindrom or not

Input: madam
Output: Yes or No


'''
word = list(input())
print(word)
re_word = word[::-1]
# print(re_word)
if str(word) == str(re_word):
    print("Yes")
else:
    print("No")
