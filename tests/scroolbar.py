# Imports
from tkinter import *
from tkinter.ttk import *
# Import for the listboxEditable
from ListboxEditable import *

# Colors
colorActiveTab="#CCCCCC" # Color of the active tab
colorNoActiveTab="#EBEBEB" # Color of the no active tab
# Fonts
fontLabels='Calibri'
sizeLabels2=13

# Main window
root = Tk()

# *** Design *****
frame_name=Frame(root,bg=colorActiveTab) # Column frame
frame_name_label=Frame(frame_name,bg='blue') # Label frame
label_name=Label(frame_name_label, text="Header", bg='blue', fg='white', font=(fontLabels, sizeLabels2, 'bold'), pady=2, padx=2, width=10)
frame_name_listbox=Frame(frame_name,bg='blue') # Label frame
list_name=['test1','test2','test3']
listBox_name=ListboxEditable(frame_name_listbox,list_name,selectmode="tk.BROWSE")

# *** Packing ****
frame_name.pack(side=LEFT,fill=Y)
frame_name_label.pack(side=TOP, fill=X)
label_name.pack(side=LEFT,fill=X)
frame_name_listbox.pack(side=TOP, fill=X)
listBox_name.placeListBoxEditable()

# Infinite loop
root.mainloop()
