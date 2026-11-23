def suma_parnih(n):
    suma = 0
    for broj in n:
        if broj % 2 == 0:
            suma += broj

    return suma