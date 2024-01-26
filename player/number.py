import random

numere = [random.randint(1,49) for i in range(6)]
print(numere)

numar_ales = int(input("Introduceti un numar intre 1 si 49:\n"))
print("Ai ghicit!") if numar_ales in numere else print("Nu ai ghicit!")

