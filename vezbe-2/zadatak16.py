def minInt():
    x = input("Unesi ceo broj: ")
    najmanjaCifra = '9'
    n = len(x)

    while n > 0:
        if x[n-1] < najmanjaCifra:
            najmanjaCifra = x[n-1]

        n -= 1

    print(najmanjaCifra)

minInt()