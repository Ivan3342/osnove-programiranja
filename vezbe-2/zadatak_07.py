def deljivost_dva_tri():
    n = int(input("Unesi broj: "))

    if n % 2 == 0 and n % 3 == 0:
        print("Broj je deljiv sa i 2 i 3.")
    elif n % 2 == 0 and n % 3 != 0:
        print("Broj je deljiv sa 2, ali nije deljiv sa 3.")
    elif n % 2 != 0 and n % 3 == 0:
        print("Broj nije deljiv sa 2, ali je deljiv sa 3.")
    else:
        print("Broj nije deljiv ni sa 2, ni sa 3.")