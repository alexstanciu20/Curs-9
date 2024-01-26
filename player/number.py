import random

numere = [random.randint(1,49) for i in range(6)]
print(numere)
numere_alese = [int(input("Introduceti un numar intre 1 si 49:\n")) for i in range(6)]
nr_ghicite = [nr for nr in numere_alese if nr in numere]

print(nr_ghicite)

categorii = {
    6 : 1,
    5 : 2,
    4 : 3,
    3 : 4
}

print("Categoria: ", categorii[len(nr_ghicite)] if len(nr_ghicite) in categorii else 0)
print("Categoria: ", categorii.get(len(nr_ghicite), 0))
