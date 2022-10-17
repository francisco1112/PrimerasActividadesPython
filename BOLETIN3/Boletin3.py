"""6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc."""
vocala=input("Dime una vocal: ")
if vocala=="A" or vocala=="a":
    print("Es la primera vocal a")
elif vocala == "e" or vocala == "i" or vocala == "o" or vocala == "u":
    print("Es vocal")
else:
    print("No es vocal")
vocalb=input("Dime una vocal: ")
if vocalb=="E" or vocalb=="e":
    print("Es la segunda vocal e") 
elif vocalb == "a" or vocalb == "i" or vocalb == "o" or vocalb == "u":
    print("Es vocal")
else:
    print("No es vocal")
vocalc=input("Dime una vocal: ")
if vocalc=="I" or vocalc=="i":
    print("Es la tercera vocal i")
elif vocalc == "e" or vocalc == "a" or vocalc == "o" or vocalc == "u":
    print("Es vocal")
else:
    print("No es vocal")
vocald=input("Dime una vocal: ")
if vocald=="O" or vocald=="o":
    print("Es la cuarta vocal o")
elif vocald == "e" or vocald == "i" or vocald == "a" or vocald == "u":
    print("Es vocal")
else:
    print("No es vocal")
vocale=input("Dime una vocal: ")
if vocale=="U" or vocale=="u":
    print("Es la quinta vocal u")
elif vocale == "e" or vocale == "i" or vocale == "o" or vocale == "a":
    print("Es vocal")
else:
    print("No es vocal")
    
"""7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:"""
estadocivil=input("estadocivil: ")
años=input("años: ")
precio=input("precio: ")
if estadocivil == "S" or estadocivil == "D" and años < 35:
    print(precio*12/100)
elif años > 50:
    print(precio*8.5/100)
elif estadocivil == "V" or estadocivil == "C" and años < 35:
    print(precio*11.3/100)
else:
    print(precio*10.5/100)
    
"""8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor."""
hora1, min1, seg1 = 0, 12, 59
hora2, min2, seg2 = 0, 20, 20
if hora1<hora2:
    print("la hora 1 es menor que la hora 2")
elif hora2 < hora1:
    print("la hora 2 es menor que la hora 1")
else:
    if min1 < min2:
        print("la hora 1 es menor que la hora 2")
    elif min1 > min2:
        print("la hora 2 es menor que la hora 1")
    else:
        if seg1 < seg2:
            print("la hora 1 es menor que la hora 2")
        elif seg1 > seg2:
            print("la hora 2 es menor que la hora 1")
        else:
            print("Las horas coinciden")
else:
    print("Los datos son incorrectos")



"""9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:"""

tipoproducto = insert("producto: ")
precio = insert("precio: ")
if tipoproducto == "A":
    print(precio*7/100)
elif tipoproducto == "C" or precio < 500:
    print(precio*12/100)
else:
    print(precio*9/100)
    
    
"""10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error"""

    


    






"""numero = 81
exponente = 2
print(numero**(1/exponente)) #raiz cuadrada
print(math.sqrt(numero))#raiz cuadrada
print(numero**exponente) #potencia
print(math.pow(numero, exponente)"""


"""numero = 81
print(numero**(1/2)) #raiz cuadrada
print(math.sqrt(numero))#raiz cuadrada
print(numero**2) #potencia
print(math.pow(numero, 2)"""


"""range(inicio, fin, incremento)
for variable in range(10):
    print(variable)"""
    
