print("Ingrese dos números para calcular su multiplicación con sumas susesivas")

base = int(input("Ingrese un numero:"))
repeticion = int(input("Ingrese otro numero:"))
resultado = base

for i in range(repeticion-1):
    print(resultado, repeticion, i)
    resultado =  resultado + base

print("Resultado %s x %s = %s " % (base, repeticion, resultado))
