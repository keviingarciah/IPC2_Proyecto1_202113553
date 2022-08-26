class Pacient: 

    global pacients
    pacients = []

    def __init__(self, name, age, periods, m, results, n, cells ): 
        self.name = name 
        self.age = age
        self.periods = periods
        self.m = m
        #self.c = c
        #self.f = f
        self.results = results
        self.n = n
        self.cells = cells    


    def add_to_list(name, age, periods, m, results, n, cells):

        pacients.append(Pacient(name, age, periods, m, results, n, cells))
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


class Grids: 

    global infected
    infected = []

    def __init__(self, period, coords ): 
        self.period = period
        self.coords = coords


    def addGrids(period, coords):

        infected.append(Grids(period, coords))
        #print(infected)
        #print(len(infected))

       #for i in infected:
       #    print(i.period)
       #    print(i.coords)
  
    #def getPeriods(condition):
    #    print("Se obtienen el periodo: ", condition)
#
    #    for i in infected:
    #        if condition == pacient:
    #            print(i.periods)
    #            n = i.periods
    #            break
#
    #    return n    




            