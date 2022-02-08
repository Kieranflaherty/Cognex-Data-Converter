from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
import pandas as pd

root=Tk()
root.geometry("500x300")
root.title("Cognex Data Converter")

tk.Label(root,
		 text="Cognex Data Converter",
		 fg = "black",
		 bg = "yellow",
         width = "500",
         height = "2",
		 font = "Helvetica 18 bold italic").pack()

ent1=Entry(root,font=("Calibri 12"),width="30")
ent1.place(x=125,y=100)
filepath = Label(text="File Path: ")
filepath.place(x=65,y=100)

#2 functions to access files, convert to csv and to display message box
def browsefunc():
	global filename
	filename = askopenfilename(filetypes=(("txt file", "*.txt"),))
	ent1.insert(END, filename) # add this
def convert():
	try:
		df = pd.read_csv(filename,delimiter=';')
		df.to_csv('Cognex_Data.csv')
	except:
		tk.messagebox.showinfo("Cognex Data Converter","Failed to write to CSV. Close CSV file and try again.")
	else:
		tk.messagebox.showinfo("Cognex Data Converter","Data Converted Successfully")

#Create buttons for convert and select file
b1=Button(root,text="Select File",command=browsefunc,width="10",height="1",bg="light grey")
b1.place(x=140,y=170)
b2=Button(root,text="Convert",command=lambda:[convert()],width="10",height="1",bg="light grey")
b2.place(x=265,y=170)

root.mainloop()
