def n_faktorijel(n):
    faktorijel = 1
    i = 1
    while i < n+1:
        faktorijel *= i
        i += 1 

    return faktorijel

print(n_faktorijel(6))
