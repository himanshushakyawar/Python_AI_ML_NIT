#Write a program to find the given number 
#is Armstrong number or not and print out 
#as "Yes" or "No"
num = input()
num_list = list(num)
if int(num) == sum(int(num_list[i])**3 for i in range(len(num_list))):
    # //Debugging print(sum(int(num_list[i])**3 for i in range(len(num_list))))
    print("Yes")
else:
    print("No")
    # //Debugging print(sum(int(num_list[i])**3 for i in range(len(num_list))))
    
