for a in range(10, 20, 2):
    print(a)
    
print("***************")
    
for e in range(-10, 20, 4):
    print(e)
    
print("***************")
   
numero = int(input("Introduzca un numero: "))
for numero in range(0, numero*10+1, numero):
    print(numero)

print("**************")
a = 0
while a < 5:
    print(a)
    a+=1
    
print("***************")
    
introducirDatos = "S"
while introducirDatos == "S":
    
peso = int(input("¿Cual es tu peso?"))
while peso < 0:
    print("No son datos válidos")
altura = float(input("¿Cual es tu altura? Introduce un valor válido(> 0): "))


print(f"Tu indice de masa corporal es {peso/altura**2}")

while introducirDatos != "S" and introducirDatos != "N":
    print("No son datos válidos")

