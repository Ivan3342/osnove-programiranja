def proveri_trougao():
    a = float(input("Unesi prvu stranicu: "))
    b = float(input("Unesi drugu stranicu: "))
    c = float(input("Unesi trecu stranicu: "))

    if a < ( b + c ) and b < ( a + c ) and c < ( a + b ):
        print("Trougao postoji.")
    else:
        print("Trougao ne postoji.")