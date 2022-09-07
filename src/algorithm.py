
from object import Pacient, Grids
from lists import List, Node
import simulation, diagnostic
import os

def evaluateMatrix( m, matrix, periods, pacient): #next

    for n in range(periods):

        grid = []

        for i in range(m):
            for j in range(m):

                actualCell = matrix.getCell(i,j,m)

                neighbor1 = matrix.getCell(i-1,j-1,m) 
                neighbor2 = matrix.getCell(i-1,j,m)
                neighbor3 = matrix.getCell(i-1,j+1,m)
                neighbor4 = matrix.getCell(i,j-1,m)
                neighbor5 = matrix.getCell(i,j+1,m)
                neighbor6 = matrix.getCell(i+1,j-1,m)
                neighbor7 = matrix.getCell(i+1,j,m)
                neighbor8 = matrix.getCell(i+1,j+1,m)

                sickCells = evaluateCells(neighbor1,neighbor2,neighbor3,neighbor4,neighbor5,neighbor6,neighbor7,neighbor8)

                evaluateSicks(actualCell, sickCells, matrix, m , i, j)
            
        infecteCells(matrix, m, grid)

        simulation.printPeriods(matrix, m, n)  
        
        results = Grids.compareGrids(n+1, grid, pacient)  


        graphicMatrix(matrix, m, str(n+1))

        if results[0] == "Enfermedad MORTAL":
            
            break

        elif results[0] == "Enfermedad GRAVE":

            break

        Grids.addGrids(n+1, grid, pacient)  

    print("Diagnóstico: "+results[0]+", N: "+str(results[1])+", N1: "+str(results[2]))

    Pacient.editResults(pacient, results[0], results[1], results[2])

    return results


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

            return matrix.getStatus(x,y,m)

        else:
            matrix.editCell(actualCell, 0, x, y ,m) 

            return matrix.getStatus(x,y,m)

    elif actualCell == "█":

        if (sickCells == 3) or (sickCells ==2):
            matrix.editCell(actualCell, 1, x, y ,m) 

            return matrix.getStatus(x,y,m)

        else:
            matrix.editCell(actualCell, 0, x, y ,m)  

            return matrix.getStatus(x,y,m)    

def infecteCells(matrix, m, infected):

    for i in range(m):

        for j in range(m):

            if matrix.getStatus(i, j, m) == 1:
                matrix.editCell("█", 1, i, j ,m) 

                coords = [i,j]
                infected.append(coords)

            elif matrix.getStatus(i, j, m) == 0:

                matrix.editCell("░", 0, i, j ,m)

def graphicMatrix(matrix, m, n):

    graphviz = 'digraph EJEMPLO{\n    node [shape=plaintext];'
    graphviz += '\n    struct1 [label=<'
    graphviz += '\n        <TABLE>'

    for i in range(m):
        graphviz += '\n        	<TR>'

        for j in range(m):

            if matrix.getStatus(i, j, m) == 1:

                graphviz += '\n        	    <td bgcolor="green"></td>'

            elif matrix.getStatus(i, j, m) == 0:
                graphviz += '\n        	    <td bgcolor="white"></td>'        

        graphviz += '\n        	</TR>'
            
    graphviz += '\n        </TABLE>'

    graphviz += '\n    >];'
    graphviz += '\n}'

    with open('Gráficas\graphviz.txt', 'w') as file:

            file.write(graphviz)

    os.system('dot.exe -Tpng Gráficas\graphviz.txt -o Gráficas\Período_'+n+'.png')
    
def graphicInitial(matrix, m):

    graphviz = 'digraph PROYECTO_1{\n    node [shape=plaintext];'
    graphviz += '\n    struct1 [label=<'
    graphviz += '\n        <TABLE>'

    for i in range(m):
        graphviz += '\n        	<TR>'

        for j in range(m):

            if matrix.getStatus(i, j, m) == 1:

                graphviz += '\n        	    <td bgcolor="green"></td>'

            elif matrix.getStatus(i, j, m) == 0:
                graphviz += '\n        	    <td bgcolor="white"></td>'        

        graphviz += '\n        	</TR>'
            
    graphviz += '\n        </TABLE>'

    graphviz += '\n    >];'
    graphviz += '\n}'

    with open('Gráficas\graphviz.txt', 'w') as file:

            file.write(graphviz)

    os.system('dot.exe -Tpng Gráficas\graphviz.txt -o Gráficas\Período_0.png')