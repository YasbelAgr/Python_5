
n1= int(input("Ingresa un numero: "))
n2= int(input("Ingresa un numero: "))
n3= int(input("Ingresa un numero: "))
if n1 > 50 and n2 > 50 and n3 > 50:
    print("Todos los numeros son altos")
elif n1 > n2 and n1 > n3:
    print("El numero mayor es ",n1)
elif n2 > n1 and n2 > n3:
    print("El numero mayor es ",n2)
elif n3 > n1 and n3 > n2:
    print("El numero mayor es ",n3)
    