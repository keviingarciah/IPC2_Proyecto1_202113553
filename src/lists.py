#from object import Pacient

class Node:

    def __init__(self, pos=0, value=None, status=None) -> None:
        self.pos = pos
        self.value = value
        self.status = status
        self.next = None

class List: 
   #global infected
   #infected = []

   #global coordinates
   #coordinates = []

    def __init__(self) -> None: 
        self.size = 0
        self.root = None 

    def insert(self, value, status):
        if(self.root==None):
            self.root = Node(self.size, value, status)

        else:
            aux = self.root
            while aux.next != None:
                aux = aux.next
            aux.next = Node(self.size, value, status)

        self.size +=1      
        
    def getMatrix(self, size):
        for i in range(size):
            self.insert("░", 0)       

    def editCell(self, value, status, i, j, max):
        pos = self.rowMajor(j,i,max)
        aux = self.root

        while aux != None:
            if aux.pos == pos:
                aux.value = value
                aux.status = status
                break
            aux = aux.next        

    def getCell(self, i, j, max):
        pos = self.rowMajor(j,i,max)
        aux = self.root

        while aux != None:
            if aux.pos == pos:
                return aux.value
            aux = aux.next
        return "Error" 

    def getStatus(self, i, j, max):
        pos = self.rowMajor(j,i,max)
        aux = self.root

        while aux != None:
            if aux.pos == pos:
                return aux.status
            aux = aux.next
        return "Error"             


    def rowMajor(self, x, y, maxY):
        return x + y * maxY              

            
