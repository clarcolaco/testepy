numero1 = int(input("Coloque aqui o numero para tabuada:  "))
vezes = 1

for vezes in range (1,11):
    resultado = numero1 * vezes
    print("{} x {} = {}".format(numero1, vezes, resultado))
    vezes = vezes + 1
print("Acabou, obrigada!")
