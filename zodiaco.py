
# Signos del Zodiaco, implementación en python para conocer el signo zodiacal con base en al mes y día de nacimiento
# Algoritmos selectivos

'''Signo	Fechas	Astro	Elemento	India	China
Aries	21 de marzo - 20 de abril	Marte / Plutón	Fuego	Tejas (fuego)	Dragón (5)	5.°
Tauro	21 de abril 20 de mayo	Venus / Tierra	Tierra	Prithivi (tierra)	Serpiente (6)	2.°
Géminis	21 de mayo - 21 de junio	Mercurio	Aire	Vayu (aire)	Caballo (7)	3.°
Cáncer	22 de junio - 22 de julio	Luna	Agua	Jala (agua)	Serpiente (8)	1.°
Leo	23 de julio - 23 de agosto	Sol	Fuego	Tejas	Mono (9)
Virgo	24 de agosto - 23 de septiembre	Mercurio	Tierra	Prithivi	Gallo (10)
Libra	24 de septiembre - 22 de octubre	Venus	Aire	Vayu	Perro (11)
Escorpio	23 de octubre - 22 de noviembre	Plutón / Marte	Agua	Jala	Cerdo (12)
Sagitario	23 de noviembre - 21 de diciembre	Júpiter	Fuego	Tejas	Rata (1)	8.°
Capricornio	22 de diciembre - 19 de enero	Saturno	Tierra	Prithivi	Buey (2)	8.°
Acuario	20 de enero - 19 de febrero	Urano / Saturno	Aire	Vayu	Tigre (3)	3.°
Piscis	20 de febrero - 20 de marzo	Neptuno / Júpiter	Agua	Jala	Conejo (4)	3.°
'''

#anio = int(input("Ingrese su año de nacimiento: "))
mes = input("Ingrese su mes de nacimiento:" )
dia = int(input("Ingrese su día de nacimiento: "))

if (mes=='marzo' or mes=='abril'):
    if (dia>=1 and dia<=21):
        print("Signo: Aries \nFechas: 21 de marzo - 20 de abril \nAstro: Marte/Plutón \nElemento: Fuego	\nIndia: Tejas (fuego) \nChina: Dragón (5)	\nGrado: 5.°")
    elif (dia>=22 and dia<=30):
        print("Signo: Tauro	\nFechas: 21 de abril - 20 de mayo	\nAstro: Venus / Tierra	\nElemento: Tierra	\nIndia: Prithivi (tierra)	\nChina: Serpiente (6) \nGrado: 2.°")
elif (mes=='mayo'):
    if (dia>=1 and dia<=20):
        print("Signo: Tauro	\nFechas: 21 de abril - 20 de mayo	\nAstro: Venus / Tierra	\nElemento: Tierra	\nIndia: Prithivi (tierra) \nChina: Serpiente (6) \nGrado: 2.°")
    elif (dia>=21 and dia<=31):
        print("Signo: Géminis \nFechas: 21 de mayo - 21 de junio	\nAstro: Mercurio	\nElemento: Aire	\nIndia: Vayu (aire)	\nChina: Caballo (7) \nGrado: 3.°")
elif (mes=='junio'):
    if (dia>=1 and dia<=21):
        print("Signo: Géminis \nFechas: 21 de mayo - 21 de junio	\nAstro: Mercurio	\nElemento: Aire	\nIndia: Vayu (aire)	\nChina: Caballo (7) \nGrado: 3.°")
    elif(dia>21 and dia <=30):
        print("Signo: Cáncer \nFechas: 22 de junio - 22 de julio	\nAstro: Luna \nElemento: Agua	\nIndia: Jala (agua)	\nChina: Serpiente (8)	\nGrado:  1.°")
elif (mes=='julio'):
    if (dia>=1 and dia <=22):
        print("Signo: Cáncer \nFechas: 22 de junio - 22 de julio	\nAstro: Luna \nElemento: Agua	\nIndia: Jala (agua)	\nChina: Serpiente (8)	\nGrado:  1.°")
    elif (dia>22 and dia <=31):
        print("Signo: Leo	\nFechas: 23 de julio - 23 de agosto	\nAstro:  Sol \nElemento: Fuego	\nIndia: Tejas	\nChina: Mono (9) ")
