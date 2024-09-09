
a = int(input("Значение А:"))
b = int(input("Значение B:"))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)