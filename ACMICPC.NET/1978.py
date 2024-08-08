_ = input()
import sys
nums = list(sorted(map(int,sys.stdin.readline().strip().split()),reverse=True))
prime_nums = []
not_prime_nums = [1]
res = []
for num in nums:
    if num in not_prime_nums:
        continue
    if num in prime_nums:
        res.append(num)
        continue
    isPrimeNum = True
    for i in range(2,num):
        if num % i == 0:
            isPrimeNum = False
            break
    if isPrimeNum:
        res.append(num)
        prime_nums.append(num)
    else:
        not_prime_nums.append(num)

print(len(res))