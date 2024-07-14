N=int(input())
import sys
strs = [sys.stdin.readline() for _ in range(3)]
for s in strs:
    print(s[0],s[-2],sep='')