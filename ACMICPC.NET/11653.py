N = int(input())
import math
for i in range(2,int(math.sqrt(N))+1):
    while N % i == 0:
        print(i)
        N //= i

if N > 1:
    print(N)