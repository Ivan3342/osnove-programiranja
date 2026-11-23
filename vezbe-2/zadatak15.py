def factorial(x):
    fac = 1
    for i in range(x):
        fac *= i+1
    return fac

broj = int(input("Unesi broj: "))
print(factorial(broj))