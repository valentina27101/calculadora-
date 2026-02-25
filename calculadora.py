def sum (a, b):
    return a + b

def rest (a, b):
    return a - b

def mult (a, b):
    return a * b

def div (a, b):
    if b == 0:
        return "error: division por cero"
    return a / b 

def poten (a, b):
    return a ** b 

def raiz (a, b):
    if b == 0:
        return "error: raiz por cero"
    return a ** (1/b)

def porcen (a, b):
    return (a * b) / 100

def promedio (a, b):
    return (a + b) / 2

def modulo (a, b):
    if b == 0:
        return "error: modulo por cero"
    return a % b

print("bienvenido a la calculadora")

operaciones = int(input("cuantas operaciones deseas realizar? "))

for i in range(operaciones):
    print("operaciones")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potencia")
    print("6. raiz")
    print("7. porcentaje")
    print("8. promedio")
    print("9. modulo")

    opcion = int(input("selecciona una opcion:"))
    a = float(input("ingresa el primer numero: "))
    b = float(input("ingresa el segundo numero: ")) 
    
    if opcion == 1:
        print("resultado:", sum(a, b))
    elif opcion == 2:
        print("resultado:", rest(a, b))
    elif opcion == 3:
        print("resultado:", mult(a, b))
    elif opcion == 4:
        print("resultado:", div(a, b))
    elif opcion == 5:
        print("resultado:", poten(a, b))
    elif opcion == 6:
        print("resultado:", raiz(a, b))
    elif opcion == 7:
        print("resultado:", porcen(a, b))
    elif opcion == 8:
        print("resultado:", promedio(a, b))
    elif opcion == 9:
        print("resultado:", modulo(a, b))
    else: 
        print("opcion invalida.")
        print("gracias por usar nuestra calculadora.")

