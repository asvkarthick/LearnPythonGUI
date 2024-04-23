from tkinter import *
import numpy as np
from PIL import ImageTk, Image

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
# img = Image.fromarray(data, 'RGB')
img = Image.fromarray(data)

root = Tk()
root.title("Display Image")

myImage = ImageTk.PhotoImage(img)
myLabel = Label(image = myImage)
myLabel.pack()

root.mainloop()
