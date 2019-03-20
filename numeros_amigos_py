#Ingresar dos nùmeros para comprobar si son números amigos

sum_n1, sum_n2 = 0, 0

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

for i in range(1, n1):
    if n1%i==0:
        sum_n1+=i

for j in range(1, n2):
    if n2%j==0:
        sum_n2+=j

if sum_n1==n2 or sum_n2==n1:
    print("Los números %s y %s son amigos, porque sus divisores suman %s y %s" % (n1, n2, sum_n1, sum_n2))
else:
    print("Los números %s y %s NO son amigos, debido a la diferencia en la suma de sus divisores %s y %s respectivamente" % (n1, n2, sum_n1, sum_n2))
