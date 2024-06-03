import sys
x,y=[int(sys.stdin.readline()) for _ in range(2)]
if x*y>0:
    if x > 0:
        print(1)
    else:
        print(3)
else:
    if x > 0:
        print(4)
    else:
        print(2)