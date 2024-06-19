nums = []
for i in range(10):
    nums.append(int(input()))
nums = set(map(lambda x:x%42,nums))
print(len(nums))