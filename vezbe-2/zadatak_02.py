def izbaci_stotinu():
    n = int(input("Unesi broj: "))

    prefix = n // 1000
    sufix = n % 100

    print(prefix * 100 + sufix)
    return (prefix * 100 + sufix)