mylista = [673,958,997,1129,1190,1226,1246,1381,1441,1528,1541,1555,1628]
 
promedio = sum(mylista)/len(mylista)
suma = 0

for item in mylista:
    suma = suma + item**2

varianza = (suma/len(mylista))-(promedio**2)
desv =  varianza**0.5

print("%0.2f" % varianza)
print("%0.2f" % desv)

