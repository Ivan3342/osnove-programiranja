def najmanji(n):
    najmanji = n[0]
    for broj in n:
        if broj < najmanji:
            najmanji = broj

    return najmanji