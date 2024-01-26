import random

numere = [random.randint(1,49) for i in range(6)]
print(numere)
numere_alese = [int(input("Introduceti un numar intre 1 si 49:\n")) for i in range(6)]
nr_ghicite = [nr for nr in numere_alese if nr in numere]

print(nr_ghicite)

print("Categoria:", 7 - len(nr_ghicite) if len(nr_ghicite) >= 3 else 0)

print(all([nr in range(1, 50) for nr in numere]))
print(all([nr in range(1, 50) for nr in numere_alese]))

# Verificam daca elementele sunt unice
print(len(set(numere)) == len(numere))
print(len(set(numere_alese)) == len(numere_alese))




