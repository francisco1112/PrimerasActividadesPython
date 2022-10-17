"""1.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""

"""2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""

"""3. Calcular la media de tres números pedidos por teclado"""
numero1 = int(input("Un número: "))
numero2 = int(input("Otro número: "))
numero3 = int(input("Otro número: "))

media = (numero1 + numero2 + numero3) /3
print(media)

"""4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra"""

totalcompra = int(input("Total de compra: "))
print(15*totalcompra/100)

"""5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""
numero1 = int(input("Un número: "))
numero2 = int(input("Otro número: "))
total = (numero1 - numero2) 
if total < 0:
    print(total*-1)
elif total >= 0:
    print(total)
    
"""6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos."""

"""7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?"""
num = int(input("Introduce un número: "))

"""8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos)."""
dinero = int(input("Introduce una cantidad: "))



"""9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:"""
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
if exponente > 0:
    print(base*exponente)
elif exponente == 0:
    print("1")
elif exponente < 0:
    print(1/base*exponente*-1)
    
"""10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:"""

A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if A != B and A != C and B != C and B != A and C != A and C != B:
    print("Triángulo rectángulo")
elif A == B and A != C and B != C or A == C and A != B and C != B or B == C and C != A and B != A:
    print("Isósceles")
elif A == B and A == C and B == C and C == A and C == B and B == A and B == C:
    print("Equilátero")
else:
    print("Escaleno")
    
"""11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400."""
año = int(input("Año: "))



"""8.
2€ = 3
1€ = 4
0.50€ = 2
0.20€ = 5
0.10€ = 6
0.05€ = 3
0.02€ = 5
0.01€ = 15
Tiene que aparecer por pantalla los euros y los centimos.
Si queremos que nos muestre los centimos,si por ejemplo tenemos 105,53€, al restarlo por los euros solamente, en esta caso seria restarlo con 105€, nos daría los céntimos.
"""



"""Investigar el TRUNC y el ROOM"""
"""tenemos 15 min, 
5 min * 1€
3 min * 0.8€
2 min * 0.7€
5 min * 0.5€"""

