import lista_doblemente_enlazada
import os
option = 1
agenda = lista_doblemente_enlazada.Lista()
while option != "4":
    print("Elija una opcion")
    options = ["Ingresar nuevo contacto", "Buscar contacto", "Visualizar agenda", "Salir"]
    cont = 1
    for option in options:
        print(str(cont) + '. ' + option)
        cont+=1
    option = input("\nIngrese el numeral de la opcion que desea ejecutar ")
    if option == "1":
        nombre = input("Ingrese el nombre del contacto ")
        apellido = input("Ingrese el apellido del contacto ")
        numero = input("Ingrese el numero telefonico del contacto ")
        agenda.save(nombre, apellido, numero)
    elif option == "2":
        numero = input("Ingrese el numero telefonico del contacto ")
        contacto = agenda.buscar(numero)
        print(contacto)
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