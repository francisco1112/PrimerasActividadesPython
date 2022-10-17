print ("Hola Mundo")

""" comentarios en ECLIPSE de varias lineas """

print("3+15", type("3+15"))
print(str(3+15), type(str(3+15)))
print(3+15, type(3+15))
print("-----")

"""restar"""

print(15-3) 

"""dividir sin decimal"""

print(15//3) 

"""elevar a"""

print(33**2) 

"""modulo, seria la division, el resto"""

print(19//5, 19%5)

"""dividir con decimal"""

print(3/2)

"""si ponemos decimales en una operacion, nos calcula tambien en decimales"""

print(3.01*2)

"""sigue las reglas matemáticas"""

print(3-2*5)

"""2. Calcular el valor de las siguientes expresiones aritméticas:"""
print(27%4+15/4, type(27%4+15/4))
print(37/4**2-2, type(37/4**2-2))
print(9*2/3*10*3, type(9*2/3*10*3))
print((7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))

"""5"""
a, b=True, True

print(a or not(b))

a, b=True, False

print(a or not(b))
a, b=False, True

print(a or not(b))
a, b=False, False

print(a or not(b))
