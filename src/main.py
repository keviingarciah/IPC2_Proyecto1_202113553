import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import load, simulation, diagnostic, webbrowser
from object import Pacient


class Menu(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("¡Bienvenido!")
        self.geometry("430x420+600+170")
        self.resizable(0,0)

        self.frame_1 = tk.Frame(self,width=240, height = 480)
        self.frame_1.grid( row=0, column=0, padx=(30,30), pady=(30,30))

        self.label_1_1 = tk.Label(self.frame_1, text="IPC2 - PRÁCTICA NO. 1", font=("Arial", 15))  # font name and size in px
        self.label_1_1.grid(row=1, column=0, pady=(10,5), padx=10)
        
        self.frame_2 = tk.Frame(self,width=240, height = 480)
        self.frame_2.grid( row=1, column=0, padx=(30,30), pady=(0,30))

        self.label_2_1 = tk.Label(self.frame_2, text="Eliga una opción:", font=("Arial", 13))  # font name and size in px
        self.label_2_1.grid(row=0, column=0, pady=(10,5), padx=115)

        self.button_2_1 = tk.Button(self.frame_2, text="Cargar Archivo", command = self.openFile) 
        self.button_2_1.grid(row=1, column=0, pady=10, padx=20)

        self.button_2_2 = tk.Button(self.frame_2, text="Iniciar Simulación", command = self.simulate)
        self.button_2_2.grid(row=2, column=0, pady=10, padx=20)

        self.button_2_2 = tk.Button(self.frame_2, text="Generar XML", command = self.xml)
        self.button_2_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_2_4 = tk.Button(self.frame_2, text="Salir", command = self.quit)
        self.button_2_4.grid(row=4, column=0, pady=10, padx=20)

    def openFile(self):
        
        filepath = filedialog.askopenfilename(title = "Carga de Archivo", filetypes=[('all', '*')])
        print(filepath)

        load.read(filepath)

        condition = Pacient.knowList()

        if condition is True:

            messagebox.showinfo(message="Se cargó el archivo correctamente.", title="Archivo cargado") 

    def simulate(self):
        Simulation(self)

    def xml(self):
        XML(self)    
        
    def exit(self):  
        self.quit()    


class Simulation(tk.Toplevel):

    def __init__(self, master):
        super().__init__()
        
        self.master = master

        self.title("Simular")
        self.geometry("400x270+610+230")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

        self.frame_o2 = tk.Frame(master=self,width=240, height = 480)
        self.frame_o2.grid(row=0, column=0, padx=(30,30), pady=(30,15))

        self.label_o_2 = tk.Label(master=self.frame_o2, text="Elija alguno: ", font=("Arial", 12))  # font name and size in px
        self.label_o_2.grid(row=0, column=0, pady=(15,20), padx=10)

        n = tk.StringVar()
        self.combox = ttk.Combobox(master=self.frame_o2, width = 27, textvariable = n) 
        self.combox.grid(row=0, column=1, pady=(15,20), padx=10)
        
        list = []

        self.combox['values'] = Pacient.getPacient(list)

        self.button_o_1 = tk.Button(master=self.frame_o2, text="Simular", command=self.simulate)
        self.button_o_1.grid(row=1, column=1, pady=(10,20), padx=10)

        self.button_o_3 = tk.Button(master=self, text="Regresar", command=self.back_to_main)
        self.button_o_3.grid(row=2, column=0, pady=(0,20), padx=10)

        self.master.withdraw()

    def back_to_main(self):
        self.master.deiconify()
        self.destroy()   

    def simulate(self):

        print("\n Paciente: ", self.combox.get())
        print("----------------------")
        pacient = self.combox.get()
        
        results = simulation.simulate(pacient)  

        if results[2] != 0:
            messagebox.showinfo(message="El paciente tiene una "+str(results[0])+", donde el patrón se repite por primera vez" 
            +"en el periodo "+str(results[1])+" cada "+str(results[2])+" periodos." , title="Simulación terminada.") 

        elif results[1] != 0:    
            messagebox.showinfo(message="El paciente tiene una "+str(results[0])+", donde el patrón se repite cada " 
            +str(results[1])+" periodos." , title="Simulación terminada.") 

        else:
            messagebox.showinfo(message="El paciente tiene una "+str(results[0])+", por lo cual podrá vivir una bonita vida :D.", title="Simulación terminada.") 

        messagebox.showinfo(message="Se generaron cada uno de los periodos de la simulación.", title="Rejillas generadas.") 
        webbrowser.open('Gráficas')

class XML(tk.Toplevel):

    def __init__(self, master):
        super().__init__()
        
        self.master = master

        self.title("Generar XML")
        self.geometry("400x270+610+240")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

        # Frame 1
        self.frame_o2 = tk.Frame(master=self,width=240, height = 480)
        self.frame_o2.grid(row=0, column=0, padx=(30,30), pady=(30,15))

        self.label_o_2 = tk.Label(master=self.frame_o2, text="Elija alguno: ", font=("Arial", 12))  # font name and size in px
        self.label_o_2.grid(row=0, column=0, pady=(15,20), padx=10)

        n = tk.StringVar()
        self.combox = ttk.Combobox(master=self.frame_o2, width = 27, textvariable = n) 
        self.combox.grid(row=0, column=1, pady=(15,20), padx=10)
        
        list = []

        self.combox['values'] = Pacient.getPacient(list)

        self.button_o_1 = tk.Button(master=self.frame_o2, text="Generar XML", command=self.generate)
        self.button_o_1.grid(row=1, column=1, pady=(10,20), padx=10)

        self.button_o_3 = tk.Button(master=self, text="Regresar", command=self.back_to_main)
        self.button_o_3.grid(row=2, column=0, pady=(0,20), padx=10)

        self.master.withdraw()


    def back_to_main(self):
        self.master.deiconify()
        self.destroy()   

    def generate(self):

        print("\nSe da el XML de ",self.combox.get())
        pacient = self.combox.get()

        diagnostic.generateXML(pacient)   
        messagebox.showinfo(message="Se generó el archivo XML.", title="Resultados cargados")   


if __name__ == "__main__":

    root = Menu()
    root.mainloop()