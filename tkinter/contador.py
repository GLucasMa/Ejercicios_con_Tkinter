#Porque tengo que importar como tk y no me deja usar el comando Tk. directamente sobre los metodos o atributos?

import tkinter as tk
from tkinter import ttk

def sumar():
    producto.set(str(int(producto.get()) + 1))

root= tk.Tk()
root.title("contador")
root.geometry('450x250')

label = tk.Label (root, text='contador')

label.place(x=50, y=100)

producto = tk.StringVar(root, "0")
prod = tk.Entry(root, textvariable= producto)
prod.config(state="disabled")
prod.place(x=120,y=100)

botonmas = ttk.Button(root, text="+", command= sumar)
botonmas.place(x=300,y=100)

root.mainloop()

"""
import tkinter as tk
from tkinter import ttk


def sumar():
    produccion.set(str(int(produccion.get()) + 1))     


raiz = tk.Tk()
produccion = tk.StringVar(raiz, "0")
prod = tk.Entry(raiz, textvariable=produccion)
prod.pack(side=tk.TOP)
contador = ttk.Button(raiz, text="sumador", command=sumar)
contador.pack(side=tk.BOTTOM)

raiz.mainloop() 
"""

"""
import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        
        self.button = ttk.Button(self, text="Hola, mundo!")
        self.button.pack(padx=1, pady=2, ipadx=50, ipady=50)
        
        self.pack()



main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
"""