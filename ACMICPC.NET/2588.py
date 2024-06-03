import sys
a,b = [sys.stdin.readline() for _ in range(2)]
a = int(a)
b1,b2,b3 = int(b[0]), int(b[1]), int(b[2])
print(a*b3,a*b2,a*b1,a*int(b),sep='\n')