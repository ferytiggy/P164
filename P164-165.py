# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:59:51 2024

@author: Aidan
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Proyecto 164-165")
root.configure(background = "black")
root.geometry("600x600")

abrir = Button(root, text="abrir imagen", bg="white")
abrir.place(relx=0.5, rely=0.1, anchor=CENTER)

imagen = Label(root, bg="white", highlightthickness=5)
imagen.place(relx=0.5, rely=0.5, anchor=CENTER)

rotar = Label(root, text="rotar imagen", bg="white")
rotar.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()