import sys
inputs = sys.stdin.readlines()
for input_ in inputs:
    print(sum(map(int,input_.split())))