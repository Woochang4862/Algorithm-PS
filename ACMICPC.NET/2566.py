import sys
row, col = 0, 0
M = 0
for i in range(9):
    nums = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if nums[j] > M:
            row = i
            col = j
            M = nums[j]
print(M)
print(row+1, col+1)