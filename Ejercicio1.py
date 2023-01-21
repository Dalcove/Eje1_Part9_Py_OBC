from tkinter import ttk

import tkinter
window = tkinter.Tk()

def reiniciar(event):
    selected.set(None)
    monitor.config(text="")



monitor = tkinter.Label(window)
boton = tkinter.Button(window, text="Reiniciar")

window.columnconfigure(0, weight=1)
window.columnconfigure(1,weight=3)

selected = tkinter.StringVar()
selected.set(None)


r1 = ttk.Radiobutton(window,text="Uno", value=1, variable=selected)
r2 = ttk.Radiobutton(window,text="Dos", value=2, variable=selected)
r3 = ttk.Radiobutton(window,text="Tres", value=3, variable=selected)
r4 = ttk.Radiobutton(window,text="Cuatro", value=4, variable=selected)



r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)
r4.grid(column=0, row=4, pady=5, padx=5)


boton.grid(column=1, row=5)
monitor.grid(column= 1, row=6)

boton.bind("<Button-1>", reiniciar)

window.mainloop()
