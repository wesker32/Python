
import tkinter, tkinter.font


def calcular(*args):
    try:
        valor = float(feet.get())
        novovalor = valor/ 3.5
        novovalor = "{:8.2f}".format(novovalor)
        var.set(novovalor)
        novovalor2 = valor / 5
        novovalor2 = "{:8.2f}".format(novovalor2)
        var2.set(novovalor2)
        statusLabel.config(text="Nada a declarar")
    except ValueError as e:
        statusLabel.config(text="Entrada apenas com numeros")
    feet_entry.focus()




root = tkinter.Tk()
root.title("Conversão")

customFont = tkinter.font.Font(
    family="Courier",
    weight="bold",
    underline=False,
    overstrike=False,
    slant="italic",
    size=24)

mainframe = tkinter.Frame(root, background='gray')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = tkinter.StringVar()
var = tkinter.StringVar()
var2 = tkinter.StringVar()

feet_entry = tkinter.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=1, row=0, sticky=(tkinter.W, tkinter.E))

tkinter.Label(mainframe, textvariable=var).grid(column=1, row=1, sticky=(tkinter.W, tkinter.E))
tkinter.Label(mainframe, text="Real$",
              font=customFont,
              foreground='orange',
              background='Gray',
              ).grid(column=2, row=0, sticky=tkinter.W)
tkinter.Label(mainframe, text="E equivalente ",
              background='white'
              ).grid(column=0, row=1, sticky=tkinter.E)
tkinter.Label(mainframe, text="Dolar$",
              font=customFont,
              foreground='orange',
              background='Gray',
              ).grid(column=2, row=1, sticky=(tkinter.E, tkinter.W))

tkinter.Label(mainframe, textvariable=var2).grid(column=1, row=2, sticky=(tkinter.W, tkinter.E))
tkinter.Button(mainframe, text="Calcular", command=calcular,
               foreground='white',
               background='red',
               activeforeground='green',
               highlightbackground='blue',
               highlightcolor='pink',
               ).grid(column=1, row=3, sticky=tkinter.W)


tkinter.Label(mainframe, text="E equivalente ",
              background='white'
              ).grid(column=0, row=2, sticky=tkinter.E)
tkinter.Label(mainframe, text="Euro$",
              font=customFont,
              foreground='orange',
              background='Gray',
              ).grid(column=2, row=2, sticky=(tkinter.E, tkinter.W))
statusLabel = tkinter.Label(mainframe, text="Aviso",)
statusLabel.grid(column=1, row=4)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calcular)
root.resizable(0, 0)
root.mainloop()
