from math import sqrt, pow

def rastojanje(x1, y1, x2, y2):
    rastojanje = sqrt(pow((x1 - x2), 2) - pow((y1 - y2), 2))

    return round(rastojanje, 3)