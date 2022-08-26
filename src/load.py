import xml.etree.ElementTree as ET
from object import Pacient

def read (filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    print("Root:", root)


    #coords = []

    for patient in root: 

        if patient.tag == "paciente":
            
            for data in patient:

                if data.tag == "datospersonales":

                    for sub_data in data:

                        if sub_data.tag == "nombre":

                            print (sub_data.text)
                            name = sub_data.text

                        elif sub_data.tag == "edad":

                            print (sub_data.text)  
                            age = int(sub_data.text)
                            #age = (sub_data.text)

                elif data.tag == "periodos": 

                    print (data.text)
                    periods = int(data.text)

                elif data.tag == "m": 

                    print (data.text)
                    m = int(data.text)

                elif data.tag == "rejilla":

                    cells = []

                    for sub_data in data:
                        

                        if sub_data.tag == "celda":

                            print (sub_data.get('f'), sub_data.get('c'))
                            f = int(sub_data.get('f'))

                            c = int(sub_data.get('c'))

                            coords = [f, c]
                            
                            cells.append(coords)


            results = ""
            n = 0   

        
            print(cells)
            
            Pacient.add_to_list( name, age, periods, m, results, n, cells)     
        
                             


                            
        
             