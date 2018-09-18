from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import time,os,json
from PIL import ImageTk

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        #quiz= Questions(**data)



def fileExplore():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select KaYEET Quiz file",filetypes = (("json files","*.json"),("all files","*.*")))
    print (filename)
    loadQuiz(filename)
    
def loadQuiz(filename):
    with open(filename) as x:
        jsonDump = json.loads(x.read())
    global Quiz
    Quiz= Questions(**dict(jsonDump))
    print(Quiz)
        

class QuizGUI:
    def default(self):
        self.sidelist.selection_clear(0, END)
        self.sidelist.selection_set( first = 0 )
        self.titlevar.set(Quiz.questions["Q1"]['question'])
        self.choiceOneVar.set(Quiz.questions["Q1"]['choices'][0])
        self.choiceTwoVar.set(Quiz.questions["Q1"]['choices'][1])
        self.choiceThreeVar.set(Quiz.questions["Q1"]['choices'][2])
        self.choiceFourVar.set(Quiz.questions["Q1"]['choices'][3])
        self.__answersCorrect=0
        for i in range(1,int(Quiz.meta['length'])+1):
            self.sidelist.itemconfig(i-1, {'fg': 'black'})
        self.questionsAnswered=[]
        self.displayQuesiton(self,1)
    
    def __init__(self, master):
        # sidebar
        self.master=master
        sidebar = tk.Frame(master, width=200, bg='#F0F0F0', height=500, relief='sunken', borderwidth=0)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack( side = LEFT, fill = Y )
        self.sidelist = Listbox(sidebar,height=700,width=15,bg="#F0F0F0",fg="#757515",font=("Montserrat",16),selectmode="tk.BROWSE",activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.sidelist.pack(padx=5,pady=50)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Reset", command=self.default)
        menubar.add_cascade(label="File", menu=fileMenu)

        #Main content area
        self.titlevar= StringVar(self.master)
        self.mainarea = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')

        self.errortitlevar= StringVar(self.master)
        self.errortitle = Label(self.mainarea, textvar=self.errortitlevar, bg="#F0F0F0", fg="red",font=('Helvetica Neue',12,"bold"),wraplength=700,pady=5)
        self.errortitle.grid(row=0,column=0,sticky="we",columnspan=4)


        maintitle = Label(self.mainarea, textvar=self.titlevar, bg="#F0F0F0", fg="black",font=('Helvetica Neue',18),wraplength=700,pady=5)
        maintitle.grid(row=1,column=0,sticky="we",columnspan=4)
        self.mainarea.grid_columnconfigure(0, weight=1)
        self.mainarea.grid_columnconfigure(1, weight=1)

        self.choiceFont = font.Font(family="Montserrat", size=24, weight='bold')
        self.choiceWidth= 350
        self.choiceHeight= 200
        self.choicePadX= 10
        self.choicePadY= 10

        self.choiceOneImg=PhotoImage(file="images/tri.png")
        self.choiceOneVar= StringVar(self.master)
        self.choiceOne = Button(self.mainarea,textvar=self.choiceOneVar,relief="flat", bg="#c01733",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(1))
        self.choiceOne.config(image= self.choiceOneImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
        self.choiceOne.grid(row=2,column=0,sticky="W",padx=self.choicePadX, pady=30)

        self.choiceTwoImg=PhotoImage(file="images/dia.png")
        self.choiceTwoVar= StringVar(self.master)
        self.choiceTwo = Button(self.mainarea,textvar=self.choiceTwoVar,relief="flat",  bg="#1368ce",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(2))
        self.choiceTwo.config(image= self.choiceTwoImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
        self.choiceTwo.grid(row=2,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

        self.choiceThreeImg=PhotoImage(file="images/cir.png")
        self.choiceThreeVar= StringVar(self.master)
        self.choiceThree = Button(self.mainarea, textvar=self.choiceThreeVar,relief="flat",  bg="#d89e00", fg="white",width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(3))
        self.choiceThree.config(image= self.choiceThreeImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
        self.choiceThree.grid(row=4,column=0,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

        self.choiceFourImg=PhotoImage(file="images/squ.png")
        self.choiceFourVar= StringVar(self.master)
        self.choiceFour = Button(self.mainarea,image=self.choiceFourImg, textvar=self.choiceFourVar,relief="flat", bg="#298f0d",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(4))
        self.choiceFour.config(image= self.choiceFourImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
        self.choiceFour.grid(row=4,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

        self.skip= Button(self.mainarea, text="Skip",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.skip)
        self.skip.grid(row=5,column=1,sticky="E",padx=self.choicePadX, pady=self.choicePadY)
        
        for i in range(1,int(Quiz.meta['length'])+1):
            self.sidelist.insert(END,"Question "+str(i))
            self.sidelist.bind('<<ListboxSelect>>', self.select)
            self.sidelist.curselection()
        
        self.sidelist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.sidelist.yview)
        self.default()

    def select(self,other):
        a = int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        print("a=",a)
        self.displayQuesiton(self,a)

    def displayQuesiton(self,other=None,Qnum=None):
        print("Qnum ",Qnum)
        self.mainarea.configure(background='#F0F0F0')
        
        if self.isDisabled() == True:
            self.errortitlevar.set("You have already answered this Question!")
            self.choiceOne.configure(state=DISABLED)
            self.choiceTwo.configure(state=DISABLED)
            self.choiceThree.configure(state=DISABLED)
            self.choiceFour.configure(state=DISABLED)
        elif Qnum != None:
            self.errortitlevar.set("")
            self.choiceOne.configure(state=NORMAL)
            self.choiceTwo.configure(state=NORMAL)
            self.choiceThree.configure(state=NORMAL)
            self.choiceFour.configure(state=NORMAL)

        if Qnum == None:
            Qnum= self.getval()
        else:
            pass

        self.titlevar.set(Quiz.questions["Q"+str(Qnum)]['question'])
        self.choiceOneVar.set(Quiz.questions["Q"+str(Qnum)]['choices'][0])
        self.choiceTwoVar.set(Quiz.questions["Q"+str(Qnum)]['choices'][1])
        self.choiceThreeVar.set(Quiz.questions["Q"+str(Qnum)]['choices'][2])
        self.choiceFourVar.set(Quiz.questions["Q"+str(Qnum)]['choices'][3])
    
    def onExit(self):
        self.master.quit()

    def debug(self):
        print("Debugging")

    def getval(self,other=None):
        try:
            return int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        except:
            print("Auto Question")
            

    def answercheck(self,choice):
        getquestionnum= int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        answer= Quiz.questions["Q"+str(getquestionnum)]['answer']
        if answer == choice:
            self.__answersCorrect=self.__answersCorrect+1
            print("Correct:",self.__answersCorrect)
            self.sidelist.itemconfig(getquestionnum-1, {'fg': '#66bf39'})
            self.mainarea.configure(background='#66bf39')
        else:
            print("Incorrect")
            self.sidelist.itemconfig(getquestionnum-1, {'fg': 'red'})
        self.disableQuestion()
        self.next()

    def isDisabled(self):
        if self.getval() in self.questionsAnswered:
            return True
        else:
            return False

    def disableQuestion(self):
        self.questionsAnswered.append(self.getval())
        self.displayQuesiton()

    def skip(self):
        if self.getval() == (int(Quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(Quiz.meta['length'])+1):
            if i not in self.questionsAnswered:
                if i == self.getval():
                    continue
                else:
                    print(i)
                    self.displayQuesiton(Qnum=i)
                    self.sidelist.selection_clear(0, END)
                    self.sidelist.selection_set( first = i-1 )
                    return
    def next(self):
        if len(self.questionsAnswered) == int(Quiz.meta['length']):
            print("Quiz Complete?")
        if self.getval() == (int(Quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(Quiz.meta['length'])+1):
            if i not in self.questionsAnswered:
                if i == self.getval():
                    continue
                else:
                    print(i)
                    self.sidelist.selection_set( first = i-1 )
                    self.displayQuesiton(Qnum=i)
                    self.sidelist.selection_clear(0, END)
                    self.sidelist.selection_set( first = i-1 )
                    return


class Homescreen:
    def __init__(self, master):
        self.master = master
        self.drawUI()

    def drawUI(self):
        self.master.grid_columnconfigure(0, weight=1,uniform="yes")
        self.master.grid_columnconfigure(1, weight=1,uniform="yes")
        self.master.grid_columnconfigure(2, weight=1,uniform="yes")
        self.master.grid_rowconfigure(1,weight=1,uniform="yes")
        self.title = Label(self.master, text="KaYEET", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
        self.title.grid(row=0,column=0,sticky="we",columnspan=3)

        #self.selectedFileVar= StringVar(self.master)
        #self.selectedFile = Label(self.master, textvar=self.selectedFileVar, bg="lightgrey", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=10)
        #self.selectedFile.grid(row=1,column=0,sticky="we",columnspan=3)

        self.sidelist = Listbox(self.master,bg="#F0F0F0",fg="#757515",font=("Montserrat",16),activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.sidelist.config()
        self.sidelist.grid(row=1, column=0, sticky="NSWE",columnspan=3,padx=200,pady=20)
        self.scrollbar = tk.Scrollbar(self.sidelist)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        for i in range(1,10):
            self.sidelist.insert(END,"Quiz "+str(i))
            self.sidelist.curselection()
        
        self.sidelist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.sidelist.yview)

        self.buttonWidth=20
        self.buttonHeight=2
        self.buttonPadY=10
        self.buttonFont= font.Font(family="Montserrat", size=16, weight='bold')
        self.button1 = tk.Button(self.master, text = 'Start', command = self.new_window,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button1.grid(row=3,column=0,pady=self.buttonPadY)
        self.button2 = tk.Button(self.master, text = 'Open', command = self.click,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button2.grid(row=3,column=1,pady=self.buttonPadY)
        self.button3 = tk.Button(self.master, text = 'Create',relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button3.grid(row=3,column=2,pady=self.buttonPadY)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.minsize("1000","700")
        self.newWindow.maxsize("1000","700")
        self.app = QuizGUI(self.newWindow)

    def click(self):
        fileExplore()
    
def init():   
    root = Tk()
    root.minsize("1000","700")
    root.maxsize("1000","700")
    homescreen=Homescreen(root)
    root.mainloop()

init()
