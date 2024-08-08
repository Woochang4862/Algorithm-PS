# 아이디어 : 목표 높이에서 움직이는 길이를 뺀 곳 까지만 도달하면 된다. (V-A)//(A-B)
# 주의할 점 : 근데 (V-A)/(A-B) 의 나머지가 있을경우 + 1
A,B,V = map(int,input().split())
if V == A:
    print(1)
else: 
    print((V-A)//(A-B) + 1 + min(1,(V-A)%(A-B)))