'''
a1*n + a0 <= c*n
0 <= (c-a1)*n - a0

1. c == a1
-a0 >= 0
2. c > a1
(c-a1)*n0 - a0 >= 0
3. c < a1
false (수직선 상에 표현해보면 이해됨!)
'''

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c == a1:
    print(int(-a0 >= 0))
elif c > a1:
    print(int((c-a1)*n0 - a0 >= 0))
else:
    print(0)