
def menu_de_cafeteria():
    print("bienvenido a la cafeteria desordenada que desea ordenar?")
    print("1. cafe")
    print("2. te")
    print("3. jugo")
    print("4. pastel")
    opcion = int(input("ingrese el numero de su orden: "))

    if opcion == 1:
        print("usted ha ordenado un cafe")

    elif opcion == 2:
        print("usted ha ordenado un te")
    elif opcion == 3:
        print("ustedd ha ordenado un jugo")
    elif opcion == 4:
        print("usted ha ordenado un pastel")
    
    menu_de_cafeteria()

menu_de_cafeteria()

def mostrar_menu():
    print("bienvenidos a la cafeteria")
    print("1. cafe - 2k")
    print("2. postre del dia - 5k")
    print("3. agua  - 1k")
    print("4. brownie  - 6k")
    print("5. finalizar compra")



mostrar_menu()
