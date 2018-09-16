from tkinter import *
from tkinter import ttk
import tkinter as tk

questions= {"1":"Hi","2":"hello"}

root = Tk()
root.minsize("1000","700")
root.maxsize("1000","700");
scrollbar = Scrollbar(root)
s=ttk.Style()
s.theme_use('vista')

class GUI:
    def __init__(self, root):
        # sidebar
        self.root=root
        sidebar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        scrollbar.pack( side = LEFT, fill = Y )
        self.mylist = Listbox(sidebar,height=700,width=20,font=('Helvetica',16),selectmode="tk.BROWSE",)
        self.mylist.pack()
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Debug", command=self.debug)
        menubar.add_cascade(label="File", menu=fileMenu)
        

        # main content area
        mainarea = tk.Frame(root, bg='#CCC', width=500, height=500)
        mainarea.pack(expand=True, fill='both', side='right')


        for question in questions:
            self.mylist.insert(END,question)
            self.mylist.bind('<<ListboxSelect>>', self.getval)

        self.mylist.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.mylist.yview)

    def onExit(self):
        self.root.quit()

    def debug(self):
        print("Debugging")

    def getval(self,other):
        print(str(self.mylist.get(self.mylist.curselection())))

class Questions:
    def __init__(self):
        self.question= "Test"
        
    
app=GUI(root)
root.mainloop()
