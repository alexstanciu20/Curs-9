import random

numere = [random.randint(1,49) for i in range(6)]
numere_alese = [int(input("Introduceti un numar intre 1 si 49:\n")) for i in range(6)]
nr_ghicite = [nr for nr in numere_alese if nr in numere]

print(numere)
print(nr_ghicite)

categorii = {
    6 : "Categoria 1",
    5 : "Categoria 2",
    4 : "Categoria 3",
    3 : "Categoria 4"
}

print(categorii[len(nr_ghicite)])
