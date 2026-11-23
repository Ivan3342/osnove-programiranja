def broj_suglasnika(rec):
    brojac = 0
    for slovo in rec:
        if slovo not in ("A", "E", "I", "O", "U") and slovo.isupper():
            brojac += 1
    return brojac

print(broj_suglasnika("Crnac"))