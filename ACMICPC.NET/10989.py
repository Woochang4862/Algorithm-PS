# import sys
# count_list = [0]*10001
# for _ in range(int(sys.stdin.readline())): count_list[int(sys.stdin.readline())] += 1
# for i in range(10001): 
#     if count_list[i] != 0:
#         for _ in range(count_list[i]):
#             print(i)

import sys
from collections import defaultdict
count_dict = defaultdict(int)
for _ in range(int(sys.stdin.readline())): count_dict[int(sys.stdin.readline())] += 1
count_list = list(sorted(count_dict.items()))
for number, count in count_list: 
    for _ in range(count):
            print(number)