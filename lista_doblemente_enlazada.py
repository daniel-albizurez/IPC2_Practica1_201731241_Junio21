class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido + " " + self.telefono

class Nodo:
    def __init__(self, nombre, apellido, telefono):
        self.anterior = None 
        self.siguiente = None
        self.contacto = Contacto(nombre, apellido, telefono)

    def imprimir(self):
        print(self.contacto)

class Lista:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0 

    def save(self, nombre, apellido, numero):
        temp = Nodo(nombre, apellido, numero)
        nombre = nombre.lower()
        apellido = apellido.lower()
        if self.first == None:
            self.first = temp
            self.last = temp
        else:
            aux = self.first
            while aux != None:
                apellidoAux = aux.contacto.apellido.lower()
                if apellidoAux < apellido:
                    if aux.siguiente == None:
                        self.insertar(aux, temp)
                        break
                    else:
                        aux = aux.siguiente
                elif apellidoAux == apellido:
                    nombreAux = aux.contacto.nombre.lower()
                    if nombreAux < nombre:
                        aux = aux.siguiente
                    elif nombreAux >= nombre:
                        self.insertar(aux.anterior, temp)
                        break
                elif apellidoAux > apellido:
                    self.insertar(aux.anterior, temp)
                    break
        while self.first.anterior != None:
            self.first = self.first.anterior
        while self.last.siguiente != None:
            self.last = self.last.siguiente
        self.count += 1

    def insertar(self, anterior, nuevo):
        if  anterior != None:
            if anterior.siguiente != None:
                anterior.siguiente.anterior = nuevo
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
        else:
            nuevo.siguiente = self.first
            self.first.anterior = nuevo
        
    def buscar(self, telefono):
        temp = self.first
        while temp != None:
            if temp.contacto.telefono == telefono:
                return temp.contacto
            temp = temp.siguiente
        return None
                
    def imprimir(self):
        temp = self.first
        cont = 0
        while cont < self.count and temp!= None:
            temp.imprimir()
            temp = temp.siguiente
            cont += 1

    def generarDot(self):
        temp = self.first
        estructura = "digraph { node [shape = box]"
        while temp != None:
            estructura += "\n" + temp.contacto.telefono + " [label=\"" +  temp.contacto.__str__().replace(" ", "\n") + "\"]\n"
            if temp != self.first:
                estructura += temp.contacto.telefono + "->" + temp.anterior.contacto.telefono + "\n"
            if temp != self.last:
                estructura += temp.contacto.telefono + "->" + temp.siguiente.contacto.telefono + "\n" 
            temp = temp.siguiente

        estructura += "}"
        return estructura
