'''
Created on Oct 13, 2022

@author: estudiante
'''
"""3. Diseña un programa que pregunte cuántos números quiere introducir el usuario. Después,
el usuario tendría que introducir los números uno a uno y el programa debería
decir si cada uno de los números es par o impar. Si el usuario ingresa 0 o un negativo
número, no es válido, y el sistema debe pedir otro número. Los mensajes
son los siguientes:
"¿Cuántos números desea ingresar?" para pedir la cantidad de números.
“Ingrese un número mayor que 0:” para solicitar un número.
“El número no es válido, debe ser mayor a 0” para informar que el número no es
válido.
“El número XX es impar”
“El número XX es par”
"""
"""cantidad = int(input("¿Cuántos números desea introducir? "))
while cantidad <= 0:
    cantidad = int(input("El número no es válido, debe ser mayor a 0: "))
while cantidad > 0:
    numero = int(input("Introduce número: "))
    while numero <= 0:
        numero = int(input("El número no es válido, debe ser superior a 0: "))
    if numero%2 == 0:
        print(f"El número {numero} es par")
    elif numero%1 == 0:
        print(f"El número {numero} es impar")
    cantidad-=1"""
    
"""18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo."""
inferior = int(input("Límite inferior: "))
superior = int(input("Límite superior: "))
while inferior >= superior:
    inferior = int(input("El límite superior tiene que ser mayor al inferior: ")
numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))  

suma = 0
fuera = 0
igual = 0
while numero != 0:
    
    if inferior < numero < superior:
        suma+=numero
    elif numero < inferior or numero > superior:
        fuera+=1
    else:
        igual+=1
    numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))
        
print(f"La suma de los numeros dentro del intervalo es  {suma}, fuera del intervalo hay {fuera} numeros")
print(f"Existe {igual} numeros iguales al intervalo")
"""cantidad = int(input("¿Cuántos números desea introducir? "))
while cantidad <= 0:
    cantidad = int(input("ERROR¿Cuántos números desea introducir? "))
for i in range(cantidad):
    numero = int(input(""))
    
    while numero <= 0:
        numero = int(input(""))
        
    if numero%2==0:"""
        


