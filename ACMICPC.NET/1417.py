import sys

N = int(input())

votes = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
"""
첫번째 사람이 가장 큰 숫자가 아니거나 가장 큰 숫자가 여러개 있으면 반복
가장 큰 숫자의 인덱스 찾기
첫번째 사람에게 1 더하고 가장 큰 숫자에서 1 빼기
카운트 1 증가
"""
while max(votes) != votes[0] or votes.count(votes[0]) > 1:
    max_index = votes[1:].index(max(votes[1:]))+1
    votes[0] += 1
    votes[max_index] -= 1
    count += 1

print(count)
