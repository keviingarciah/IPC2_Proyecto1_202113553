import tkinter as tk
from tkinter import filedialog, ttk
from turtle import width
import load, simulation, algorithm, diagnostic
from object import Pacient
from PIL import ImageTk, Image

class Menu(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("¡Bienvenido!")
        self.geometry("430x480+580+150")
        self.resizable(0,0)

        # ============ create two frames ============
        # Frame 1
        self.frame_1 = tk.Frame(self,width=240, height = 480)
        self.frame_1.grid( row=0, column=0, padx=(30,30), pady=(30,30))

        #Labels 1
        self.label_1_1 = tk.Label(self.frame_1, text="Menú Principal")  # font name and size in px
        self.label_1_1.grid(row=1, column=0, pady=(10,5), padx=10)

        #self.label_1_2 = tk.Label(self.frame_1, text="Menú Principal")  # font name and size in px
        #self.label_1_2.grid(row=2, column=0, pady=(0,5), padx=10)

        #self.label_1_3 = tk.Label(self.frame_1, text="Kevin Ernesto García Henrández")  # font name and size in px
        #self.label_1_3.grid(row=3, column=0, pady=(0,5), padx=10)

        #self.label_1_4 = tk.Label(self.frame_1, text="202113553")  # font name and size in px
        #self.label_1_4.grid(row=4, column=0, pady=(0,5), padx=10)

        # Frame 2
        self.frame_2 = tk.Frame(self,width=240, height = 480)
        self.frame_2.grid( row=1, column=0, padx=(30,30), pady=(0,30))

        self.label_2_1 = tk.Label(self.frame_2, text="Eliga una opción:")  # font name and size in px
        self.label_2_1.grid(row=0, column=0, pady=(10,5), padx=115)

        self.button_2_1 = tk.Button(self.frame_2, text="Cargar Archivo", command = self.openFile) 
        self.button_2_1.grid(row=1, column=0, pady=10, padx=20)

        self.button_2_2 = tk.Button(self.frame_2, text="Iniciar Simulación", command = self.simulate)
        self.button_2_2.grid(row=2, column=0, pady=10, padx=20)

        self.button_2_3 = tk.Button(self.frame_2, text="xml", command = self.XML)
        self.button_2_3.grid(row=3, column=0, pady=10, padx=20)

        self.button_2_4 = tk.Button(self.frame_2, text="Salir", command = self.quit)
        self.button_2_4.grid(row=4, column=0, pady=10, padx=20)

    def openFile(self):
        filepath = filedialog.askopenfilename(title =  "Carga de Archivo", filetypes=[('all', '*'),('archivo LFP', '*LFP, *lfp'),('archivo CSV', '*CSV, *csv')])
        print(filepath)

        load.read(filepath)

    def simulate(self):
        #simulation.print_matrix()
        #simulation.simulate()
        Simulation(self)

    def XML(self):

        print("Se da el xml") 
        #diagnostic.generateXML()    <-------------- ESTE ES EL BUENO

        Graph(self)

    def exit(self):  
        self.quit()    


class Simulation(tk.Toplevel):

    def __init__(self, master):
        super().__init__()
        
        self.master = master

        self.title("sIMULAR")
        self.geometry("380x280+600+210")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

        # Frame 1
        self.frame_o2 = tk.Frame(master=self,width=240, height = 480)
        self.frame_o2.grid(row=0, column=0, padx=(30,30), pady=(30,15))

        self.label_o_2 = tk.Label(master=self.frame_o2, text="Elija alguno:")  # font name and size in px
        self.label_o_2.grid(row=0, column=0, pady=(15,20), padx=10)

        n = tk.StringVar()
        self.combox = ttk.Combobox(master=self.frame_o2, width = 27, textvariable = n) 
        self.combox.grid(row=0, column=1, pady=(15,20), padx=10)
        
        list = []

        self.combox['values'] = Pacient.getPacient(list)

        self.button_o_1 = tk.Button(master=self.frame_o2, text="Simular", command=self.simulate)
        self.button_o_1.grid(row=1, column=1, pady=(10,20), padx=10)

        self.button_o_2 = tk.Button(master=self, text="Regresar", command=self.back_to_main)
        self.button_o_2.grid(row=2, column=0, pady=(15,20), padx=10)

        self.master.withdraw()

    def back_to_main(self):
        self.master.deiconify()
        self.destroy()   

    def simulate(self):

        print(self.combox.get())
        pacient = self.combox.get()

        simulation.simulate(self, pacient)  

        #Graph(self) 

class Graph(tk.Toplevel):
    def __init__(self, master, condition):
        super().__init__()

        self.condition = condition
        self.master = master

        self.title("Simulación")
        self.geometry("435x650+600+100")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

        self.frame_g = tk.Frame(master=self,width=240, height = 480)
        self.frame_g.grid(row=1, column=0, padx=(30,30), pady=(15,5))

        self.image = Image.open("graphviz.png")

        self.img = self.image.resize((350, 350))

        self.graph = ImageTk.PhotoImage(self.img)

        self.image_label = tk.Label(master = self.frame_g, image = self.graph)
        self.image_label.grid(row=0, column=0, padx=10, pady=5)

        self.label_p = tk.Label(master=self, text="Período: 0", font = ("Arial, 25"))  # font name and size in px
        self.label_p.grid(row=0, column=0, pady=(20,0), padx=10)


        self.button_g_1 = tk.Button(master=self, text="Siguiente", height=2, width=10, command=self.nextPeriod)
        self.button_g_1.grid(row=2, column=0, pady=(10,0), padx=10)

        self.button_g_3 = tk.Button(master=self, text="Terminar", height=2, width=10, command = self.allPeriods)
        self.button_g_3.grid(row=3, column=0, pady=(10,0), padx=10)
        
        self.button_g_2 = tk.Button(master=self, text="Regresar", height=2, width=10, command = self.back_to_main)
        self.button_g_2.grid(row=4, column=0, pady=(15,20), padx=10)

        self.master.withdraw()


    def back_to_main(self):
        self.master.deiconify()
        self.destroy()   

    def nextPeriod(self):
        
        self.image = Image.open("graphviz.png")

        self.img = self.image.resize((350, 350))

        self.graph = ImageTk.PhotoImage(self.img)

        self.image_label = tk.Label(master = self.frame_g, image = self.graph)
        self.image_label.grid(row=0, column=0, padx=10, pady=5)

        self.condition = "next"

    def allPeriods(self):

        self.image_label.destroy()

        self.image = Image.open("graphviz.png")

        self.img = self.image.resize((350, 350))

        self.graph = ImageTk.PhotoImage(self.img)

        self.image_label = tk.Label(master = self.frame_g, image = self.graph)
        self.image_label.grid(row=0, column=0, padx=10, pady=5)

        self.condition = "finish"

        

class Periods(tk.Toplevel):
    def __init__(self, master, m, matrix, periods, pacient):
        super().__init__()
        
        self.master = master

        self.title("Simulación")
        self.geometry("435x650+600+100")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

        self.frame_g = tk.Frame(master=self,width=240, height = 480)
        self.frame_g.grid(row=1, column=0, padx=(30,30), pady=(15,5))

        self.image = Image.open("graphviz.png")

        self.img = self.image.resize((350, 350))

        self.graph = ImageTk.PhotoImage(self.img)

        self.image_label = tk.Label(master = self.frame_g, image = self.graph)
        self.image_label.grid(row=0, column=0, padx=10, pady=5)

        self.label_p = tk.Label(master=self, text="Período: 0", font = ("Arial, 25"))  # font name and size in px
        self.label_p.grid(row=0, column=0, pady=(20,0), padx=10)


        self.button_g_1 = tk.Button(master=self, text="Siguiente", height=2, width=10, command=self.nextPeriod)
        self.button_g_1.grid(row=2, column=0, pady=(10,0), padx=10)

        self.button_g_3 = tk.Button(master=self, text="Terminar", height=2, width=10, command = self.allPeriods)
        self.button_g_3.grid(row=3, column=0, pady=(10,0), padx=10)
        
        self.button_g_2 = tk.Button(master=self, text="Regresar", height=2, width=10, command = self.back_to_main)
        self.button_g_2.grid(row=4, column=0, pady=(15,20), padx=10)

        self.master.withdraw()

    def back_to_main(self):
        self.master.deiconify()
        self.destroy()   

    def nextPeriod(self):

        return 1

    def allPeriods(self):

        return 1        


if __name__ == "__main__":

    root = Menu()
    root.mainloop()