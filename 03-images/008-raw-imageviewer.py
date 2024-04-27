from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
from PIL import ImageTk, Image

root = Tk()
root.title("RAW Image Viewer")
root.geometry("800x600")
root.filename = ""

def openFile():
    global image
    global fileLabel
    root.filename = filedialog.askopenfilename(initialdir="./data/", title="Select a raw file")
    fileLabel.grid_forget()
    fileLabel = Label(root, text = root.filename)
    fileLabel.grid(row = 0, column = 1, columnspan = 3)
    widthInput.focus_set()

def showImage():
    if widthInput.get() == "":
        messagebox.showerror("Please set the width", "Please set the width")
        return
    elif heightInput.get() == "":
        messagebox.showerror("Please set the height", "Please set the height")
        return
    elif root.filename == "":
        messagebox.showerror("Please select the file", "Please select the file")
        return
    elif format.get() == "":
        messagebox.showerror("Please select the format", "Please selsect the format")
        return
    width = int(widthInput.get())
    height = int(heightInput.get())
    if root.filename != "":
        if format.get() == "RAW8":
            data = np.fromfile(root.filename, dtype='uint8').reshape(height, width)
        elif format.get() == "RAW10":
            tmpwidth = int(width * 10 / 8)
            tmpheight = int(height * tmpwidth / 5)
            data = np.fromfile(root.filename, dtype='uint8')
            data = data.reshape(tmpheight, 5)
            data = data[:, :4]
            data = data.reshape(height, width)
        img = Image.fromarray(data, mode = 'L')
        image = ImageTk.PhotoImage(img)
        imageLabel = Label(image = image, width = 640, height = 480)
        imageLabel.image = image
        imageLabel.grid(row = 3, column = 0, columnspan = 4)
    else:
        messagebox.showinfo("Please select the file", "Please select the file")

def executeOption(v):
    showImage()

openButton = Button(root, text = "Select file", command = openFile)
openButton.grid(row = 0, column = 0)
fileLabel = Label(root, text = root.filename)
fileLabel.grid(row = 0, column = 1, columnspan = 3)

widthLabel = Label(root, text = "Width")
widthLabel.grid(row = 1, column = 0)
widthInput = Entry(root, width = 10)
widthInput.grid(row = 1, column = 1)
heightLabel = Label(root, text = "Height")
heightLabel.grid(row = 1, column = 2)
heightInput = Entry(root, width = 10)
heightInput.grid(row = 1, column = 3)
formatLabel = Label(root, text = "Format")
formatLabel.grid(row = 2, column = 0)

formatOptions = [
        "RAW8",
        "RAW10"
]
format = StringVar()
formatDropdown = OptionMenu(root, format, *formatOptions, command = executeOption)
formatDropdown.grid(row = 2, column = 1)
# widthInput.focus_set()
formatDropdown.focus_set()

root.mainloop()
