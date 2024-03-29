
"""
We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

"""


elements1 = int(input())
A = set(map(int, input().split()))
N = int(input())


for i in range(N):
    command, elem = input().split()
    elem = int(elem)
    A1 = set(map(int, input().split()))
    if command == "intersection_update":
        A.intersection_update(A1)
        #print(A)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(A1)
        #print(A)
    elif command == "update":
        A.update(A1)
        #print(A)
    elif command == "difference_update":
        A.difference_update(A1)
        #print(A)
    
print(sum(A))
