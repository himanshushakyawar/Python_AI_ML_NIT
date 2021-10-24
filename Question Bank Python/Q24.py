'''

Write a program to calculate all possible permutation
for a given sequence of numbers.

'''

n = int(input())
seq = list(map(int, input().split()))
perms = [[]]

for num in seq:
    temp = []
    for perm in perms:
        for i in range(len(perm)+1):
            temp.append(perm[:i] + [num] + perm[i:])
            perms = temp

print("Permutation: ", perms)