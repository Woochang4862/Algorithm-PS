import sys
N, M = list(map(int,sys.stdin.readline().split()))
q = []
baskets = [i for i in range(1,N+1)]
for _ in range(M):
    q.append(tuple(map(int,sys.stdin.readline().split())))

for i,j in q:
    tmp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = tmp

print(' '.join(map(str,baskets)))