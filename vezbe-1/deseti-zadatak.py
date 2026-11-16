def geomSredina(brojDecimala):
    x = int(input("Unesi cetvorocifren broj: "))

    h = x // 1000
    s = ( x // 100 ) % 10
    d = ( x // 10 ) % 10
    j = x % 10

    return round((h*s*d*j)**(1/4), brojDecimala)