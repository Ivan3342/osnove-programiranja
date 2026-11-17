def proveri_parnost():
    broj = int(input("Unesi broj: "))

    if broj % 2 == 0:
        print(f"Broj {broj} je paran.")
    else:
        print(f"Broj {broj} je neparan.")