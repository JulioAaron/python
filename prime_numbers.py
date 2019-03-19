n = int(input("Ingrese el número límite: "))

for num in range(n + 1):
   # los números primos son mayores que 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
