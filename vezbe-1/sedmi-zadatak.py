from math import sqrt

def povTrougla(obim):
    stranica = obim / 3
    povrsina = (pow(stranica, 2) + sqrt(3)) / 4

    return round(povrsina, 3)