#Calcular la n-esima potencia de x con ciclos repetitivos

x = int(input("Ingrese un numero:"))
exp = int(input("Ingrese su exponente:"))
producto = x

for i in range(exp-1):
    print(x, producto, i)
    producto = producto*x

print("%s^%s = %s" % (x, exp, producto))
print("Comprobacion", x**exp)
