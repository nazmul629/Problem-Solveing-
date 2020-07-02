
n = input()
l = len(n)-1

k = int(n) - (10**l) + 1

r = 9*l

while k:
    r += k % 10 
    k //= 10
print(r)