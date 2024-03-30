

"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

"""

test_cases = int(input())

for i in range(test_cases):
    num_A = int(input())
    A = set(map(int, input().split()))
    num_B =int(input())
    B = set(map(int, input().split()))
    print(bool(A.issubset(B)))

