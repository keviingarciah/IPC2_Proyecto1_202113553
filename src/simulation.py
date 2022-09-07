from object import Pacient, Grids
from lists import Node, List
import algorithm, os


def simulate(pacient):

    folder = 'Gráficas'

    for f in os.listdir(folder):
        filep_path = os.path.join(folder, f)
        os.unlink(filep_path)

    m = Pacient.getDimension(pacient)

    matrix = List()

    matrix.getMatrix(m * m)

    print_matrix(matrix, m)

    #---------------------------------
    
    getInfected(matrix, m, pacient)

    periods = Pacient.getPeriods(pacient)

    print_matrix(matrix, m) 

    algorithm.graphicInitial(matrix, m) 

    results = algorithm.evaluateMatrix(m, matrix, periods, pacient)

    return results
 
def getInfected(matrix, m, pacient):

    cells = Pacient.getCells(pacient)

    initial = []

    for i in range(len(cells)):

        x = cells[i][0]           #Esto para que quede en coordenadas de la matriz
        y = cells[i][1]
        matrix.editCell("█", 1, x, y ,m) 

        coords = [x,y]
        
        initial.append(coords)

        if i == len(cells)-1:
            Grids.addGrids(0, initial, pacient)


        
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