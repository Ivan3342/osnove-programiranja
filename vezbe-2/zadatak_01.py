def zbir_cifara():
    broj = int(input("Unesi cetvorocifreni broj: "))

    h = broj // 1000
    s = ( broj // 100 ) % 10
    d = ( broj // 10 ) % 10
    j = broj % 10

    return (h+s+d+j)

print(zbir_cifara())