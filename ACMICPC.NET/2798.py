from itertools import combinations # 가능한 모든 조합 계산

N, M = map(int,input().split()) # N : 카드의 개수, M : 목표 숫자
cards = list(map(int,input().split()))
res = []
for p in combinations(cards, 3):
    tmp = sum(p)
    if tmp <= M:
        res.append(tmp)

print(max(res))