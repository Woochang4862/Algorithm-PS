a1, a2, a3, b1, b2, b3 = map(int, input().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if a1*x + a2*y == a3 and b1*x + b2*y == b3:
            print(x,y)
