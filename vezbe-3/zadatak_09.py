def nzs(x, y):
    for i in range(max(x,y), x*y+1, max(x,y)):
        if i % x == 0 and i % y == 0:
            return i