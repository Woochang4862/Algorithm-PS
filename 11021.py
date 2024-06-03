import sys
N = int(sys.stdin.readline())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i,(a,b) in enumerate(nums,1):
    print(f"Case #{i}: {a+b}")