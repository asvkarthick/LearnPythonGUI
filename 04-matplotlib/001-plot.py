from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Matplotlib demo")
root.geometry("400x400")

def plot():
    data = np.random.normal(250000, 50000, 500)
    plt.hist(data, 50)
    plt.show()
    
Button(root, text="Plot", command=plot).pack()

root.mainloop()
