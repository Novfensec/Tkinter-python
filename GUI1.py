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

#window maximum size
root.minsize(787,256)

#window minimum size
root.maxsize(987,456)


#window Icon choice1
img=PhotoImage(file="filename")
root.iconphoto(False,img)

#window Icon choice2 (recommended bitmaps)
root.iconbitmap(r'filename.ico')

#window Icon choice3 (recommended bitmaps)[best way]
root.wm_iconbitmap("filename.ico")


#add text to GUI window with Label widget
txt=Label(root,text="This is the first Label in this GUI! Please subscribe!")
text.pack()

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
