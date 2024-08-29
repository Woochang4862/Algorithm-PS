from itertools import permutations

N, M = map(int,input().split())
cards = list(map(int,input().strip().split()))
res = []
for p in permutations(cards, 3):
    tmp = sum(p)
    if tmp <= M:
        res.append(tmp)

print(max(res))