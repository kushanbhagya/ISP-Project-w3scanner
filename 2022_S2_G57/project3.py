from tkinter import *
import subprocess
import os


root = Tk()
root.title('w3scanner')
#root.iconbitmap(r'icon.ico')

#root.geometry("600x600")

# img=PhotoImage(file='logo.png')
# Label(root,image=img).pack()
# root.mainloop()

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

mylabel = Label(root, text ="Whatweb", font= "Arial 15", padx=5, pady=5)
mylabel.pack()

#button01 = Button(root, text="Whatweb").grid(row=1, column=1)
#button01.grid(row=1, column=1)
#button01.pack(padx=5, pady=5)

#button02 = Button(root, text="Nmap")grid(row=1, column=2)
#button02.grid(row=1, column=2)
#button02.pack(padx=5, pady=5)

#button03 = Button(root, text="button").grid(row=1, column=3)
#button03.grid(row=1, column=3)
#button03.pack(padx=5, pady=5)


#frame = LabelFrame(root, text="Result", padx=5, pady=5)
#frame.pack(padx=10, pady=10)

def output():
    L = subprocess.getstatusoutput("whatweb "+var.get()+" "+var1.get()+" "+var2.get()+" "+e.get())
    Resultlabel1 = Label(root, text=L)
    Resultlabel1.pack()

e = Entry(root, width=50, borderwidth=2)
e.pack(padx=20, pady=5)


var = StringVar()
c = Checkbutton(root, text="Verbose output", variable=var, onvalue="-v", offvalue="", padx=20, pady=5)
c.deselect()
c.pack(anchor=NW)


var1 = StringVar()
c1 = Checkbutton(root, text="List all plugins", variable=var1, onvalue="-l", offvalue="", padx=20, pady=5)
c1.deselect()
c1.pack(anchor=W)

var2 = StringVar()
c2 = Checkbutton(root, text="Do not display brief logging to STDOUT", variable=var2, onvalue="-q", offvalue="", padx=20, pady=5)
c2.deselect()
c2.pack(anchor=SW)

submitbutton= Button(root, text="Show Results", command=output, padx=20, pady=5)
submitbutton.pack(pady=10)

root.mainloop()

