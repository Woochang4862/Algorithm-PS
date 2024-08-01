import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
nums = list(range(M,N+1))
res = []
for num in reversed(nums):
    if num == 1:
        continue
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        res.append(num)

if len(res) != 0:
    print(sum(res),min(res),sep='\n')
else:
    print(-1)