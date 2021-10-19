from tkinter import *
import os
#from tkinter import ttk
#from main import *

cls = lambda: os.system("cls")
cls()

def push(variable):
    """ funcion para obtener el contenido ingresado por el usuario """
    #print(entrada.get())
    obtener = variable.get()
    print(obtener)
    resultado["text"] = obtener

def mostrar_resultado(variable):
    """ funcion para mostrar el resultado """
    pass
    #resultado["text"] = 


raiz = Tk()
raiz.geometry('500x350')        # anchura x altura
raiz.resizable(width = False, height = False)       # impide aumentar dimenciones 
raiz.configure(bg = 'beige')    # background
raiz.title('CONVERSOR DE BASES')


boton_salir = Button(raiz, text = 'Salir',
            width = 15,
            command = raiz.destroy).grid(row=45, column=4)
    

entrada = Entry(raiz)
#entrada.pack(padx= 20, pady=20)
entrada.grid(row= 14, column= 2)

boton_commit = Button(raiz, text= "Click",
                    width = 5,
                    command = lambda: push(entrada))#.pack()


resultado = Label(text = "resultado", font= ("Georgia", 15, "normal"))
resultado.grid(row= 14, column=3, padx = 30, pady = 30)

raiz.mainloop()








