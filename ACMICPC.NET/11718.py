import sys

while True:
  s = sys.stdin.readline().strip() # 공백이랑 개행문자 제거
  if s == '':
    break
  else:
    print(s)