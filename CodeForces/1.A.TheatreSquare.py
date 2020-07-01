import math
def theater(m,n,a):
    if m%a == 0:
        x1 = math.floor(m/a)
    else:
        x1 = math.floor(m/a+1)
    if n%a ==0:
        x2 = math.floor(n/a)
    else:
        x2 = math.floor(n/a+1)

    print(x1*x2)

m,n,a = map(int,input().split())
theater(m,n,a)
