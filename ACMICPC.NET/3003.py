import sys
nums = list(map(int,sys.stdin.readline().split()))
K = [1,1,2,2,2,8]
res = []
for n,k in zip(nums,K):
    res.append(str(k-n))
print(' '.join(res))