import xml.etree.ElementTree as ET

class Pacient: 

    global pacients
    pacients = []

    def __init__(self, name, age, periods, m, results, n, n1, cells ): 
        self.name = name 
        self.age = age
        self.periods = periods
        self.m = m
        #self.c = c
        #self.f = f
        self.results = results
        self.n = n
        self.n1 = n1
        self.cells = cells    


    def add_to_list(name, age, periods, m, results, n, n1, cells):

        pacients.append(Pacient(name, age, periods, m, results, n, n1, cells))
        print(pacients)
        print(len(pacients))

        for i in pacients:
            print(i.name, i.age, i.periods, i.m)
            print(i.cells)


    def getPacient(values):
        print("Se obtienen el paciente: ", len(pacients))

        for i in pacients:
            print(i.name)
            z = i.name
            values.append(z)

        return values


    def getDimension(pacient):
        print("Se obtienen las dimensiones: ")

        for i in pacients:
            if i.name == pacient:
                print(i.m)
                x = i.m
                break

        return x    

    def getCells(pacient):
        print("Se obtienen las coordenadas: ", pacient)

        for i in pacients:
            if i.name == pacient:
                print(i.cells)
                y = i.cells
                break

        return y      

    def getPeriods(pacient):
        print("Se obtienen los periodos: ", pacient)

        for i in pacients:
            if i.name == pacient:
                print(i.periods)
                n = i.periods
                break

        return n    


    def editResults(pacient, results, n0, n1):
        print("Se editan los resultados de: ", pacient)

        for i in pacients:

            if i.name == pacient:

                i.results = results
                i.n = n0
                i.n1 = n1

                print(i.results, i.n, i.n1)

                break
     
    def getResults (all):

        for i in pacients:

            name = i.name 
            age = i.age
            periods = i.periods
            m = i.m
            results = i.results
            n = i.n
            n1 = i.n1

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

        print("Se agrego la rejilla")
        #print(infected)
        #print(len(infected))

       #for i in infected:
       #    print(i.period, i.pacient)
       #    print(i.coords)

    def getGrid(k):
        print("Se obtienen la rejilla: ", k)

        for i in infected:

            if i.period == k:
                print("Las coordenadas: ")
                print(i.coords)
                ords = i.coords

                return ords


    def compareGrids(n, grid, pacient):

        status = ""

        print("Comparando periodo: ", n, "de paciente : ", pacient)
        print(grid, "\n")

        for i in infected:

            if grid == i.coords:

                print("Las coordenadas se repiten en: ", i.period)
                print(i.coords, "\n")

                period_repeated =  i.period

                if period_repeated == 0:
                    
                    n0 = n - period_repeated
                    n1 = 0

                    print("NO. DE PERIODOS: ", n0, "\n")
                

                    if n0 == 1:
                        print("Enfermedad MORTAL")

                        status = "Enfermedad MORTAL"
                        return status, n0, n1 

                    else:
                        print("Enfermedad GRAVE")   
                        status = "Enfermedad GRAVE"
                        #return status

                else: 

                    n0 = n   
                    n1 = n0 - period_repeated

                    print("NO. DE PERIODOS: ", n1, "\n")

                    if n1 == 1:
                        print("Enfermedad MORTAL")
                        status = "Enfermedad MORTAL"
                        return status, n0, n1 


                    else:
                        print("Enfermedad GRAVE")   
                        status = "Enfermedad GRAVE"
                        #return status

        if status == "Enfermedad GRAVE":
            return status, n0, n1 

        else:    
            print("ENFERMEDAD LEVE")   
            status = "Enfermedad LEVE"
            n0 = 0
            n1 = 0
            return status, n0, n1        

        

        



            