import sys
count_x = dict()
count_y = dict()
for _ in range(3):
    x,y = map(int, sys.stdin.readline().strip().split())
    if x in count_x:
        count_x[x] = 2
    else:
        count_x[x] = 1
    
    if y in count_y:
        count_y[y] = 2
    else:
        count_y[y] = 1

for x, count in count_x.items():
    if count == 1:
        print(x, end=' ')

for y, count in count_y.items():
    if count == 1:
        print(y, end='')