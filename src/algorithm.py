from object import Pacient, Grids
from lists import List, Node
import simulation, diagnostic

#global infected
#infected = []
#
def evaluateMatrix(m, matrix, periods):

    #print("Periodos : ", periods)

    for n in range(periods):

        infected = []

        for i in range(m):
            for j in range(m):

                #print("Celda actual: ",i,",",j,")", matrix.getCell(i,j,m), "\n")

                actualCell = matrix.getCell(i,j,m)

                neighbor1 = matrix.getCell(i-1,j-1,m) 
                neighbor2 = matrix.getCell(i-1,j,m)
                neighbor3 = matrix.getCell(i-1,j+1,m)
                neighbor4 = matrix.getCell(i,j-1,m)
                neighbor5 = matrix.getCell(i,j+1,m)
                neighbor6 = matrix.getCell(i+1,j-1,m)
                neighbor7 = matrix.getCell(i+1,j,m)
                neighbor8 = matrix.getCell(i+1,j+1,m)

                #print(neighbor1,neighbor2,neighbor3,neighbor4,neighbor5,neighbor6,neighbor7,neighbor8) 
                
                #print("Las celulas infectadas son: ", evaluateCells(neighbor1,neighbor2,neighbor3,neighbor4,neighbor5,neighbor6,neighbor7,neighbor8),"\n")
                sickCells = evaluateCells(neighbor1,neighbor2,neighbor3,neighbor4,neighbor5,neighbor6,neighbor7,neighbor8)

                c = evaluateSicks(actualCell, sickCells, matrix, m , i, j)
                #print("Infectado: ", c,"\n")
            
        infecteCells(matrix, m, infected)

        simulation.printPeriods(matrix, m, n)  

        #print("Posiciones infectadas: ")
        #print(infected)

        Grids.addGrids(n+1, infected)  

        #diagnostic.saveInfected(infected )
              

def evaluateCells(neighbor1,neighbor2,neighbor3,neighbor4,neighbor5,neighbor6,neighbor7,neighbor8):

    sickCells = 0

    if neighbor1 == "█":
        sickCells += 1

    if neighbor2 == "█":
        sickCells += 1

    if neighbor3 == "█":
        sickCells += 1

    if neighbor4 == "█":
        sickCells += 1

    if neighbor5 == "█":
        sickCells += 1

    if neighbor6 == "█":
        sickCells += 1

    if neighbor7 == "█":
        sickCells += 1     

    if neighbor8 == "█":
        sickCells += 1    

    return sickCells        

def evaluateSicks(actualCell, sickCells, matrix, m, x, y):

    if actualCell == "░":

        if sickCells == 3:
            matrix.editCell(actualCell, 1, x, y ,m) 
            #print(matrix.getStatus(x,y,m))

            return matrix.getStatus(x,y,m)

        else:
            matrix.editCell(actualCell, 0, x, y ,m) 
            #print(matrix.getStatus(x,y,m))

            return matrix.getStatus(x,y,m)

    elif actualCell == "█":

        if (sickCells == 3) or (sickCells ==2):
            matrix.editCell(actualCell, 1, x, y ,m) 
            #print(matrix.getStatus(x,y,m))

            return matrix.getStatus(x,y,m)

        else:
            matrix.editCell(actualCell, 0, x, y ,m)  
            #print(matrix.getStatus(x,y,m))

            return matrix.getStatus(x,y,m)    

def infecteCells(matrix, m, infected):

    for i in range(m):

        for j in range(m):

            if matrix.getStatus(i, j, m) == 1:
                matrix.editCell("█", 1, i, j ,m) 

                coords = [i,j]
                infected.append(coords)
               #print(infected)


            elif matrix.getStatus(i, j, m) == 0:

                matrix.editCell("░", 0, i, j ,m)


#def saveInfected(coords):
    

        
               
