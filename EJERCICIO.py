import tkinter
from tkinter import ttk
ventana = tkinter.Tk()


ventana.columnconfigure(0, weight=5)
ventana.columnconfigure(5, weight=5)



label_saludo = ttk.Label(ventana, text="Saludo")
label_saludo.grid(row=0, column=3, sticky=tkinter.N)
lista = ["Opción1", "Opcion2", "Opcion3"]
lista2 = tkinter.StringVar(value = lista)

opcion1 = tkinter.Listbox(ventana, listvariable=lista2)
opcion1.grid(column=3, row=1)
ventana.mainloop()
