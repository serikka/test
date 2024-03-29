"""

You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.


"""
A = set(map(int, input().split()))
num_sets = int(input())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print(A.issuperset(set1) and A.issuperset(set2))
