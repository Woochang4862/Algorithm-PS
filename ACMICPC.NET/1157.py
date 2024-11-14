from collections import Counter

word = input().strip().upper() # 대문자로 변환
counter = Counter(word)
common = counter.most_common() # 내림차순 딕셔너리로 변환
print(common)

if len(common) > 1 and common[0][1] == common[1][1]: # 내림차순으로 정렬되어 있음
    print('?')
else:
    print(common[0][0])