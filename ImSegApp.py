#--------------------------------------------------------------------------------------------------
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

global array
global array2
global array3
array=[]
array2=[]
array3=[]

#--------------------------------------------------------------------------------------------------

App = Tk()
App.iconbitmap(default='favicon.ico')
App.title("Image Segmentation Tool")
App.geometry("400x400")

#--------------------------------------------------------------------------------------------------

# Functions and Actions

def selectfolder():
    global filename
    filename = filedialog.askdirectory()
    isFile=os.path.isdir(filename + "/" + "Segmentation")
    if(not isFile):
        os.mkdir(filename + "/" + "Segmentation")
    print(filename)
    for r, d, files in os.walk(filename):
        for file in files:
            directoryview.insert(END,file)
    landingPage.destroy()
    App.geometry("{0}x{1}+0+0".format(App.winfo_screenwidth()-20, App.winfo_screenheight()-80))
    App.resizable(0,0)
    imsegpage.pack(fill=BOTH)




def showimg(event):
    n = directoryview.curselection()
    global fname,img,segmap
    fname = directoryview.get(n)
    imsegcanvas.delete("all")
    imgpath=filename+"/"+fname
    img = Image.open(imgpath)
    imgwidth, imgheight = img.size
    # img = img.resize((300, 300), Image.ANTIALIAS)

    # Segmentation Map
    segmap = np.zeros((imgheight, imgwidth, 3), np.uint8)
    img = ImageTk.PhotoImage(img)
    imsegcanvas.config(width=imgwidth,height=imgheight,scrollregion=(0,0,imgwidth,imgheight))
    imsegcanvas.create_image(0,0, anchor=NW, image=img)




def choose_color():
    global color_code
    global clf
    clf = colorchooser.askcolor(title="Choose color")
    color_code=clf[1]
    print(color_code)




def point(event):
    try:
        x1, y1 = (imsegcanvas.canvasx(event.x) - 1), (imsegcanvas.canvasy(event.y) - 1)
        imsegcanvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="#ff0000")
        array.append(x1)
        array.append(y1)
        array2.append([x1, y1])
    except:
        messagebox.showerror("Error", "Error Occured")




def clearcanvas(event):
    imsegcanvas.delete("all")
    imsegcanvas.create_image(0, 0, anchor=NW, image=img)
    imsegcanvas.image = img
    messagebox.showinfo("Message", "Segmap Cleared")




def genpolygon(event):
    try:
        imsegcanvas.create_polygon(array, outline=color_code, fill=color_code, width=3, stipple="gray50")
        pts = np.array(array2, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(segmap, [pts], [clf[0][2],clf[0][1],clf[0][0]], 1)
        array2.clear()
        array.clear()
    except:
        messagebox.showerror("Error", "Error Occured")




def outline(event):
    try:
        x1, y1 = (imsegcanvas.canvasx(event.x) - 1), (imsegcanvas.canvasy(event.y) - 1)
        imsegcanvas.create_oval(x1 - 1, y1 - 1, x1 + 1, y1 + 1, fill="#ff0000")
        array.append(x1)
        array.append(y1)
        array2.append([x1, y1])
    except:
        messagebox.showerror("Error", "Error Occured")




def save():
    print(filename+"/Segmentation/"+fname)
    cv2.imwrite(filename+"/Segmentation/"+fname, segmap)
    messagebox.showinfo("Message", "Image Saved")


# def bbox(event):
#     if len(array3)>=3:
#         imsegcanvas.create_rectangle(array3[0],array3[1],array3[2],array3[3],fill="")
#         array3.clear()
#     x1, y1 = (imsegcanvas.canvasx(event.x) - 1), (imsegcanvas.canvasy(event.y) - 1)
#     imsegcanvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="#ff0000")
#     array3.append(x1)
#     array3.append(y1)

#--------------------------------------------------------------------------------------------------

# Landing Page
global landingPage
landingPage = Frame(App)
landingText = Label(landingPage,text="An Image Segmentation Tool using Tkinter and OpenCV")
selectFolder = Button(landingPage,text="Select Image Folder",command=selectfolder)
canvas = Canvas(landingPage, width = 300, height = 300)
imgland = Image.open("Segvizlogo.png")
imgland = imgland.resize((300, 300), Image.ANTIALIAS)
imgland=ImageTk.PhotoImage(imgland)

canvas.create_image(20,20, anchor=NW, image=imgland)
canvas.pack()
selectFolder.pack(side=BOTTOM,fill=BOTH)
landingText.pack(fill=BOTH,side=BOTTOM)
landingPage.pack()

#--------------------------------------------------------------------------------------------------


# Image Segmentation Tool
global imsegpage
global canvasimage
global imsegcanvas
global imageoncanvas
global wt,ht


imsegpage = Frame(App)
currentimage=Image.open("segvizbg.png")
currentimage=currentimage.resize((250, 250), Image.ANTIALIAS)
wt,ht=currentimage.size
imsegcanvas = Canvas(imsegpage,width=wt,height=ht)
canvasimage = ImageTk.PhotoImage(currentimage)
imsegcanvas.create_image(0,0, anchor=NW, image=canvasimage)



# List Box for files
global directoryview
directoryview=Listbox(imsegpage)
directoryview.bind("<<ListboxSelect>>", showimg)
directoryview.pack(side="left", fill=Y,expand=False)

# Scrollbars for Image
scroll_x = Scrollbar(imsegpage, orient="horizontal", command=imsegcanvas.xview)
scroll_y = Scrollbar(imsegpage, orient="vertical", command=imsegcanvas.yview)
imsegcanvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

# Tab Control
tabControl = ttk.Notebook(imsegpage)
tab1 = ttk.Frame(tabControl)
selectcolor = Button(tab1,text="Select Color",command=choose_color)
save = Button(tab1,text="Save Segmentation",command=save)
tabControl.add(tab1, text='Tools')

# Pack the widgets
selectcolor.pack(fill=BOTH)
save.pack(fill=BOTH)
tabControl.pack(side=TOP,fill=X)

# Bind the canvas actions

imsegcanvas.bind("<Double-1>",point)
# imsegcanvas.bind("<Button-1>",bbox)
imsegcanvas.bind("<Button-3>",genpolygon)
imsegcanvas.bind("<B1-Motion>",outline)
imsegcanvas.bind("<Button-2>",clearcanvas)

#--------------------------------------------------------------------------------------------------

imsegcanvas.pack()


App.mainloop()