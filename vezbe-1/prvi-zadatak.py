def dvaBroja(a, b):
    sum = a + b
    raz = a - b
    pro = a * b
    kol = a // b
    ost = a % b

    print(f"Zbir: {sum}\nRazlika: {raz}\nProizvod: {pro}\nKolicnik: {kol}\nDeljenje sa ostatkom: {ost}")

x = int(input("Unesi prvi broj: "))
y = int(input("Unesi drugi broj: "))

dvaBroja(x, y)