#Ingrese su mes y día de nacimiento y obtenga su signo zodiacal, astro y más
#Una implementacón con listas, diccionarios, ciclos, if

data =[
      {"signo":"Aries",   "mes":"marzo", "dia_inicio": 21, "dia_fin": 30, "astro": "Marte / Plutón", "elemento":"Fuego",  "india":"Tejas (fuego)",     "china":"Dragón (5)",    "grado":"5.°" },
      {"signo":"Aries",   "mes":"abril", "dia_inicio": 1,  "dia_fin": 20, "astro": "Marte / Plutón", "elemento":"Fuego",  "india":"Tejas (fuego)",     "china":"Dragón (5)",    "grado":"5.°" },
      {"signo":"Tauro",   "mes":"abril", "dia_inicio": 21, "dia_fin": 31, "astro": "Venus / Tierra", "elemento":"Tierra", "india":"Prithivi (tierra)", "china":"Serpiente (6)", "grado":"2.°" },
      {"signo":"Tauro",   "mes":"mayo",  "dia_inicio": 1,  "dia_fin": 20, "astro": "Venus / Tierra", "elemento":"Tierra", "india":"Prithivi (tierra)", "china":"Serpiente (6)", "grado":"2.°" },
      {"signo":"Géminis", "mes":"mayo",  "dia_inicio": 21,  "dia_fin": 31, "astro": "Mercurio",      "elemento":"Aire",   "india":"Vayu (aire)",       "china":"Caballo (7)",   "grado":"3.°" },
      {"signo":"Géminis", "mes":"junio", "dia_inicio": 1,  "dia_fin": 21, "astro": "Mercurio",       "elemento":"Aire",   "india":"Vayu (aire)",       "china":"Caballo (7)",   "grado":"3.°" },
      {"signo":"Cáncer",  "mes":"junio",  "dia_inicio": 22,  "dia_fin": 30, "astro": "Luna",       "elemento":"Agua",      "india":"Jala (agua)",       "china":"Serpiente (8)",   "grado":"1.°" },
      {"signo":"Cáncer",  "mes":"julio",  "dia_inicio": 1,  "dia_fin": 22, "astro": "Luna",       "elemento":"Agua",      "india":"Jala (agua)",       "china":"Serpiente (8)",   "grado":"1.°" },
      {"signo":"Leo",     "mes":"julio",  "dia_inicio": 23,  "dia_fin": 31, "astro": "Sol",       "elemento":"Fuego",      "india":"Tejas",       "china":"Mono (9)",   "grado":"" },
      {"signo":"Leo",     "mes":"agosto",  "dia_inicio": 1,  "dia_fin": 23, "astro": "Sol",       "elemento":"Fuego",      "india":"Tejas",       "china":"Mono (9)",   "grado":"" },
      {"signo":"Virgo",   "mes":"agosto",  "dia_inicio": 24,  "dia_fin": 31, "astro": "Mercurio",       "elemento":"Tierra",      "india":"Prithivi",       "china":"Gallo (10)",   "grado":"" },
      {"signo":"Virgo",   "mes":"septiembre",  "dia_inicio": 1,  "dia_fin": 23, "astro": "Mercurio",       "elemento":"Tierra",      "india":"Prithivi",       "china":"Gallo (10)",   "grado":"" },
      {"signo":"Libra",   "mes":"septiembre",  "dia_inicio": 24,  "dia_fin": 30, "astro": "Venus",       "elemento":"Aire",      "india":"Vayu",       "china":"Perro (11)",   "grado":"" },
      {"signo":"Libra",   "mes":"octubre",  "dia_inicio": 1,  "dia_fin": 22, "astro": "Venus",       "elemento":"Aire",      "india":"Vayu",       "china":"Perro (11)",   "grado":"" },
      {"signo":"Escorpio", "mes":"octubre",  "dia_inicio": 23,  "dia_fin": 31, "astro": "Plutón / Marte",       "elemento":"Agua",      "india":"Jala",       "china":"Cerdo (12)",   "grado":"" },
      {"signo":"Escorpio", "mes":"noviembre",  "dia_inicio": 1,  "dia_fin": 22, "astro": "Plutón / Marte",       "elemento":"Agua",      "india":"Jala",       "china":"Cerdo (12)",   "grado":"" },
      {"signo":"Sagitario", "mes":"noviembre",  "dia_inicio": 23,  "dia_fin": 30, "astro": "Júpiter",       "elemento":"Fuego",      "india":"Tejas",       "china":"Rata (1)",   "grado":"8.°" },
      {"signo":"Sagitario", "mes":"diciembre",  "dia_inicio": 1,  "dia_fin": 21, "astro": "Júpiter",       "elemento":"Fuego",      "india":"Tejas",       "china":"Rata (1)",   "grado":"8.°" },
      {"signo":"Capricornio", "mes":"diciembre",  "dia_inicio": 22,  "dia_fin": 31, "astro": "Saturno",       "elemento":"Tierra",      "india":"Prithivi",       "china":"Buey (2)",   "grado":"8.°" },
      {"signo":"Capricornio", "mes":"enero",  "dia_inicio": 1,  "dia_fin": 19, "astro": "Saturno",       "elemento":"Tierra",      "india":"Prithivi",       "china":"Buey (2)",   "grado":"8.°" },
      {"signo":"Acuario", "mes":"enero",  "dia_inicio": 20,  "dia_fin": 31, "astro": "Urano / Saturno",       "elemento":"Aire",      "india":"Vayu",       "china":"Tigre (3)",   "grado":"3.°" },
      {"signo":"Acuario", "mes":"febrero",  "dia_inicio": 1,  "dia_fin": 19, "astro": "Urano / Saturno",       "elemento":"Aire",      "india":"Vayu",       "china":"Tigre (3)",   "grado":"3.°" },
      {"signo":"Picis", "mes":"febrero",  "dia_inicio": 20,  "dia_fin": 29, "astro": "Neptuno / Júpiter",       "elemento":"Agua",      "india":"Jala",       "china":"Conejo (4)",   "grado":"3.°" },
      {"signo":"Picis", "mes":"marzo",  "dia_inicio": 1,  "dia_fin": 20, "astro": "Neptuno / Júpiter",       "elemento":"Agua",      "india":"Jala",       "china":"Conejo (4)",   "grado":"3.°" },
      ]

mes=input("Ingrese su mes de nacimiento: ")
dia=int(input("Ingrese su día de nacimiento: "))
bandera = 0

for i in range(len(data)):
    if (data[i]["mes"]==mes) and (data[i]["dia_inicio"] <= dia <= data[i]["dia_fin"]):
        print("********************************************************")
        print("Signo: %s" % data[i]["signo"])
        print("Astro: %s" % data[i]["astro"])
        print("Elemento: %s" % data[i]["elemento"])
        print("India: %s" % data[i]["india"])
        print("China: %s" % data[i]["china"])
        print("Grado: %s" % data[i]["grado"])
        print("********************************************************")
        bandera = 1

if bandera == 0:
    print("Por favor, revise sus datos.")
