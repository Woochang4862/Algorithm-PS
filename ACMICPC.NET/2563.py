import sys
N = int(input())
papers = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

board = [[0]*101 for _ in range(101)] # [[False]*101]*101 은 모든 같은 list 객체 101개가 생성이됨
for paper in papers:
    x1,y1,x2,y2 = paper[0], paper[1], paper[0]+10, paper[1]+10
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1
            
print(sum(sum(board,[])))
