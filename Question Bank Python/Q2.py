#Write a program to create a list of even number
#starting from x to y

# x,y = map(int,input().split())
# even_list=[]
# if x%2==0:
#     for i in range(x,y+1,2):
#         even_list.append(i)
# else:
#     x = x -x%2
#     for i in range(x,y+1,2):
#         even_list.append(i)
# print(even_list)


#Alternative

x,y = map(int,input().split())
even_list = list(range(x,y+1,2))
print(even_list)
