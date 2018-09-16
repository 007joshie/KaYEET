from tkinter import *
from tkinter import ttk
import tkinter as tk


class App:
    numdigs = 0
    def __init__(self, root):
        frame = Frame(root)
        grid=Frame(frame)
        b = Label(root, text="This should be in center")
        b.grid(row=0, column=1, columnspan=2)
        b = Button(root, text="1", width=10, command= lambda *args: self.setVar(1))
        b.grid(row=1, column=0)
        b = Button(root, text="2", width=10,command= lambda *args: self.setVar(2))
        b.grid(row=1, column=1,)
        b = Button(root, text="3", width=10,command= lambda *args: self.setVar(3))
        b.grid(row=1, column=2,)
        b = Button(root, text="4", width=10,command= lambda *args: self.setVar(4))
        b.grid(row=2, column=0,)
        b = Button(root, text="5", width=10,command= lambda *args: self.setVar(5))
        b.grid(row=2, column=1,)
        b = Button(root, text="6", width=10,command= lambda *args: self.setVar(6))
        b.grid(row=2, column=2,)
        b = Button(root, text="7", width=10,command= lambda *args: self.setVar(7))
        b.grid(row=3, column=0,)
        b = Button(root, text="8", width=10,command= lambda *args: self.setVar(8))
        b.grid(row=3, column=1,)
        b = Button(root, text="9", width=10,command= lambda *args: self.setVar(9))
        b.grid(row=3, column=2,)
        b = Button(root, text="*", width=10,command= lambda *args: self.setVar("*"))
        b.grid(row=4, column=0,)
        b = Button(root, text="0", width=10,command= lambda *args: self.setVar(0))
        b.grid(row=4, column=1,)
        b = Button(root, text="#", width=10,command= lambda *args: self.setVar("#"))
        b.grid(row=4, column=2,)

start=App()
