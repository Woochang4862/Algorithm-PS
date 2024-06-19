max_id = 0
max_num = -1
import sys
for i in range(1,10):
    temp = int(sys.stdin.readline())
    if max_num < temp:
        max_id = i
        max_num = temp

print(max_num)
print(max_id)