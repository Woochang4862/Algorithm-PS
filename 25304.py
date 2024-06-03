import sys
total = int(sys.stdin.readline())
N = int(sys.stdin.readline())
items = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for price, num in items:
    total -= price*num
print("Yes" if total == 0 else "No")