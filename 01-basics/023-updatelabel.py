from tkinter import *

root = Tk()
root.title("Update label")
root.geometry("400x400")

e = Entry(root, width = 50, font = ('Helvetica', 30))
e.pack(padx = 10, pady = 10)

def delete():
    label.pack_forget()
    button1['state'] = NORMAL
    

def click():
    global label
    txt = "Hello " + e.get()
    label = Label(root, text = txt)
    e.delete(0, 'end')
    label.pack(pady = 10)
    button1['state'] = DISABLED
    
button1 = Button(root, text = "Enter a name", command = click)
button2 = Button(root, text = "Delete", command = delete)
button1.pack()
button2.pack()

root.mainloop()
