from tkinter import *
from tkinter import ttk
import tkinter as tk

data= {"meta":{"title":"Computer Quiz","author":"Joshua Boag","length": 3},"questions":{"Q1":{"question":"How many Bits are in a Byte?","choices":["1","2","3","4"]},"Q2":{"question":"Where many","choices":["1","2","three","4"]},"Q3":{"question":"How much","choices":["one","2","3","4"]}}}

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
quiz= Questions(**data)

class GUI:
    def __init__(self, root):
        # sidebar
        self.root=root
        sidebar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        scrollbar.pack( side = LEFT, fill = Y )
        self.sidelist = Listbox(sidebar,height=700,width=20,font=('Helvetica',16),selectmode="tk.BROWSE",)
        self.sidelist.pack()
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Debug", command=self.debug)
        menubar.add_cascade(label="File", menu=fileMenu)
        

        # main content area
        self.titlevar= StringVar(self.root)
        mainarea = tk.Frame(root, bg='#CCC', width=500, height=500)
        mainarea.pack(expand=True, fill='both', side='right')
        maintitle = Label(mainarea, textvar=self.titlevar, bg="red", fg="white",font=('Helvetica',18),wraplength=700)
        maintitle.grid(row=1,column=0,sticky="we",columnspan=4)
        mainarea.grid_columnconfigure(0, weight=1)
        mainarea.grid_columnconfigure(1, weight=1)

        self.choiceOne = Button(mainarea, text="Choice 1",relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'))
        self.choiceOne.grid(row=2,column=0,sticky="W",padx=20, pady=30)

        self.choiceTwo = Button(mainarea, text="Choice 2",relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'))
        self.choiceTwo.grid(row=2,column=1,sticky="W",padx=20, pady=30)

        self.choiceThree = Button(mainarea, text="Choice 3",relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'))
        self.choiceThree.grid(row=4,column=0,sticky="W",padx=20, pady=30)

        self.choiceFour = Button(mainarea, text="Choice 4",relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'))
        self.choiceFour.grid(row=4,column=1,sticky="W",padx=20, pady=30)

        for i in range(1,int(quiz.meta['length'])+1):
            self.sidelist.insert(END,"Question "+str(i))
            self.sidelist.bind('<<ListboxSelect>>', self.getval)

        self.sidelist.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.sidelist.yview)

    def onExit(self):
        self.root.quit()

    def debug(self):
        print("Debugging")

    def getval(self,other):
        getquestionnum= int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        print(getquestionnum)
        self.titlevar.set(quiz.questions["Q"+str(getquestionnum)]['question'])


root = Tk()
root.minsize("1000","700")
root.maxsize("1000","700");
scrollbar = Scrollbar(root)
s=ttk.Style()
s.theme_use('vista')

app=GUI(root)
root.mainloop()
