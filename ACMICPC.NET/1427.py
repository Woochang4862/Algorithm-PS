import sys; input = sys.stdin.readline
N = input()
arr = list(map(int, list(N.strip())))
arr.sort(reverse=True)
print(''.join(map(str, arr)))