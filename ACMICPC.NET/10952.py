import sys
while True:
    s = sum(map(int,sys.stdin.readline().split()))
    if s == 0:
        break
    print(s)