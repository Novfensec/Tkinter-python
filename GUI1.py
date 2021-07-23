#old version import(2.x)
from Tkinter import *

#upgraded version import(3.x)
from tkinter import *

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

root.mainloop()
