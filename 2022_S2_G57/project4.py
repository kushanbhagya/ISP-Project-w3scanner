from tkinter import *
import subprocess
import os

root = Tk()
root.title('w3scanner')

mylabel = Label(root, text ="w3scanner", font= "Arial 20", padx=5, pady=5)
mylabel.pack()

def program01():
    os.system('python project3.py')

def program02():
    os.system('python project4.py')

def program03():
    os.system('python project5.py')

frame = Frame(root)
Button(frame, text="Whatweb", command = program01).grid(row=0,column=0)
Button(frame, text="Nmap", command = program02).grid(row=0,column=1)
Button(frame, text="Button", command = program03).grid(row=0,column=2)
frame.pack()

mylabel = Label(root, text ="Nmap", font= "Arial 15", padx=5, pady=5)
mylabel.pack()

def output():
    L = subprocess.getstatusoutput("nmap "+var.get()+" "+var1.get()+" "+var2.get()+" "+e.get())
    Resultlabel1 = Label(root, text=L)
    Resultlabel1.pack()

e = Entry(root, width=50, borderwidth=2)
e.pack(padx=20, pady=5)


var = StringVar()
c = Checkbutton(root, text="Fast Scan", variable=var, onvalue="-F", offvalue="", padx=20, pady=5)
c.deselect()
c.pack(anchor=NW)


var1 = StringVar()
c1 = Checkbutton(root, text="Scan without Ping Requests", variable=var1, onvalue="-Pn", offvalue="", padx=20, pady=5)
c1.deselect()
c1.pack(anchor=W)

var2 = StringVar()
c2 = Checkbutton(root, text="Operating System Detection", variable=var2, onvalue="-A", offvalue="", padx=20, pady=5)
c2.deselect()
c2.pack(anchor=SW)


submitbutton= Button(root, text="Show Results", command=output, padx=20, pady=5)
submitbutton.pack(pady=10)

root.mainloop()