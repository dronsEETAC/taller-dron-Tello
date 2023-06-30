
from tkinter import *

def EntrarClick ():
    print ('Has introducido la frase --- ' + fraseEntry.get() + ' --- y has pulsado el botón entrar')

def AClick ():
    print ('Has pulsado el botón A')

window = Tk()
window.geometry("400x400")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

tituloLabel = Label(window, text = "Mi programa", font=("Courier", 20, "italic"))
tituloLabel.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky=N + S + E + W)

fraseEntry = Entry(window)
fraseEntry.grid(row=1, column=0, columnspan = 3, padx=5, pady=5, sticky=N + S + E + W)

EntrarButton = Button(window, text="Entrar", bg='red', fg="white",command=EntrarClick)
EntrarButton.grid(row=1, column=3, padx=5, pady=5, sticky=N + S + E + W)

AButton = Button(window, text="A", bg='red', fg="white",command=AClick)
AButton.grid(row=2, column=0, padx=5, pady=5, sticky=N + S + E + W)
BButton = Button(window, text="B", bg='yellow', fg="black")
BButton.grid(row=2, column=1, padx=5, pady=5, sticky=N + S + E + W)
CButton = Button(window, text="C", bg='blue', fg="white")
CButton.grid(row=2, column=2, padx=5, pady=5, sticky=N + S + E + W)
DButton = Button(window, text="D", bg='orange', fg="black")
DButton.grid(row=2, column=3, padx=5, pady=5, sticky=N + S + E + W)

window.mainloop()