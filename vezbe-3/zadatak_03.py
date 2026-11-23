def najveci(n):
    najveci = n[0]
    for broj in n:
        if broj > najveci:
            najveci = broj

    return najveci