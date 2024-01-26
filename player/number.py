import random

numere = [random.randint(1,49) for i in range(6)]
print(numere)

numar_ales = int(input("Introduceti un numar intre 1 si 49:\n"))

for nr in numere:
    if numar_ales == nr:
        print("Ai ghicit!")
        break
else:
    print("Nu ai ghicit!")

