'''

Given below a list of integers, find the triplets
whose sum if equal to zero and print them as tuples.

[4,0,-2,-1,2,3]

'''

list = [0,2,3,4,5,6,9,-1,-9,-7,-6,-5,-4,-3,-2]
#One Way
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         for k in range(j+1,len(list)):

#             if (list[i]+list[j]+list[k])==0:
#                 print((list[i],list[j],list[k]))

#Alternative

list = [0,2,3,4,5,6,9,-1,-9,-7,-6,-5,-4,-3,-2]
n =len(list)
s = set()
for i in range(0,n):
    
    for j in range(i+1,n):
        x = -(list[i] + list[j])
    
    if x in s:
        print((x,list[i],list[j]))
    else:
        s.add(list[j])

