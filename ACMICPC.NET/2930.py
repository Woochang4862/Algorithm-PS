'''
N | 한줄의 정사각형 갯수 | 점의 갯수 = (한줄의 정사각형 갯수+1)^2
0   2^0		 
1   2^1		 
2   2^2
3   2^3		 
n   2^n                  (2^n+1)^2
'''
print((2**int(input())+1)**2)