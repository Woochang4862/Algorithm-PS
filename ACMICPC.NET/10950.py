import sys
N = int(sys.stdin.readline())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for a,b in nums:
    print(a+b)