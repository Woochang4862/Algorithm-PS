import sys
N, M = list(map(int,sys.stdin.readline().split()))
q = []
baskets = [0] * N
for _ in range(M):
    q.append(tuple(map(int,sys.stdin.readline().split())))

for i,j,k in q:
    for basket_num in range(i,j+1):
        baskets[basket_num-1] = k

print(' '.join(map(str,baskets)))