#Muestra la sucesión de fibonacci hasta el número ingresado

n = int(input("Ingrese un número límite para mostrar los n términos de la sucesión de fibonacci: "))

a1, a2 = 0, 1

if n==a1:
    print(a1)
elif n==a2:
    print(a1)
    print(a2)
if n > 1:
    for i in range(2,n):
        fi=a1+a2
        a1 = a2
        a2 = fi
        print(fi)
