def cnvrt_bool():
    str_input = input("Unesi vrednost: ")
    if str_input.lower() == "tacno":
        return True
    elif str_input.lower() == "netacno":
        return False
    else:
        return "Pogresan unos!"

print(cnvrt_bool())