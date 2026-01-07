import sys
input = sys.stdin.readline
N = int(input())
arr = list(set([input().strip() for _ in range(N)]))
arr.sort(key=lambda x: (len(x), x))
for s in arr:
    print(s)