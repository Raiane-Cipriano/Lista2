numero1 = float(input("diite um numero: "))
numero2 = float(input("digite outro numero: "))
numero3 = float(input("digite mais um numero: "))
if numero1 > numero2 > numero3:
    print(numero1, numero2, numero3)
elif numero1 > numero3 > numero2:
    print(numero1, numero3, numero2)
elif numero2 > numero1> numero3:
    print(numero2, numero1,numero3)
elif numero2 > numero3 > numero1:
    print(numero2, numero3, numero1)
elif numero3 > numero1 > numero2:
    print(numero3, numero1, numero2)
else:
    print(numero3, numero2, numero1)