import sys
a,b,c = map(int,sys.stdin.readline().strip().split())
sticks = [a,b,c]
M = max(a,b,c)
sum_of_others = sum(sticks) - M

'''
1. M 이 나머지 두변과 같은때
2. M 이 나머지 두변보다 작을때
3. M 이 나머지 두변보다 클때
'''
if sum_of_others == M:
    print(sum_of_others + M - 1)
elif sum_of_others > M:
    print(sum_of_others + M)
else:
    print(2*sum_of_others - 1)
