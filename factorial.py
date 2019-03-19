#Factorial de un número calculado con ciclo ascendente y descendente

n = int(input("Ingrese un numero para obtener su factorial! "))
fact=1
if n > 0:
    for i in range(n,0,-1):
        fact=fact*i
        print(fact)

print("********** el factorial de %s es %s **********" % (n, fact))

fact=n
if n > 0:
    for i in range(1,n,1):
        fact=fact*i
        print(fact)

print("********** el factorial de %s es %s **********" % (n, fact))