elif (mes=='agosto'):
    if (dia>=1 and dia <=23):
        print("Signo: Leo	\nFechas: 23 de julio - 23 de agosto	\nAstro:  Sol \nElemento: Fuego	\nIndia: Tejas	\nChina: Mono (9) ")
    elif (dia>23 and dia <=31):
        print("Signo: Virgo	\nFechas: 24 de agosto - 23 de septiembre \nAstro: 	Mercurio	\nElemento: Tierra	\nIndia: Prithivi \nChina: Gallo (10) ")
elif (mes=='septiembre'):
    if (dia>=1 and dia <=23):
        print("Signo: Virgo	\nFechas: 24 de agosto - 23 de septiembre	\nAstro: Mercurio	\nElemento: Tierra	\nIndia: Prithivi \nChina: Gallo (10)")
    elif(dia>23 and dia <=30):
        print("Signo: Libra	\nFechas: 24 de septiembre - 22 de octubre \nAstro:	Venus \nElemento: Aire	\nIndia: Vayu \nChina: Gallo Perro (11)")
elif (mes =='octubre'):
    if (dia>=1 and dia <=23):
        print("Signo: Libra	\nFechas: 24 de septiembre - 22 de octubre \nAstro:	Venus \nElemento: Aire	\nIndia: Vayu \nChina: Gallo Perro (11)")
    elif(dia>23 and dia <=31):
        print("Signo: Escorpio \nFechas: 23 de octubre - 22 de noviembre \nAstro: Plutón / Marte \nElemento: Agua \nIndia: Jala	\nChina: Cerdo (12)")
elif (mes=='noviembre'):
    if (dia>=1 and dia <=22):
        print("Signo: Escorpio \nFechas: 23 de octubre - 22 de noviembre \nAstro: Plutón / Marte \nElemento: Agua \nIndia: Jala	\nChina: Cerdo (12)")
    elif(dia>22 and dia <=30):
        print("Signo: Sagitario	\nFechas: 23 de noviembre - 21 de diciembre	\nAstro: Júpiter \nElemento: Fuego	\nIndia:  Tejas	\nChina: Rata (1) \nGrado:  8.°")
elif (mes=='diciembre'):
    if (dia>=1 and dia <=23):
        print("Signo: Sagitario	\nFechas: 23 de noviembre - 21 de diciembre	\nAstro: Júpiter \nElemento: Fuego	\nIndia:  Tejas	\nChina: Rata (1) \nGrado:  8.°")
    elif(dia>23 and dia <=31):
        print("Signo: Capricornio \nFechas: 22 de diciembre - 19 de enero \nAstro: Saturno \nElemento: Tierra 	\nIndia: Prithivi	\nChina: Buey (2) \nGrado: 8.°")
elif (mes=='enero'):
    if (dia>=1 and dia <=19):
        print("Signo: Capricornio \nFechas: 22 de diciembre - 19 de enero \nAstro: Saturno \nElemento: Tierra 	\nIndia: Prithivi	\nChina: Buey (2) \nGrado: 8.°")
    elif(dia>23 and dia <=31):
        print("Signo: Acuario \nFechas: 20 de enero - 19 de febrero	\nAstro: Urano / Saturno \nElemento: Aire 	\nIndia: Vayu \nChina: Tigre (3) \nGrado: 3.°")
elif (mes=='febrero'):
    if (dia>=1 and dia <=19):
        print("Signo: Acuario \nFechas: 20 de enero - 19 de febrero	\nAstro: Urano / Saturno \nElemento: Aire 	\nIndia: Vayu \nChina: Tigre (3) \nGrado: 3.°")
    elif(dia>19 and dia <=29):
        print("Signo: Piscis \nFechas:  20 de febrero - 20 de marzo	\nAstro:  Neptuno / Júpiter	 \nElemento: Agua \nIndia Jala \nChina:	Conejo (4) \nGrado:	3.°")
else:
    print("Por favor, revise sus datos e intente de nuevo")
