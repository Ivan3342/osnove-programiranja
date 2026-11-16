def srCifara():
    cifre = str(input("Unesi cetvorocifren broj: "))
    if len(cifre) != 4:
        print("Nije cetvorocifren broj!")
        return 1
    zbir = int(cifre[0]) + int(cifre[1]) + int(cifre[2]) + int(cifre[3])

    return zbir/4
