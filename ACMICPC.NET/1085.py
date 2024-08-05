x,y,w,h = map(int, input().split())

right = abs(x-w) # 오른쪽 벽과의 거리
top = abs(y-h) # 위쪽 벽과의 거리
left = x # 왼쪽 벽과의 거리
bottom = y # 아래쪽 벽과의 거리
print(min(left,right,top,bottom))