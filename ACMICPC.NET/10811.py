import sys
N, M = tuple(map(int,sys.stdin.readline().split()))
q = []
baskets = [i for i in range(1,N+1)]
for _ in range(M):
    q.append(tuple(map(int,sys.stdin.readline().split())))
for i,j in q:
    baskets = baskets[:i-1]+list(reversed(baskets[i-1:j]))+baskets[j:]
print(' '.join(map(str,baskets)))