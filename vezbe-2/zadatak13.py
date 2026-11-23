def ispisi_ocenu():
    bodovi = int(input("Unesi bodove: "))
    ocena = 0
    if bodovi >= 91:
        ocena = 10
    elif bodovi >= 81:
        ocena = 9
    elif bodovi >= 71:
        ocena=8
    elif bodovi >= 61:
        ocena = 7
    elif bodovi >= 51:
        ocena = 6
    else:
        print("Pali ste ispit! Ocena je manja od 6.")
        return 1

    print(ocena)

ispisi_ocenu()