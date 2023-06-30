from tkinter import *

def EntrarClick ():
    print ('Has introducido la frase --- ' + fraseEntry.get() + ' --- y has pulsado el botón entrar')

def Button1Click ():
    print ('Has pulsado el botón 1')

window = Tk()
window.geometry("400x400")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

topFrame = LabelFrame (window, text ='Display')
topFrame.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)
topFrame.rowconfigure(0, weight=1)
topFrame.rowconfigure(1, weight=1)
topFrame.columnconfigure(0, weight=1)
topFrame.columnconfigure(1, weight=1)
topFrame.columnconfigure(2, weight=1)

AButton = Button(topFrame, text="A", bg='red', fg="white")
AButton.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)
BButton = Button(topFrame, text="B", bg='yellow', fg="black")
BButton.grid(row=0, column=1, padx=5, pady=5, sticky=N + S + E + W)
CButton = Button(topFrame, text="C", bg='blue', fg="white")
CButton.grid(row=0, column=2, padx=5, pady=5, sticky=N + S + E + W)

fraseEntry = Entry(topFrame)
fraseEntry.grid(row=1, column=0, columnspan = 2, padx=5, pady=5, sticky=N + S + E + W)

EntrarButton = Button(topFrame, text="Entrar", bg='red', fg="white",command=EntrarClick)
EntrarButton.grid(row=1, column=2, padx=5, pady=5, sticky=N + S + E + W)


bottomFrame = LabelFrame (window, text ='Volar')
bottomFrame.grid(row=1, column=0, padx=5, pady=5, sticky=N + S + E + W)

bottomFrame.rowconfigure(0, weight=1)
bottomFrame.rowconfigure(1, weight=1)
bottomFrame.rowconfigure(2, weight=1)
bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)
bottomFrame.columnconfigure(2, weight=1)

Button1 = Button(bottomFrame, text="1", bg='red', fg="white",command=Button1Click)
Button1.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)
Button2 = Button(bottomFrame, text="2", bg='yellow', fg="black")
Button2.grid(row=0, column=1, padx=5, pady=5, sticky=N + S + E + W)
Button3 = Button(bottomFrame, text="3", bg='blue', fg="white")
Button3.grid(row=0, column=2, padx=5, pady=5, sticky=N + S + E + W)
Button4 = Button(bottomFrame, text="4", bg='orange', fg="black")
Button4.grid(row=1, column=0, padx=5, pady=5, sticky=N + S + E + W)

Button5 = Button(bottomFrame, text="5", bg='red', fg="white")
Button5.grid(row=1, column=1, padx=5, pady=5, sticky=N + S + E + W)
Button6 = Button(bottomFrame, text="6", bg='yellow', fg="black")
Button6.grid(row=1, column=2, padx=5, pady=5, sticky=N + S + E + W)
Button7 = Button(bottomFrame, text="7", bg='blue', fg="white")
Button7.grid(row=2, column=0, padx=5, pady=5, sticky=N + S + E + W)
Button8 = Button(bottomFrame, text="8", bg='orange', fg="black")
Button8.grid(row=2, column=1, padx=5, pady=5, sticky=N + S + E + W)
Button9 = Button(bottomFrame, text="9", bg='pink', fg="black")
Button9.grid(row=2, column=2, padx=5, pady=5, sticky=N + S + E + W)


window.mainloop()