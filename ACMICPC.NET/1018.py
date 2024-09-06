'''
M,N
if M 짝:
BW... n(B) - n(W) = 0 or 1
WB... n(W) - n(B) = 0 or 1
...
BW... n(B) - n(W) = 0 or 1
WB... n(W) - n(B) = 0 or 1
==> n(B) == n(W)

if M 홀:
BW... n(B) - n(W) = 0 or 1
WB... n(W) - n(B) = 0 or 1
...
BW... n(B) - n(W) = 0 or 1
WB... n(W) - n(B) = 0 or 1
BW... n(B) - n(W) = 0 or 1
	if N 짝 => n(B) == n(W)
	if N 홀 => abs(n(B) - n(W)) == 1
'''

import sys
M, N = map(int, input().split())
print(M,N)
board = [list(sys.stdin.readline().strip()) for _ in range(M)]

number_of_black = 0
number_of_white = 0
for line in board:
    number_of_black += N - line.count('B')
    number_of_white += N - line.count('W')

print(number_of_black,number_of_white)