'''
Created on Oct 13, 2022

@author: estudiante
'''
"""17. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""
num1 = int(input("Inserte un numero: "))
num2 = int(input("Inserte otro numero: "))
for i in range(num1,num2,2):
    print(i)
    
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


"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

potencia = 1
for i in range(exponente):
    potencia *=base
print("La potencia es:", potencia)

"""20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses."""

pago = 10   
suma = pago

print(f"El pago del mes 1 es {pago}")
for i in range (2, 21):
   
    pago*=2
    print(f"El pago del mes {i} es {pago}")
    suma+=pago
       
print(f"El total es {suma}€")  








