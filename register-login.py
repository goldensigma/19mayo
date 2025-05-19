n = int(input("Introduce numero: "))
x = int(input("Introduc segundo numero: "))

while True:
    opcion = int(input("Introduce que opcion de la calculadora deseas realizar:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n"))
    
    if opcion == 1:
        print(f"El resultado de la suma es: {n+x}")
    elif opcion == 2:
        print(f"El resultado de la resta es: {n-x}")
    elif opcion == 3:
        print(f"Eel resultado de la multiplicacion: {n*x}")
    elif opcion == 4:
        print(f"El resultado de la division con decimales es de: {n/x}")
    else:
        print("Error: 404")
        
