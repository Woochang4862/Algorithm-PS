import sys
angles = []
for _ in range(3):
    angles.append(int(sys.stdin.readline()))
num_of_unique = len(set(angles))
if sum(angles) != 180:
    print('Error')
elif num_of_unique == 3:
    print('Scalene')
elif num_of_unique == 2:
    print('Isosceles')
else:
    print('Equilateral')