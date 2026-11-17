def proveri_trougao():
    a = float(input("Unesi prvu stranicu: "))
    b = float(input("Unesi drugu stranicu: "))
    c = float(input("Unesi trecu stranicu: "))

    if a < ( b + c ) and b < ( a + c ) and c < ( a + b ):
        print("Trougao postoji.")
        return 0
    else:
        print("Trougao ne postoji.")
        return 1