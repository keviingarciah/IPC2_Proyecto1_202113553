import xml.etree.ElementTree as ET

class Pacient: 

    global pacients
    pacients = []

    def __init__(self, name, age, periods, m, results, n, n1, cells ): 
        self.name = name 
        self.age = age
        self.periods = periods
        self.m = m
        self.results = results
        self.n = n
        self.n1 = n1
        self.cells = cells


    def knowList ():

        if len(pacients) == 0:

            return False

        else:
            return True    


    def add_to_list(name, age, periods, m, results, n, n1, cells):

        pacients.append(Pacient(name, age, periods, m, results, n, n1, cells))


    def getPacient(values):

        for i in pacients:
            z = i.name
            values.append(z)

        return values


    def getDimension(pacient):

        for i in pacients:
            if i.name == pacient:
                x = i.m
                break

        return x    

    def getCells(pacient):

        for i in pacients:
            if i.name == pacient:
                y = i.cells
                break

        return y      

    def getPeriods(pacient):

        for i in pacients:
            if i.name == pacient:
                n = i.periods
                break

        return n    


    def editResults(pacient, results, n0, n1):

        for i in pacients:

            if i.name == pacient:

                i.results = results
                i.n = n0
                i.n1 = n1

                break
     
    def getResults (all):

        for i in pacients:

            data = [i.name, i.age, i.periods, i.m, i.results, i.n, i.n1]

            all.append(data)

        return all

class Grids: 

    global infected
    infected = []

    def __init__(self, period, coords, n0, n1, pacient): 
        self.period = period
        self.coords = coords
        self.n0 = n0
        self.n1 = n1
        self.pacient = pacient


    def addGrids(period, coords, pacient):

        n0 = 0
        n1 = 0

        infected.append(Grids(period, coords, n0, n1, pacient))

    def getGrid(k):

        for i in infected:

            if i.period == k:

                ords = i.coords

                return ords


    def compareGrids(n, grid, pacient):

        status = ""

        for i in infected:

            if grid == i.coords:
                period_repeated =  i.period

                if period_repeated == 0:
                    n0 = n - period_repeated
                    n1 = 0

                    if n0 == 1:
                        status = "Enfermedad MORTAL"
                        return status, n0, n1 

                    else:
              
                        status = "Enfermedad GRAVE"


                else: 
                    n0 = n
                    n1 = n - period_repeated

                    if n1 == 1:
                        status = "Enfermedad MORTAL"
                        return status, n0, n1 


                    else:
                        status = "Enfermedad GRAVE"


        if status == "Enfermedad GRAVE":
            return status, n0, n1 

        else:    
            status = "Enfermedad LEVE"
            n0 = 0
            n1 = 0
            return status, n0, n1        

        

        



            