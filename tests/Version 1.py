from tkinter import *
from tkinter import ttk
import tkinter as tk

data= {"meta":{"title":"Computer Quiz","author":"Joshua Boag","length": 3},"questions":{"Q1":{"question":"How many Bits are in a Byte?","choices":["8 Bits","2 Bits","6 Bits","4 Bits"],"answer":1},"Q2":{"question":"Where many","choices":["1","2","three","4"],"answer":4},"Q3":{"question":"How much","choices":["one","2","3","4"],"answer":3}}}

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
quiz= Questions(**data)

def default(e):
    e.sidelist.selection_set( first = 0 )
    e.getval(e)
    e.titlevar.set(quiz.questions["Q1"]['question'])
    e.choiceOneVar.set(quiz.questions["Q1"]['choices'][0])
    e.choiceTwoVar.set(quiz.questions["Q1"]['choices'][1])
    e.choiceThreeVar.set(quiz.questions["Q1"]['choices'][2])
    e.choiceFourVar.set(quiz.questions["Q1"]['choices'][3])

class GUI:
    def __init__(self, root):
        self.__answersCorrect=0
        self.questionsAnswered=[]
        
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

        self.choiceOneVar= StringVar(self.root)
        self.choiceOne = Button(mainarea, textvar=self.choiceOneVar,relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'),command=lambda: self.answercheck(1))
        self.choiceOne.grid(row=2,column=0,sticky="W",padx=20, pady=30)

        self.choiceTwoVar= StringVar(self.root)
        self.choiceTwo = Button(mainarea,textvar=self.choiceTwoVar,relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'),command=lambda: self.answercheck(2))
        self.choiceTwo.grid(row=2,column=1,sticky="W",padx=20, pady=30)

        self.choiceThreeVar= StringVar(self.root)
        self.choiceThree = Button(mainarea, textvar=self.choiceThreeVar,relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'),command=lambda: self.answercheck(3))
        self.choiceThree.grid(row=4,column=0,sticky="W",padx=20, pady=30)

        self.choiceFourVar= StringVar(self.root)
        self.choiceFour = Button(mainarea, textvar=self.choiceFourVar,relief="groove", bg="white", fg="#306bff", width=35,height=10, highlightcolor="red", font=('Roboto', '12'),command=lambda: self.answercheck(4))
        self.choiceFour.grid(row=4,column=1,sticky="W",padx=20, pady=30)

        for i in range(1,int(quiz.meta['length'])+1):
            self.sidelist.insert(END,"Question "+str(i))
            self.sidelist.bind('<<ListboxSelect>>', self.displayQuesiton)

        self.sidelist.curselection()
        
        self.sidelist.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.sidelist.yview)

    def displayQuesiton(self,other=None):
        if self.isDisabled() == True:
            self.choiceOne.configure(state=DISABLED)
            self.choiceTwo.configure(state=DISABLED)
            self.choiceThree.configure(state=DISABLED)
            self.choiceFour.configure(state=DISABLED)
        else:
            self.choiceOne.configure(state=NORMAL)
            self.choiceTwo.configure(state=NORMAL)
            self.choiceThree.configure(state=NORMAL)
            self.choiceFour.configure(state=NORMAL)

        Qnum= self.getval()
        self.titlevar.set(quiz.questions["Q"+str(Qnum)]['question'])
        self.choiceOneVar.set(quiz.questions["Q"+str(Qnum)]['choices'][0])
        self.choiceTwoVar.set(quiz.questions["Q"+str(Qnum)]['choices'][1])
        self.choiceThreeVar.set(quiz.questions["Q"+str(Qnum)]['choices'][2])
        self.choiceFourVar.set(quiz.questions["Q"+str(Qnum)]['choices'][3])
    
    def onExit(self):
        self.root.quit()

    def debug(self):
        print("Debugging")

    def getval(self,other=None):
        return int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])

    def answercheck(self,choice):
        getquestionnum= int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        answer= quiz.questions["Q"+str(getquestionnum)]['answer']
        if answer == choice:
            self.__answersCorrect=self.__answersCorrect+1
            print("Correct",self.__answersCorrect)
            self.sidelist.itemconfig(getquestionnum-1, {'fg': 'green'})
        else:
            print("Incorrect")
            self.sidelist.itemconfig(getquestionnum-1, {'fg': 'red'})
        self.disableQuestion()

    def isDisabled(self):
        if self.getval() in self.questionsAnswered:
            return True
        else:
            return False

    def disableQuestion(self):
        self.questionsAnswered.append(self.getval())
        self.displayQuesiton()
        
        
root = Tk()
root.minsize("1000","700")
root.maxsize("1000","700");
scrollbar = Scrollbar(root)
s=ttk.Style()
s.theme_use('vista')

app=GUI(root)
default(app)
root.mainloop()
