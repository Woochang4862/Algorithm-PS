N = int(input())
res = 0
for i in range(1,N+1):
    s = 0
    tmp = i
    while tmp != 0:
        s += tmp % 10
        tmp //= 10
    if N == i + s:
        res = i
        break
print(res)