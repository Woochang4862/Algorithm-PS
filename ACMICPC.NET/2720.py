import sys
T = int(input())
cases = [ int(sys.stdin.readline().strip()) for _ in range(T)]

def calculate(money):
    quarter, dime, nickel, penny = [0 for _ in range(4)]
    if money > 0:
        if money >= 5:
            if money >= 10:
                if money >= 25:
                    quarter += money // 25
                    money %= 25
                dime += money // 10
                money %= 10
            nickel += money // 5
            money %= 5
        penny += money // 1
    return [quarter, dime, nickel, penny]

for c in cases:
    print(' '.join(map(str,calculate(c))))
