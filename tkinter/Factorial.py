"""from itertools import product
import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title("Factorial")
root.geometry('500x250')


 Factorial de un numero negativo?
Factorial de 0=1
Factorial de 1=1


def sumar():
    numero.set(str(int(numero.get()) + 1))
    return numero

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:           
            resultado=n*factorial(n-1)
   return resultado

label = tk.Label (root, text='n')
label.place(x=50, y=100) 

numero = tk.StringVar(root, "0")
num = tk.Entry(root, textvariable= numero)
num.config(state="disabled")
num.place(x=75,y=100)

label2 = tk.Label (root, text='Factorial (n)')
label2.place(x=200, y=100) 



botonnext = ttk.Button(root, text="siguiente", command= sumar)
botonnext.place(x=400,y=100)

root.mainloop() 


from tkinter import *

class Factorial():
    def __init__(self):
        self.root = Tk()
        self.root.title("Factorial")
        self.root.geometry("500x100")
        self.miFrame = Frame(self.root)
        self.miFrame.pack()

        self.n1 = IntVar(value=0)
        self.n2 = StringVar()

        self.lb1 = Label(self.miFrame, text="n")
        self.lb1.grid(row=0, column=0)
        self.txt1 = Entry(self.miFrame, textvariable=self.n1)
        self.txt1.grid(row=0, column=1)
        self.lb2 = Label(self.miFrame, text="Factorial (n)")
        self.lb2.grid(row=0, column=2)
        self.txt2 = Entry(self.miFrame, textvariable=self.n2)
        self.txt2.grid(row=0, column=3)
        self.btn = Button(self.miFrame, text="Siguiente", width=10, command=self.num_factorial)
        self.btn.grid(row=0, column=4)

        self.root.mainloop()

    def num_factorial(self):
        self.n1.set(self.n1.get() + 1)
        fact = 1
        for i in range(1, (self.n1.get()) + 1):
            fact = fact * i
            self.n2.set(fact)

    def main():
        f = Factorial()
        return 0
    if __name__ == "__main__":
        main()
"""
import tkinter as tk
import math

# Función para calcular el factorial y mostrarlo en el segundo Entry
def calcular_factorial():
    try:
        n = int(entry_n.get())
        factorial = math.factorial(n)
        entry_factorial.delete(0, tk.END)  # Borra el contenido anterior
        entry_factorial.insert(0, str(factorial))
    except ValueError:
        entry_factorial.delete(0, tk.END)
        entry_factorial.insert(0, "Error: Ingresa un número entero válido")

# Función para avanzar al siguiente número
def siguiente():
    n = int(entry_n.get())
    n += 1
    entry_n.delete(0, tk.END)
    entry_n.insert(0, str(n))
    calcular_factorial()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Factorial")

# Etiqueta para "n"
label_n = tk.Label(ventana, text="n:")
label_n.pack()

# Entry (LineEdit) para "n"
entry_n = tk.Entry(ventana)
entry_n.pack()
entry_n.insert(0, "1")  # Inicialmente, n es 1

# Etiqueta para "Factorial (n)"
label_factorial = tk.Label(ventana, text="Factorial (n):")
label_factorial.pack()

# Entry (LineEdit) para "Factorial (n)" (no editable)
entry_factorial = tk.Entry(ventana)
entry_factorial.pack()

# Botón "Siguiente"
boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente)
boton_siguiente.pack()

# Botón "Calcular Factorial"
boton_calcular = tk.Button(ventana, command=calcular_factorial)


# Inicialmente, calcula el factorial para n=1
calcular_factorial()

ventana.mainloop()
