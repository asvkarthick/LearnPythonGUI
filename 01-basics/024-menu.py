from tkinter import *

root = Tk()
root.title("Menu demo")
root.geometry("400x400")

myMenu = Menu(root)
root.config(menu=myMenu)

def cmd():
    pass

fileMenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu = fileMenu)
fileMenu.add_command(label = "New", command = cmd)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = root.quit)

root.mainloop()
