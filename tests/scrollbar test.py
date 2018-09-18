from tkinter import *
from tkinter.ttk import *

class   Application(Frame): 
    def __init__(self,  master=None):
        Frame.__init__(self, master)    
        self.grid(sticky=N+S+E+W)   
        self.mainframe()

    def mainframe(self):                
        self.data = Listbox(self, bg='red')
        self.scrollbar = Scrollbar(self.data, orient=VERTICAL)
        self.data.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.data.yview)

        for i in range(1000):
            self.data.insert(END, str(i))

        self.run = Button(self, text="run")
        self.stop = Button(self, text="stop")

        self.data.grid(row=0, column=0, rowspan=4,
                       columnspan=2, sticky=N+E+S+W)
        self.data.columnconfigure(0, weight=1)

        self.run.grid(row=4,column=0,sticky=EW)
        self.stop.grid(row=4,column=1,sticky=EW)

        self.scrollbar.grid(column=2, sticky=N+S)

a = Application()
a.mainframe()
a.mainloop()
