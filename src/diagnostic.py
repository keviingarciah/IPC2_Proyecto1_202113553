import xml.etree.ElementTree as ET
from object import Pacient

def generateXML():

    all = []

    all = Pacient.getResults(all)

    #print(all)

    pacients = ET.Element("pacientes")

    for i in range(len(all)):

        pacient= ET.Element("paciente")
        pacients.append(pacient) 

        dates = ET.Element("datospersonales")
        pacient.append(dates)

        name = ET.SubElement(dates, "nombre")
        name.text = all[i][0]

        age = ET.SubElement(dates, "edad")
        age.text = str(all[i][1])

        period = ET.SubElement(pacient, "periodos")
        period.text = str(all[i][2])

        m = ET.SubElement(pacient, "m")
        m.text = str(all[i][3])

        result = ET.SubElement(pacient, "resultado")
        result.text = all[i][4]

        if all[i][6] != 0:
            n = ET.SubElement(pacient, "n")
            n.text = str(all[i][5])

            n1 = ET.SubElement(pacient, "n1")
            n1.text = str(all[i][6])

        if all[i][6] != 0:

            n = ET.SubElement(pacient, "n")
            n.text = str(all[i][5])


    tree = ET.ElementTree(pacients)
    ET.indent(pacients)
    tree.write("Resultados\Resultados.xml", xml_declaration=True, encoding='utf-8')
