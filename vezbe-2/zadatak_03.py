def obrni_poslednje_cifre():
    n = int(input())

    prefiks = n // 10000
    cifra_hiljada = ( n//1000 ) % 10
    cifra_stotina = ( n//100 ) % 10
    cifra_desetica = ( n // 10 ) % 10
    cifra_jedinica = n % 10

    return prefiks * 10000 + cifra_jedinica * 1000 + cifra_desetica * 100 + cifra_stotina * 10 + cifra_hiljada