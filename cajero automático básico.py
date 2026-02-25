saldo = 1000

print ("bienvenido al cajero automatico")
operaciones = int(input("cuantas operaciones deseas realizar?"))

for i in range(operaciones):
    print("operaciones")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")

    opcion = int(input("selecciona una opcion : "))

    if opcion == 1:
        print("su saldo actual es: $", saldo)

    elif opcion == 2:
        retiro = float(input("ingrese la cantidad: $"))
        
        while retiro < 0:
            saldo = float(input("saldo invalido. ingresa un saldo positivo: "))
            if retiro > saldo: 
                print("fondos insuficientes. ")
                continue
            
        saldo -= retiro
        print("retiro exitoso. nuevo saldo:", saldo)
        break
    elif opcion == 3:
        retiro = float(input("ingresa el monto a depositar: "))

        while saldo < 0:
            retiro = float(input("saldo invalido. ingresa un saldo positivo: "))

        saldo += retiro 
        print("deposito exitoso. muestra el nuevo saldo: ")

    else: 
        print("opcion invaalida.")


print("gracias por usar nuestro servicio.")
