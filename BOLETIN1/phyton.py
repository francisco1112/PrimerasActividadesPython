"""1. Calcular el resultado de las siguientes expresiones lógicas:"""
"""from future.backports.test.pystone import TRUE"""
print(7>=27 and not (7<=2))
print(24>5 and 10<=10 or 10==5)
print((10>=15 or 23==13) and not(8==8))
print (not (6/3>3) or 7>7)
#a)false
#b)true
#c)false
#d)true
"""2. Calcular el valor de las siguientes expresiones aritméticas:"""
print(27%4+15/4, type(27%4+15/4))
print(37/4**2-2, type(37/4**2-2))
print(9*2/3*10*3, type(9*2/3*10*3))
print((7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))

"""3. Escribir una expresión lógica que cumpla:"""

"""a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
euros pero igual o inferior a 420 euros."""


"""5"""
a, b=True, True
print(a or not(b))

a, b=True, False
print(a or not(b))

a, b=False, True
print(a or not(b))

a, b=False, False
print(a or not(b))

a, b=True, True
print(not(a and b)and(b or a))

a, b=True, False
print(not(a and b)and(b or a))

a, b=False, True
print(not(a and b)and(b or a))

a, b=False, False
print(not(a and b)and(b or a))

"""3"""
"""a"""
precio = 60
print(60 <= precio and precio<=420)

precio = 420
print(60 <= precio and precio<=420)
"""b"""
precio=21 
print(precio % 2==1)

precio=40
print(precio % 2==1)  
"""c"""
saldo=200
dineroSacar=100
print(dineroSacar <= saldo and saldo >= 0 and dineroSacar > 0)

"""d"""
hora=23
minutos=22
minutos=60
hora=24
print(hora>=0 and hora<=23 and minutos<=59 and minutos>=0)

"""e"""
#con el or
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='Ñ'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
#con el and
estadoCivil='D'
print(estadoCivil!= 'S' and estadoCivil!='C' and estadoCivil!='V' and estadoCivil!= 'D')

"""4. Escribir una expresión lógica que cumpla:"""
"""a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
es superior a 300 euros o negativa."""
"""a"""
cantidad = -1
print(not(cantidad<0 or cantidad>300)) 
cantidad = 0
print(not(cantidad<0 or cantidad>300)) 
cantidad = 200
print(not(cantidad<0 or cantidad>300)) 
      
"""d"""
numero= 21
print(not(numero%7==0 or numero%3==0))
numero=15
numero=14
numero=16
      
      
      
      
      