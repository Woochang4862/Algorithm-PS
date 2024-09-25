'''
풀이
'a1 b1' 으로 입력이 들어오면 split 으로 ['a1','b1']을 만들고 map 으로 [a1,b1]을 만든다. 그리고 sum 으로 그것의 합을 출력한다.
위 작업을 케이스 개수만큼 반복한다.
'''
import sys
for _ in range(int(input())):print(sum(map(int, sys.stdin.readline().strip().split())))
# for _ in range(int(input())):print(eval(sys.stdin.readline().strip().replace(' ','+')))