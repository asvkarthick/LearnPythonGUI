from tkinter import *
import numpy as np
from PIL import ImageTk, Image

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[:, :, :] = [0, 0, 0]
img = Image.fromarray(data, 'RGB')

root = Tk()
root.title("Create Image")

myImage = ImageTk.PhotoImage(img)
imageLabel = Label(image = myImage)
imageLabel.grid(row = 0, column = 0, columnspan = 3)

def updateImage(var):
    global imageLabel
    global data
    imageLabel.grid_forget()
    data[:, :, 0] = sliderRed.get()
    data[:, :, 1] = sliderGreen.get()
    data[:, :, 2] = sliderBlue.get()
    data = data.astype('uint8')
    img = Image.fromarray(data, 'RGB')
    myImage = ImageTk.PhotoImage(img)
    imageLabel = Label(image = myImage)
    imageLabel.image = myImage
    imageLabel.grid(row = 0, column = 0, columnspan = 3)

sliderRed = Scale(root, from_ = 0, to = 255, command = updateImage)
sliderRed.grid(row = 1, column = 0)
sliderGreen = Scale(root, from_ = 0, to = 255, command = updateImage)
sliderGreen.grid(row = 1, column = 1)
sliderBlue = Scale(root, from_ = 0, to = 255, command = updateImage)
sliderBlue.grid(row = 1, column = 2)

root.mainloop()
