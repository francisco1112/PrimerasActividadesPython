"""1. Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages."""
numero = int(input("Inserte un número: "))
while not(numero >= 1 and numero <= 100):
    numero = int(input("Inserte un número entre el 1 y el 100 por favor: "))
for i in range(numero):
    numero = int(input("Inserte un número: "))
    

"""7. Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
        “How many numbers do you want input?” to ask for the number of numbers.
        “Enter one number greater than 0:” to ask for a number.
        “The number is not valid, it should be greater than 0” to inform that the number is not
        valid.
        “The medium is XX.XX” to show the result."""
cantidad = int(input("How many numbers do you want input? "))

while cantidad <= 0:
    cantidad = int(input("How many numbers do you want input? "))
total, contador = 0, 0

while cantidad > contador:
    numero = int(input("Enter one number greater than 0: "))
    while numero <= 0:
        numero = int(input("The number is not valid, it should be greater than 0"))
    contador +=1
    total += numero
print(f"The medium is {total/cantidad}")

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






"""10. Design a program that reads an integer positive number and says the “factorial” of
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX”"""
total = 1 
numero = int(input("Ingrese un número: "))
while numero < 0:
    numero = int(input("El número no es válido, inténtalo de nuevo: "))
for i in range(1, numero+1):
    total *=i
   
print(f"El factorial es: {i}")


"""numero = int(input("Ingrese un número: "))
while numero < 0:
    numero = int(input("El número no es válido, inténtalo de nuevo: "))
factorial = 1 
factorial = factorial * numero
numero = numero - 1 
    print(factorial)"""

