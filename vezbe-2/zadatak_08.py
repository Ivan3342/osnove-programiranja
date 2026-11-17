import random

n, m, k = map(int,input().split())

while True:
    z = random.randint(n, m)
    if z % k == 0:
        print(z)
        break