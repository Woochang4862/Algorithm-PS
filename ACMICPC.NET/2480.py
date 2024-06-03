import sys
dicies = list(map(int,sys.stdin.readline().split())) # map은 iterator 이므로 한번 iteration을 돌면 다시 사용불가
num_distinct_dicies = len(set(dicies))
if num_distinct_dicies == 3: # 모두 다른
    print(max(dicies)*100)
elif num_distinct_dicies == 2: # 하나만 다른 경우
    a = list(set(dicies))[0]
    b = list(set(dicies))[1]
    num_a = list(dicies).count(a)
    num_b = list(dicies).count(b)
    c = a if num_a > num_b else b
    print(1000+c*100)
else: # 다 같은 경우
    print(10000+list(dicies)[0]*1000)