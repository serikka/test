

"""

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}


"""


M = input()
M = int(M)
m = set(list(map(int, input().split())))
N = input()
N = int(N)
n = set(list(map(int, input().split())))

c = m.difference(n)
d = n.difference(m)
e = c.union(d)
#print(e)

for i in sorted(e):
    print(i,sep="\n")