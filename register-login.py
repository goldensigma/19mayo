import os

if not os.path.exists("historial.txt"):
    with open ("historial.txt", "w"):
        pass

n = int(input("Introduce numero: "))
x = int(input("Introduc segundo numero: "))
resultado = 0
while True:
    opcion = int(input("Introduce que opcion de la calculadora deseas realizar:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir decimalmente\n5.Salir\n"))
    
    if opcion == 1:
        print(f"El resultado de la suma es: {n+x}")
        with open ('historial.txt', 'a') as f:
            print(f"El resultado de la suma entre {n} y {x} es: {n+x}",file=f)
    elif opcion == 2:
        print(f"El resultado de la resta es: {n-x}")
        with open ('historial.txt', 'a') as f:
            print(f"El resultado de la resta entre {n} y {x} es: {n-x}",file=f)
    elif opcion == 3:
        print(f"Eel resultado de la multiplicacion: {n*x}")
        with open ('historial.txt', 'a') as f:
            print(f"El resultado de la multiplicar entre {n} y {x} es: {n*x}",file=f)
    elif opcion == 4:
        print(f"El resultado de la division con decimales es de: {n/x}")
        with open ('historial.txt', 'a') as f:
            print(f"El resultado de la division decimal entre {n} y {x} es: {n/x}",file=f)
    elif opcion == 5:
        print("Hasta luego")
        break
    else:
        print("Error: 404")
        

