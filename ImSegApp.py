# Import required libraries

from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np
import os

#--------------------------------------------------------------------------------------------------

App = Tk()
App.iconbitmap(default='favicon.ico')
App.title("Image Segmentation Tool")
App.geometry("400x400")
#--------------------------------------------------------------------------------------------------

# Functions and Actions



#--------------------------------------------------------------------------------------------------

# Landing Page
landingPage = Frame(App)
landingText = Label(landingPage,text="An Image Segmentation Tool using Tkinter and OpenCV")
selectFolder = Button(landingPage,text="Select Image Folder")
canvas = Canvas(landingPage, width = 300, height = 300)
img = Image.open("Segvizlogo.png")
img = img.resize((300, 300), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)

canvas.create_image(20,20, anchor=NW, image=img)
canvas.pack()
selectFolder.pack(side=BOTTOM,fill=BOTH)
landingText.pack(fill=BOTH,side=BOTTOM)
# landingPage.pack()

#--------------------------------------------------------------------------------------------------


# Image Segmentation Tool
imsegpage = Frame(App)
imsegcanvas = Canvas(imsegpage,width=1000,height=1000,scrollregion=(0,0,1000,1000))

# Scrollbars for Image
scroll_x = Scrollbar(App, orient="horizontal", command=canvas.xview)
scroll_y = Scrollbar(App, orient="vertical", command=canvas.yview)
imsegcanvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

# Tab Control
tabControl = ttk.Notebook(App)
tab1 = ttk.Frame(tabControl)
selectcolor = Button(tab1,text="Select Color")
save = Button(tab1,text="Save Segmentation")
tabControl.add(tab1, text='Tools')

selectcolor.pack(fill=BOTH)
save.pack(fill=BOTH)
tabControl.pack(side=LEFT,fill=Y)

#--------------------------------------------------------------------------------------------------

imsegcanvas.pack()
imsegpage.pack(fill=BOTH)


mainloop()