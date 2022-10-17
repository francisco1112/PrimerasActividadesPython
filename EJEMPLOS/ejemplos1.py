'''
Created on Oct 11, 2022

@author: estudiante
'''
"""8. Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”"""
numero = int(input("Ingrese un número: "))
peque = numero
pregunta = input("¿Desea ingresar más números (S/N)? ")
while pregunta.upper()=="S":
    numero = int(input("Ingrese otro número: "))
    if numero < peque:
        peque = numero
    pregunta = input("¿Desea ingresar más números (S/N)? ")
print(f"El número menor es {peque}")
