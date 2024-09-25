SOLUTION = 1
if SOLUTION == 1:    
    '''
    풀이1
    파이썬 내장 모듈인 datetime 의 datetime과 timedelta 를 이용한다
    datetime.now()로 년월일을 현재로 초기화해주고 replace 함수를 이용하여 시간과 분을 입력으로 바꿔서 now 라는 인스턴스를 만들어준다
    timedelta(minutes=-45) '45분전'을 의미하는 인스턴스를 만들어서 now 에 더해준다.
    '''
    import sys
    from datetime import datetime, timedelta
    h,m=map(int,sys.stdin.readline().split())
    now = datetime.now().replace(hour=h, minute=m)
    now += timedelta(minutes=-45)
    print(now.hour, now.minute)

else:
    '''
    풀이2
    직접 알고리즘을 만들어서 해결한다.
    45분전 시간을 계산할때 
    45분보다 크거나 같으면 단순히 빼주면 된다.
    그렇지 않으면 60 + (m - 45) 이와 같이 계산 되므로 m + 20이 된다.
    대신 이 경우에는 시간을 -1 해줘야하는데 시간이 0 일때는 23이 되도록 해준다.
    '''
    import sys
    from datetime import datetime, timedelta
    h,m=map(int,sys.stdin.readline().split())
    if m >= 45:
        print(h,m-45)
    else:
        if h == 0:
            h = 23
        else:
            h -= 1
        print(h,m+15)