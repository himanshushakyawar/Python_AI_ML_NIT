'''Given below are two sets A and B.
Find the intersection and print whether is
it possible to generate 'edurela' from the output or
not.'''
from typing import Set


A = {'c','a','d','e','k','r','u','q','r','y',}
B = {'b','h','k','a','d','e','k','r','u',}


New = A.intersection(B)
# print(A)
# print(B)
# print(New)

string = "edureka"
set_string =set(string)
# print(set_string)
# print(New.difference(string)) return the set()
if len(New.difference(string))==0:
    print("Yes")
else:
    print("NO")