from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import time,os,json,glob
from PIL import ImageTk

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        #quiz= Questions(**data)
        

#def fileExplore():
   # filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select KaYEET Quiz file",filetypes = (("json files","*.json"),("all files","*.*")))
    ##print (filename)
    #loadQuiz(filename)
    
#global Quiz
#data = {"meta":{"title":"Computer Quiz","author":"Joshua Boag","length":3},"questions":{"Q1":{"question":"How many Bits are in a Byte?","choices":["8 Bits","2 Bits","6 Bits","4 Bits"],"answer":1},"Q2":{"question":"Where many","choices":["1","2","three","4"],"answer":4},"Q3":{"question":"How much","choices":["one","2","3","4"],"answer":3}}}
#Quiz= Questions(**data)



class QuizGUI:
    def default(self):
        self.sidelist.selection_clear(0, END)
        self.sidelist.selection_set( first = 0 )
        self.titlevar.set(self.__quiz.questions["Q1"]['question'])
        self.choiceOneVar.set(self.__quiz.questions["Q1"]['choices'][0])
        self.choiceTwoVar.set(self.__quiz.questions["Q1"]['choices'][1])
        self.choiceThreeVar.set(self.__quiz.questions["Q1"]['choices'][2])
        self.choiceFourVar.set(self.__quiz.questions["Q1"]['choices'][3])
        self.__answersCorrect=[]
        for i in range(1,int(self.__quiz.meta['length'])+1):
            self.sidelist.itemconfig(i-1, {'fg': 'black'})
        self.questionsAnswered=[]
        self.displayQuesiton(self,1)

    def displayFrame(self):
        if self.itemsPacked == False:
            self.title = Label(self.master, text="KaYEET", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
            self.title.pack(fill="x")
            self.mainarea = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
            self.mainarea.pack(expand=True, fill='both', side='right')

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

            self.choiceOne = Button(self.mainarea,textvar=self.choiceOneVar,relief="flat", bg="#c01733",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(1))
            self.choiceOne.config(image= self.choiceOneImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceOne.grid(row=2,column=0,sticky="W",padx=self.choicePadX, pady=30)

            self.choiceTwo = Button(self.mainarea,textvar=self.choiceTwoVar,relief="flat",  bg="#1368ce",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(2))
            self.choiceTwo.config(image= self.choiceTwoImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceTwo.grid(row=2,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.choiceThree = Button(self.mainarea, textvar=self.choiceThreeVar,relief="flat",  bg="#d89e00", fg="white",width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(3))
            self.choiceThree.config(image= self.choiceThreeImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceThree.grid(row=4,column=0,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.choiceFour = Button(self.mainarea,image=self.choiceFourImg, textvar=self.choiceFourVar,relief="flat", bg="#298f0d",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(4))
            self.choiceFour.config(image= self.choiceFourImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceFour.grid(row=4,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.skip= Button(self.mainarea, text="Skip",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.skip)
            self.skip.grid(row=5,column=0,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.finish= Button(self.mainarea, text="Finish",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.quizComplete)
            self.finish.grid(row=5,column=1,sticky="E",padx=self.choicePadX, pady=self.choicePadY)
            self.itemsPacked= True
        else:
            pass

    def createQuiz(self):
        self.clearMaster()
        self.Quiz={}
        self.Quiz.update({'meta':{'author':"unknown","title":"unknown",'length':1}})
        self.Quiz.update({'questions':{'Q1':{}}})
        self.sidebar = tk.Frame(self.master, width=200, bg='#F0F0F0', height=500, relief='sunken', borderwidth=0)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack( side = LEFT, fill = Y )
        self.createQuizList = Listbox(self.sidebar,height=700,width=15,bg="#F0F0F0",fg="#757515",font=("Montserrat",16),selectmode="tk.BROWSE", exportselection=False,activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.createQuizList.pack(padx=5,pady=50)
        
        self.createdQuestions=1
        self.Qnum=1
        self.mainarea = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')

        self.title = Label(self.mainarea, text="KaYEET Quiz Creator", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
        self.title.grid(row=0,column=0,sticky="we",columnspan=4)

        self.save= Button(self.mainarea, text="Save",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.saveQuestion)
        self.save.grid(row=1,column=1,sticky="E",padx=40, pady=10)

        self.newQuestion= Button(self.mainarea, text="New Question",relief="flat", bg="#46178f", fg="white", width=15,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.createQuizQuestion)
        self.newQuestion.grid(row=1,column=0,sticky="W",padx=40, pady=10)

        self.errortitleVar= StringVar(self.master)
        self.errortitle = Label(self.mainarea, textvar=self.errortitleVar, bg="#F0F0F0", fg="red",font=('Helvetica Neue',12,"bold"),wraplength=400,pady=5)
        self.errortitle.grid(row=2,column=0,columnspan=4,sticky="EWN")

        self.questionTitleVar = StringVar(self.master)
        self.questionTitle = Entry(self.mainarea, textvar=self.questionTitleVar, bg="#F0F0F0", fg="black",font=('Helvetica Neue',18))
        self.questionTitle.grid(row=2,column=0,sticky="we",columnspan=4,padx=40,pady=40,ipady=5,ipadx=5)
        self.mainarea.grid_columnconfigure(0, weight=1)
        self.mainarea.grid_columnconfigure(1, weight=1)
        self.mainarea.grid_rowconfigure(0, weight=0)
        self.mainarea.grid_rowconfigure(1, weight=0)
        self.mainarea.grid_rowconfigure(2, weight=0)
        self.mainarea.grid_rowconfigure(3, weight=2)
        self.mainarea.grid_rowconfigure(4, weight=2)
        self.mainarea.grid_rowconfigure(5, weight=1)

        self.setAnswerVar= tk.IntVar()
        self.setAnswer= tk.Radiobutton(self.mainarea,padx = 0, variable=self.setAnswerVar,value=0)
        self.setAnswer.grid(row=3,column=0,sticky="W")
        self.entryOneVar= StringVar(self.master)
        self.entryOne = Entry(self.mainarea,textvar=self.entryOneVar,relief="flat", bg="lightgrey",fg="black",font=('Helvetica Neue',16))
        self.entryOne.grid(row=3,column=0,sticky="NWES", pady=10,padx=40,ipady=5,ipadx=5)

        self.setAnswer= tk.Radiobutton(self.mainarea,padx = 0, variable=self.setAnswerVar,value=1)
        self.setAnswer.grid(row=3,column=1,sticky="W")
        self.entryTwoVar= StringVar(self.master)
        self.entryTwo = Entry(self.mainarea,textvar=self.entryTwoVar,relief="flat", bg="lightgrey",fg="black",font=('Helvetica Neue',16))
        self.entryTwo.grid(row=3,column=1,sticky="NWES", pady=10,padx=40,ipady=5,ipadx=5)

        self.setAnswer= tk.Radiobutton(self.mainarea,padx = 0, variable=self.setAnswerVar,value=2)
        self.setAnswer.grid(row=4,column=0,sticky="W")
        self.entryThreeVar= StringVar(self.master)
        self.entryThree = Entry(self.mainarea,textvar=self.entryThreeVar,relief="flat",bg="lightgrey",fg="black",font=('Helvetica Neue',16))
        self.entryThree.grid(row=4,column=0,sticky="NWES", pady=10,padx=40,ipady=5,ipadx=5)

        self.setAnswer= tk.Radiobutton(self.mainarea,padx =0, variable=self.setAnswerVar,value=3)
        self.setAnswer.grid(row=4,column=1,sticky="W")
        self.entryFourVar= StringVar(self.master)
        self.entryFour = Entry(self.mainarea,textvar=self.entryFourVar,relief="flat", bg="lightgrey",fg="black",font=('Helvetica Neue',16))
        self.entryFour.grid(row=4,column=1,sticky="NWES", pady=10,padx=40,ipady=5,ipadx=5)

        self.export= Button(self.mainarea, text="Export",relief="flat", bg="#46178f", fg="white", width=15,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.export)
        self.export.grid(row=5,column=1,sticky="E",padx=40, pady=5)

        self.createQuizList.insert(END,"Question 1")
        self.createQuizList.bind('<<ListboxSelect>>', self.createQuizListSelect)

    def export(self):
        self.saveQuestion()
        if self.createdQuestions < 1:
            self.errortitleVar.set("Error! Must have a minimum of 3 Questions!")
            return
        try:
            for i in range(1,self.createdQuestions+1):
                self.Quiz['questions']["Q"+str(i)]['question']
                for x in range(0,4):
                    self.Quiz['questions']["Q"+str(i)]['choices'][x]
        except:
            print(i)
        self.mainarea.pack_forget()
        self.createQuizList.delete(0, END)
        self.createQuizList.insert(END,"Export")
        self.createQuizList.selection_clear(0, END)
        self.createQuizList.selection_set("end")
        self.Quiz["meta"]['length']=self.createdQuestions
        print(self.Quiz)
        self.mainarea = tk.Frame(self.master, background='#F0F0F0', width=900, height=500)
        self.mainarea.pack(expand=True, fill='both', side='right')
        self.mainarea.grid_columnconfigure(0, weight=1)
        self.title = Label(self.mainarea, text="KaYEET Quiz Creator", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
        self.title.grid(row=0,column=0,sticky="we",columnspan=4)
        self.quizNameVar= StringVar(self.master)
        self.quizNameLabel= Label(self.mainarea, text="Quiz Name", bg="#F0F0F0", fg="black",font=('Helvetica Neue',15))
        self.quizNameLabel.grid(row=1,column=0,sticky="W")
        self.quizName = Entry(self.mainarea,textvar=self.entryTwoVar,relief="flat", bg="lightgrey",fg="black",font=('Helvetica Neue',16))
        self.quizName.grid(row=1,column=1,sticky="E", pady=30,padx=40,ipady=5,ipadx=50)
        

    def createQuizListSelect(self,other):
        self.Qnum = int(str(self.createQuizList.get(self.createQuizList.curselection())).split(" ")[1])
        try:
            self.questionTitleVar.set(self.Quiz['questions']["Q"+str(self.Qnum)]['question'])
            self.entryOneVar.set(self.Quiz['questions']["Q"+str(self.Qnum)]['choices'][0])
            self.entryTwoVar.set(self.Quiz['questions']["Q"+str(self.Qnum)]['choices'][1])
            self.entryThreeVar.set(self.Quiz['questions']["Q"+str(self.Qnum)]['choices'][2])
            self.entryFourVar.set(self.Quiz['questions']["Q"+str(self.Qnum)]['choices'][3])
        except:
            self.questionTitleVar.set("Insert Question Here")
            self.entryOneVar.set("")
            self.entryTwoVar.set("")
            self.entryThreeVar.set("")
            self.entryFourVar.set("")
        
    def createQuizQuestion(self):
        if self.entryOneVar.get() == "" or self.entryTwoVar.get() == "" or self.entryThreeVar.get() == "" or self.entryFourVar.get() == "" or self.questionTitleVar.get() == "" or self.questionTitleVar.get() == "Insert Question Here":
            self.saveQuestion()
            return
        else:
            self.createdQuestions=self.createdQuestions+1
            self.Quiz['questions'].update({"Q"+str(self.createdQuestions):{}})
            self.createQuizList.insert(END,"Question "+str(self.createdQuestions))

    def saveQuestion(self):
        self.entryOne.config(bg="lightgrey")
        self.entryTwo.config(bg="lightgrey")
        self.entryThree.config(bg="lightgrey")
        self.entryFour.config(bg="lightgrey")
        self.questionTitle.config(bg="lightgrey")
        print(self.questionTitleVar)
        if self.questionTitleVar.get() == "" or self.questionTitleVar.get() == "Insert Question Here":
            self.errortitleVar.set("Error! Please enter Question!")
            self.questionTitle.config(bg="red")
            return
        if self.entryOneVar.get() == "":
            print("True")
            self.errortitleVar.set("Error! Please enter a option value")
            self.entryOne.config(bg="red")
            return
        if self.entryTwoVar.get() == "":
            self.errortitleVar.set("Error! Please enter a option value")
            self.entryTwo.config(bg="red")
            return
        if self.entryThreeVar.get() == "":
            self.errortitleVar.set("Error! Please enter a option value")
            self.entryThree.config(bg="red")
            return
        if self.entryFourVar.get() == "":
            self.errortitleVar.set("Error! Please enter a option value")
            self.entryFour.config(bg="red")
            return
        self.Quiz['questions'].update({"Q"+str(self.Qnum):{'question':self.questionTitleVar.get()}})
        self.Quiz['questions']["Q"+str(self.Qnum)].update({'choices':[]})
        self.Quiz['questions']["Q"+str(self.Qnum)].update({'answer':self.setAnswerVar.get()})
        self.Quiz['questions']["Q"+str(self.Qnum)]['choices'].append(self.entryOneVar.get())
        self.Quiz['questions']["Q"+str(self.Qnum)]['choices'].append(self.entryTwoVar.get())
        self.Quiz['questions']["Q"+str(self.Qnum)]['choices'].append(self.entryThreeVar.get())
        self.Quiz['questions']["Q"+str(self.Qnum)]['choices'].append(self.entryFourVar.get())
        self.errortitleVar.set("")
        print(self.Quiz)
            

    def quizComplete(self):
        self.menubar.destroy()
        self.sidebar.pack_forget()
        self.scrollbar.pack_forget()
        self.mainarea.pack_forget()

        self.finishFrame= tk.Frame(self.master,width=500, height=500, bg='#F0F0F0', relief='sunken', borderwidth=0)
        self.finishFrame.pack()
        self.finishText= StringVar(self.master)
        finishTitle= Label(self.finishFrame, textvar=self.finishText, bg="#F0F0F0", fg="black",font=('Helvetica Neue',24),wraplength=700,pady=10)
        finishTitle.pack(fill='x')

        c_width = 600
        c_height = 340
        c_linewidth=4
        c_padY=c_width/10
        c_padX=c_width/10
        c_barwidth=c_width/3
        c = Canvas(self.finishFrame, width=c_width, height=c_height,bd=0)
        c.pack()
        print(self.__answersCorrect)
        correct= len(self.__answersCorrect)
        wrong=int(self.meta['meta']['length'])- correct

        graphY1=((c_height/(correct+wrong)))*correct
        graphY2=((c_height/(correct+wrong)))*wrong

        if len(self.questionsAnswered) == 0:
            print("No Questions Answered")
            self.finishText.set("Uhm, did you even try?!")
            graphY1= c_padX+5
            graphY2= c_padX+5
        elif len(self.__answersCorrect) == 0:
            self.finishText.set("Better Luck Nextime!")
            graphY1= c_padX+5
            graphY2= c_height-c_padX
        if len(self.__answersCorrect) == int(self.meta['meta']['length']):            
            print("None Wrong")
            self.finishText.set("Congratulations!")
            graphY1= c_height-c_padX
            graphY2= c_padX
        elif len(self.questionsAnswered) != 0:
            print("Normal")
            self.finishText.set("Well Done!")
        
        c.create_rectangle(c_padX, c_height-graphY1, c_barwidth+c_padX, c_height-c_padY, fill="green",outline="green")
        c.create_text(c_padX+(c_barwidth/2), c_height-graphY1-(c_padY/2), text="Correct: "+str(correct),font=('Helvetica Neue',16,"bold"))
        c.create_rectangle((c_padX*2)+c_barwidth, c_height-graphY2, c_barwidth*2+c_padX*2, c_height-c_padY, fill="red",outline="red")
        c.create_text((c_padX*2)+(c_barwidth*1.5), c_height-graphY2-(c_padY/2), text="Wrong: "+str(wrong),font=('Helvetica Neue',16,"bold"))
        c.create_line(0, c_height-c_padY, c_width, c_height-c_padY,width=4)

        self.resetHome= Button(self.finishFrame, text="Home",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.resetAll)
        self.resetHome.pack()

    def resetAll(self):
        self.itemsPacked= False
        self.finishFrame.destroy()
        self.title.destroy()
        self.sidelist.destroy()
        self.home()

    def clearFrame(self):
        self.itemsPacked= False
        self.mainarea.pack_forget()

    def clearMaster(self):
        self.homescreen.pack_forget()
    
    def __init__(self, master):
        # sidebar
        self.master=master
        self.home()

    def preload(self):
        self.sidebar = tk.Frame(self.master, width=200, bg='#F0F0F0', height=500, relief='sunken', borderwidth=0)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack( side = LEFT, fill = Y )
        self.sidelist = Listbox(self.sidebar,height=700,width=15,bg="#F0F0F0",fg="#757515",font=("Montserrat",16),selectmode="tk.BROWSE",activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.sidelist.pack(padx=5,pady=50)

        self.itemsPacked= False

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        fileMenu = Menu(self.menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Reset", command=self.default)
        fileMenu.add_command(label="Clear Frame", command=self.clearFrame)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        #Main content area
        self.titlevar= StringVar(self.master)
        self.errortitlevar= StringVar(self.master)
        self.choiceOneImg=PhotoImage(file="images/tri.png")
        self.choiceOneVar= StringVar(self.master)

        self.choiceTwoImg=PhotoImage(file="images/dia.png")
        self.choiceTwoVar= StringVar(self.master)
        self.choiceThreeImg=PhotoImage(file="images/cir.png")
        self.choiceThreeVar= StringVar(self.master)
        self.choiceFourImg=PhotoImage(file="images/squ.png")
        self.choiceFourVar= StringVar(self.master)
        for i in range(1,int(self.__quiz.meta['length'])+1):
            self.sidelist.insert(END,"Question "+str(i))
            self.sidelist.bind('<<ListboxSelect>>', self.select)
            self.sidelist.curselection()
        
        self.sidelist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.sidelist.yview)

    def home(self):
        self.homescreen = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
        self.homescreen.pack(expand=True, fill='both', side='right')
        self.homescreen.grid_columnconfigure(0, weight=1,uniform="yes")
        self.homescreen.grid_columnconfigure(1, weight=1,uniform="yes")
        self.homescreen.grid_columnconfigure(2, weight=1,uniform="yes")
        self.homescreen.grid_rowconfigure(1, weight=0,uniform="yes")
        self.homescreen.grid_rowconfigure(2, weight=2,uniform="yes")
        self.homescreen.grid_rowconfigure(3, weight=0,uniform="yes")
        self.homescreen.grid_rowconfigure(4, weight=1,uniform="yes")
        self.title = Label(self.homescreen, text="KaYEET", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
        self.title.grid(row=0,column=0,sticky="we",columnspan=3)

        self.selectedFileVar= StringVar(self.master)
        self.selectedFileVar.set("Select a Built-in Quiz or click 'Open' to Play your Own")
        self.selectedFile = Label(self.homescreen, textvar=self.selectedFileVar, bg="lightgrey", fg="Black",font=('Helvetica Neue',14,"normal"),wraplength=700,pady=10)
        self.selectedFile.grid(row=3,column=0,sticky="we",columnspan=3)

        self.browseQuiz = Listbox(self.homescreen,bg="lightgrey",fg="black",bd=1,height=2,font=("Montserrat",16),activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.browseQuiz.grid(row=2, column=0, sticky="NWES",columnspan=3,padx=150,pady=10,rowspan=1,ipady=10,ipadx=10)
        self.scrollbar = tk.Scrollbar(self.browseQuiz)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        self.metaVar= StringVar(self.master)
        self.meta = Label(self.homescreen, textvar=self.metaVar, bg="lightgrey", fg="Black",font=('Helvetica Neue',14,"normal"),wraplength=700,pady=10)
        self.meta.grid(row=1,column=0,sticky="we",columnspan=3)

        #for i in range(0,len(glob.glob1(os.getcwd(),"*.json"))):
        #os.chdir(os.getcwd())
        for file in glob.glob("*.json"):
            self.browseQuiz.insert(END,file.split(".")[0])
        self.browseQuiz.bind('<<ListboxSelect>>', self.selectQuiz)
        #self.sidelist.curselection()
        
        self.browseQuiz.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.browseQuiz.yview)

        self.buttonWidth=20
        self.buttonHeight=2
        self.buttonPadY=10
        self.buttonFont= font.Font(family="Montserrat", size=16, weight='bold')
        self.button1 = tk.Button(self.homescreen, text = 'Start',state=DISABLED, command = self.startQuiz,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button1.grid(row=4,column=0,pady=self.buttonPadY)
        self.button2 = tk.Button(self.homescreen, text = 'Open', command = self.fileExplore,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button2.grid(row=4,column=1,pady=self.buttonPadY)
        self.button3 = tk.Button(self.homescreen, text = 'Create',command=self.createQuiz,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button3.grid(row=4,column=2,pady=self.buttonPadY)

    def select(self,other):
        a = int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        print("a=",a)
        self.displayQuesiton(self,a)

    def startQuiz(self):
        print(self.filename)
        self.__quiz= Questions(**(json.load(open(self.filename))))
        self.browseQuiz.destroy()
        self.clearMaster()
        self.preload()
        #print(self.filename)
        self.displayFrame()
        self.default()

    def displayQuesiton(self,other=None,Qnum=None):
        print("Qnum ",Qnum)
        self.displayFrame()
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

        self.titlevar.set(self.__quiz.questions["Q"+str(Qnum)]['question'])
        self.choiceOneVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][0])
        self.choiceTwoVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][1])
        self.choiceThreeVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][2])
        self.choiceFourVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][3])
    
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
        answer= self.__quiz.questions["Q"+str(getquestionnum)]['answer']
        if answer == choice:
            self.__answersCorrect.append(getquestionnum)
            print("Correct:",len(self.__answersCorrect))
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
        if self.getval() == (int(self.__quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(self.__quiz.meta['length'])+1):
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
        if len(self.questionsAnswered) == int(self.__quiz.meta['length']):
            self.quizComplete()
        if self.getval() == (int(self.__quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(self.__quiz.meta['length'])+1):
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
    def selectQuiz(self,other):
        #print(self.filename)
        self.button1.config(state=NORMAL)
        try:
            self.filename=str(self.browseQuiz.get(self.browseQuiz.curselection())+".json")
        except:
            pass
        
        self.meta= (json.load(open(str(self.browseQuiz.get(self.browseQuiz.curselection())+".json"))))
        self.metaVar.set("Made by: "+self.meta['meta']['author']+"\tQuestions: "+str(self.meta['meta']['length']))
        self.selectedFileVar.set("Selected: "+str(self.browseQuiz.get(self.browseQuiz.curselection())))


    def fileExplore(self):
        self.metaVar.set("")
        self.selectedFileVar.set("")
        self.browseQuiz.selection_clear(0,END)
        self.filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select KaYEET Quiz file",filetypes = [("KaYEET Quiz Files","*.json")])
        if self.filename: # If correct fuke us sekected
            print("File Selected")
            self.meta= (json.load(open(str(self.filename))))
            self.metaVar.set("Made by: "+self.meta['meta']['author']+"\tQuestions: "+str(self.meta['meta']['length']))
            self.selectedFileVar.set("Selected: "+str(self.filename))
            self.button1.config(state=NORMAL)
        else:
            print("No File Selected")
            self.button1.config(state=DISABLED)
            self.selectedFileVar.set("No File Selected! Try Again!")

def init():   
    root = Tk()
    root.minsize("1000","750")
    root.maxsize("1000","750")
    homescreen=QuizGUI(root)
    root.mainloop()

init()
