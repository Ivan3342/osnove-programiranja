n = abs(int(input("Unesite broj: ")))
s = 0

while n > 0:
    s += n % 10
    n = n // 10

print(s)