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

def solution(M,N,board):
    res = []
    for case in ["CASE_BLACK", "CASE_WHITE"]:
        for i in range(M-8+1):
            for j in range(N-8+1):
                number_of_refill = 0
                for row in range(i,i+8):
                    if case == "CASE_BLACK":
                        for a,b in zip(board[row][j:j+8],"WBWBWBWB" if row % 2 == 0 else "BWBWBWBW"):
                            if a != b:
                                number_of_refill += 1
                    else:
                        for a,b in zip(board[row][j:j+8],"BWBWBWBW" if row % 2 == 0 else "WBWBWBWB"):
                            if a != b:
                                number_of_refill += 1
                res.append(number_of_refill)
    return res

def test_with_input():
    import sys
    M, N = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(M)]
    print(min(solution(M,N,board)))

def test_with_text_case_file():
    with open('1018_test_case.txt', 'r') as f:
        while True:
            M, N = map(int, f.readline().strip().split())
            if M==-1 or N == -1:
                break
            board = [list(f.readline().strip()) for _ in range(M)]
            print(min(solution(M,N,board)))

test_with_text_case_file()