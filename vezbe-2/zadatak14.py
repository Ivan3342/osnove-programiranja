def kvadriraj(x):
    odgovor = 0
    ponavljanja = abs(int(x))

    while ponavljanja > 0:
        odgovor += abs(x)
        ponavljanja = ponavljanja - 1

    return odgovor

broj = int(input("Unesi broj koji zelis da kvadriras: "))
print(kvadriraj(broj))