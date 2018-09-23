from tkinter import *


root = Tk()
root.title("Bar Graph")

c_width = 600
c_height = 400
c_linewidth=4
c_padY=c_width/10
c_padX=c_width/10
c_barwidth=c_width/3
c = Canvas(root, width=c_width, height=c_height)
c.pack()

correct=0
wrong=0

graphY1=((c_height/(correct+wrong)))*correct
graphY2=((c_height/(correct+wrong)))*wrong

c.create_rectangle(c_padX, c_height-graphY1, c_barwidth+c_padX, c_height-c_padY, fill="green")
c.create_text(c_padX+(c_barwidth/2), c_height-graphY1-(c_padY/4), text="Correct: "+str(correct),font=('Helvetica Neue',12,"bold"))



c.create_rectangle((c_padX*2)+c_barwidth, c_height-graphY2, c_barwidth*2+c_padX*2, c_height-c_padY, fill="red")
c.create_text((c_padX*2)+(c_barwidth*1.5), c_height-graphY2-(c_padY/4), text="Wrong: "+str(wrong),font=('Helvetica Neue',12,"bold"))


c.create_line(0, c_height-c_padY, c_width, c_height-c_padY,width=4)
