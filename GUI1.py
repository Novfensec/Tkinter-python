#old version import(2.x)
from Tkinter import *

#upgraded version import(3.x)
from tkinter import *

#importing PILLOW for displaying unsupported images
from PIL import Image,ImageTk

root=Tk()

#window default size Width x Height
root.geometry('987x456')

#window title
root.title("Untitled-Notepad")

#window minimum size
root.minsize(787,256)

#window maximum size
root.maxsize(987,456)


#window Icon choice1
img=PhotoImage(file="filename")
root.iconphoto(False,img)

#window Icon choice2 (recommended bitmaps)
root.iconbitmap(r'filename.ico')

#window Icon choice3 (recommended bitmaps)[best way]
root.wm_iconbitmap("filename.ico")


#add text to GUI window with Label widget
#some label attributes
# fg- text color
# bg- background color
# bd- padding
# padx- x axis padding
# pady- y axis padding
# text- adding text
# image- adding image
# font- define font styles
# relief- define border styles
# borderwidth- define border width

txt=Label(root,text="hello this is the first label.",fg="white",bg="grey",padx="44",pady="69",font="comicsansms 19 bold",relief=RAISED,borderwidth="15")    
txt.pack()

#add unsupported image to GUI with PILLOW
newph=Image.open("1.jpeg")
pilimage=ImageTk.PhotoImage(newph)
labeltkimage=Label(root,image=pilimage)
labeltkimage.pack()

#add image to GUI with PhotoImage and Label widgets
photo=PhotoImage(file="new.jpg")
labelph=Label(root,image=photo)
labelph.pack()


root.mainloop()
