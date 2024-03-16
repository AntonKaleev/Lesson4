from tkinter import *
root = Tk()
myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text = "Меня зовут Антон Калеев")
myLabel2.grid(row=1, column=6)
root.mainloop()
