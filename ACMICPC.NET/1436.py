import re

N = int(input())
res = []
i=0
while True:
    if re.match('\d*6{3,}\d*',str(i)):
        res.append(i)
    i+=1
    if len(res) == N:
        break
print(res[-1])
