def niz_parnih(n):
    parni = []
    for broj in n:
        if broj % 2 == 0:
            parni.append(broj)

    return parni