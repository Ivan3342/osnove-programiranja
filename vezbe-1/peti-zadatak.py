from math import pi, sqrt

def obimKrugaPovrsina(povrsina):
    poluprecnik = sqrt(povrsina/pi)
    obim = 2*poluprecnik*pi

    return round(obim, 3)