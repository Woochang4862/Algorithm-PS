N = int(input())
import sys
xs, ys = [], []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    xs.append(x)
    ys.append(y)

area = (max(xs) - min(xs))*(max(ys) - min(ys))
print(area)