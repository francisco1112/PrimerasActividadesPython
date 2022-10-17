print("Bienvenido a Jacafitness!!")
hora = int(input("Inserte una hora: "))
minutos = int(input("Inserte los minutos: "))
dia = str(input("Inserte un dia: ")).upper()
if (dia == "LUNES" or dia == "MIERCOLES" or dia == "VIERNES") and hora >= 12 and minutos >= 00 and hora <= 14 and minutos <=59:
    print("Spinning")
elif (dia == "LUNES" or dia == "MIERCOLES" or dia == "VIERNES") and hora >= 16 and minutos >= 00 and hora < 20 and minutos <=59:
    print("Yoga")
elif (dia == "LUNES" or dia == "MIERCOLES" or dia == "VIERNES") and hora >= 20 and minutos >= 00  and hora <= 22 and minutos <=59:
    print("Body Combat")
elif (dia == "MARTES" or dia == "JUEVES") and hora >= 12 and minutos >= 00 and hora <= 14 and minutos <=59:
    print("Yoga")
elif (dia == "MARTES" or dia == "JUEVES") and hora >= 16 and minutos >= 00 and hora <= 20 and minutos <=59:
    print("Spinning")
else:
    print("No hay actividad")
    

print("CORREGIDO")
print(print("Bienvenido a Jacafitness!!"))
dia = str(input("Inserte un dia: ")).upper()
hora = int(input("Inserte una hora: "))
if dia == "LUNES" or dia == "MIERCOLES" or dia == "VIERNES":
    if hora >= 12 and hora <= 14:
        print("Spinning")   
    if hora >= 16 and hora < 20:
        print("Yoga")
    if hora >= 20 and hora <= 22:
        print("Body Combat")
    else:
        print("No hay actividad")
        
elif dia == "MARTES" or dia == "JUEVES":
    if hora >= 12 and hora <= 14:
        print("Yoga")
    if hora >= 16 and hora <= 20:
        print("Spinning")
    else:
        print("No hay actividad")

else:
    print("No hay actividad")
    


    