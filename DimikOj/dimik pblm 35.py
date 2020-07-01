from math import sqrt,pow 

for _ in range(int(input())):

    x1,y1 = map(float,input().split())
    r = float(input())
    x2,y2 = map(float,input().split())
    
    result = sqrt (pow((x2-x1),2) + pow((y2-y1),2) )

    if result > r:
        print('The point is not inside the circle')
    else:
        print('The point is inside the circle')
