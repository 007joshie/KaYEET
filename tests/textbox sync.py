from tkinter import *

def callback(sv):
    print(sv.get())

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)


tv = StringVar()
tv.trace("w", lambda name, index, mode, tv=tv: callback(tv))
e1 = Entry(root, textvariable=tv)
e.pack()
e1.pack()
root.mainloop()  
