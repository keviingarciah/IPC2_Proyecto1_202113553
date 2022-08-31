from object import Pacient, Grids
from lists import Node, List
from main import Graph, Simulation, Menu
import algorithm


def simulate(pacient):

    print("Se simula: \n")

    m = Pacient.getDimension(pacient)
    print("Las dimensiones son: ", m, "*", m)

    matrix = List()

    matrix.getMatrix(m * m)

    print_matrix(matrix, m)

    #---------------------------------
    
    getInfected(matrix, m, pacient)

    periods = Pacient.getPeriods(pacient)

    print_matrix(matrix, m) #Se impreme y genera la matriz en png

    algorithm.graphicMatrix(matrix, m) 

    print("\n")


    algorithm.evaluateMatrix(m, matrix, periods, pacient)

    

    
def getInfected(matrix, m, pacient):

    cells = Pacient.getCells(pacient)


    print("Las coordenadas son: ", cells, "len de la matriz: ", len(cells))

    initial = []

    for i in range(len(cells)):
        print(cells[i][0], cells[i][1])
        x = cells[i][0] - 1            #Esto para que quede en coordenadas de la matriz
        y = cells[i][1] - 1 
        matrix.editCell("█", 1, x, y ,m) 

        coords = [x,y]
        
        initial.append(coords)


        if i == len(cells)-1:
            print("INICIAL:")    
            print(initial)
            Grids.addGrids(0, initial, pacient)

    #Grids.addGrids(0, initial, pacient)
        
def print_matrix(matrix, m):

    print("Perído 0\n")

    for i in range(m):
        for j in range(m):
            print(" ", matrix.getCell(i,j,m) ,end=" ")
        print("\n")

    Grids.getGrid(0)   


def printPeriods(matrix, m, periods):

    print("Perído ",periods + 1,"\n")

    for i in range(m):
        for j in range(m):
            print(" ", matrix.getCell(i,j,m) ,end=" ")
        print("\n")