class Persona:
    def __init__(self, nombre, infectado) -> None:
        self.nombre =  nombre
        self.infectado = infectado

class Nodo:

    def __init__(self, pos=0, valor=None) -> None:
        self.pos = pos
        self.valor = valor
        self.siguiente = None


class Lista:

    def __init__(self) -> None:
        self.size = 0
        self.raiz = None

    
    def insertar(self, valor):
        if(self.raiz==None):
            self.raiz = Nodo(self.size, valor)
        else:
            aux = self.raiz
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = Nodo(self.size, valor)

        self.size +=1



    def crearMatriz(self, size):
        for i in range(size):
            self.insertar(None)



    def editarPos(self, valor, i, j, max):
        pos = self.rowMajor(j,i,max)
        aux = self.raiz 

        while aux != None:
            if aux.pos == pos:
                aux.valor = valor
                break
            aux = aux.siguiente


    def getPos(self, i, j, max):
        pos = self.rowMajor(j,i,max)
        aux = self.raiz 

        while aux != None:
            if aux.pos == pos:
                return aux.valor
            aux = aux.siguiente
        return "Error"



    def imprimir(self):
        aux = self.raiz
        while aux != None:
            print("Pos: "+ str(aux.pos) +" - Valor: "+  str(aux.valor))
            aux = aux.siguiente



    def rowMajor(self, x, y, maxY):
        return x + y * maxY





if __name__ == '__main__':
    print("Ejemplo Row Major")
    lista = Lista()
    max = 3
    lista.crearMatriz(max * max)

    lista.editarPos("Primero", 0,0 ,max)
    lista.editarPos("Segundo", 0,1 ,max)
    lista.editarPos("Tercero", 0,2 ,max)
    lista.editarPos("Cuarto", 1,1 ,max)

    for i in range(max):
        for j in range(max):
            print("| ("+str(i)+","+str(j)+")", end=" - ")
            print(lista.getPos(i,j,max) ,end=" | ")
        print()

    lista.imprimir()
    print(lista.getPos(0, 1 ,max))


    
   

    