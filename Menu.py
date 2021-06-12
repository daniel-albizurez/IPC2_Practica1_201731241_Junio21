import lista_doblemente_enlazada
import os
option = 1
agenda = lista_doblemente_enlazada.Lista()

def nuevoContacto():
        nombre = input("Ingrese el nombre del contacto ")
        apellido = input("Ingrese el apellido del contacto ")
        numero = input("Ingrese el numero telefonico del contacto ")
        if agenda.buscar(numero) != None:
            print("Contacto ya existente")
            return
        agenda.save(nombre, apellido, numero)
        if agenda.buscar(numero) != None:
            print("Agregado exitosamente")


while option != "4":
    print("Elija una opcion")
    options = ["Ingresar nuevo contacto", "Buscar contacto", "Visualizar agenda", "Salir"]
    cont = 1
    for option in options:
        print(str(cont) + '. ' + option)
        cont+=1
    option = input("\nIngrese el numeral de la opcion que desea ejecutar ")
    if option == "1":
        nuevoContacto()
    elif option == "2":
        numero = input("Ingrese el numero telefonico del contacto ")
        contacto = agenda.buscar(numero)
        if contacto == None:
            print("Contacto no existente")
            agregar = input("¿Desea agregarlo? Y/N ")
            if agregar == "Y":
                nuevoContacto()
    elif option == "3":
        f = open("agenda.dot", "w")
        f.write(agenda.generarDot())
        f.close()

        os.system("dot -Tjpg agenda.dot -o agenda.png")
        os.startfile("agenda.png")
    elif option == "4":
        pass
    else:
        print("Opcion invalida, vuelva a intentarlo")