from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
import os

App = Tk()
App.iconbitmap(default='favicon.ico')
App.title("Image Segmentation Tool")
App.geometry("400x400")

landingPage=Frame(App)

landingText=Label(text="An Image Segmentation Tool using Tkinter and OpenCV")
selectFolder=Button(text="Select Image Folder")
canvas = Canvas(landingPage, width = 300, height = 300)
img = Image.open("Segvizlogo.png")
img = img.resize((300, 300), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
canvas.create_image(20,20, anchor=NW, image=img)
canvas.pack()
selectFolder.pack(side=BOTTOM,fill=BOTH)
landingText.pack(fill=BOTH,side=BOTTOM)
landingPage.pack()

mainloop()