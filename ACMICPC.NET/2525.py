'''
풀이
2884번에서 풀이1번처럼 파이썬 내장 모듈인 datetime 의 datetime과 timedelta 를 이용하면 아주 쉽게 문제를 해결할 수 있다.
datetime.now()로 년월일을 현재로 초기화해주고 replace 함수를 이용하여 시간과 분을 입력으로 바꿔서 now 라는 인스턴스를 만들어준다
timedelta(minutes=C) 'C분후'(C가 음수라면 |C|분전)을 의미하는 인스턴스를 만들어서 now 에 더해준다.
'''
import sys
from datetime import datetime, timedelta
A,B=map(int,sys.stdin.readline().split())
C=int(sys.stdin.readline())
now = datetime.now().replace(hour=A,minute=B)
now += timedelta(minutes=C)
print(now.hour, now.minute)