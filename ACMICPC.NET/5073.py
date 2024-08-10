import sys
while True:
    angles = list(map(int,sys.stdin.readline().strip().split()))
    if sum(angles) == 0:
        break
    num_of_unique = len(set(angles))
    if sum(angles) - 2*max(angles) <= 0:
        print('Invalid')
    elif num_of_unique == 3:
        print('Scalene')
    elif num_of_unique == 2:
        print('Isosceles')
    else:
        print('Equilateral')