def palindrome():
    x = input('Unesi nisku: ')

    if x.lower() == x[::-1].lower():
        print("Niska je palindrom.")
    else:
        print("Niska nije palindrom.")

palindrome()