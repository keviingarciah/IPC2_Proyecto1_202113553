import xml.etree.ElementTree as ET
from object import Pacient
from tkinter import messagebox

def read (filepath):

    try:
        tree = ET.parse(filepath)
    
        root = tree.getroot()

        for patient in root: 

            if patient.tag == "paciente":
                
                for data in patient:

                    if data.tag == "datospersonales":

                        for sub_data in data:

                            if sub_data.tag == "nombre":

                                name = sub_data.text

                            elif sub_data.tag == "edad":
 
                                age = int(sub_data.text)

                    elif data.tag == "periodos": 

                        periods = int(data.text)

                    elif data.tag == "m": 

                        m = int(data.text)

                    elif data.tag == "rejilla":

                        cells = []

                        for sub_data in data:
                            

                            if sub_data.tag == "celda":

                                f = int(sub_data.get('f'))

                                c = int(sub_data.get('c'))

                                coords = [f, c]
                                
                                cells.append(coords)

                results = ""
                n = 0   
                n1 = 0

                Pacient.add_to_list( name, age, periods, m, results, n, n1, cells)     
        
                             
    except:
        messagebox.showerror(message="No se cargó ningún archivo.", title="Sin cargar")  

                            
        
             