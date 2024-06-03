import sys
A,B = tuple(map(int,sys.stdin.readline().split()))
res = "=="
if A > B:
    res = ">"
elif A < B:
    res = "<"
print(res)