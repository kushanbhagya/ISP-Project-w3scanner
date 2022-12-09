from tkinter import *
import subprocess
import os
from PIL import Image, ImageTk
import sys

root = Tk()
root.title('w3scanner')
root.geometry("960x800")
#root.resizable(False, True)
root.configure(bg='#444444')

#bg = PhotoImage(file="bg2.png")

#bg_label = Label(root, image=bg)
#bg_label.place(x=0, y=0, width=800, height=500)

v_s = Scrollbar(root)
v_s.pack(side=RIGHT, fill=Y)

h_s = Scrollbar(root, orient='horizontal')
h_s.pack(side=BOTTOM, fill=X)

#root.iconbitmap(r'logo.ico')

image = Image.open("logo.png")
resize_image = image.resize((200, 93))
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img, bg='#444444')
label1.image = img
label1.pack(pady=20)

# mylabel = Label(root, text ="w3scanner", font= "Arial 20", padx=5, pady=5)
# mylabel.pack()

def program01():
    subprocess.Popen(['python3', 'project3.py'])
    sys.exit(0)

def program02():
    subprocess.Popen(['python3', 'project4.py'])
    sys.exit(0)

def program03():
    subprocess.Popen(['python3', 'project5.py'])
    sys.exit(0)


frame = Frame(root, pady=10, bg='#444444')
Button(frame, text="Whatweb", command = program01, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=0, padx=10)
Button(frame, text="Nmap", command = program02, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=1, padx=10)
Button(frame, text="Nikto", command = program03, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=2, padx=10)
frame.pack()

mylabel = Label(root, text ="Nikto", font= "Arial 18 bold", padx=5, pady=5, bg='#444444', fg='#ffffff')
mylabel.pack()

def output():
    L = subprocess.getstatusoutput("nikto -h "+e.get()+" "+var.get()+" "+var6.get()+" "+var1.get()+" "+l.get() +var2.get()+" "+l1.get()+" "+var5.get()+" "+var7.get()+" "+l2.get()+" "+var8.get()+" "+l3.get())
    Resultlabel1 = Label(LF, text=L)
    Resultlabel1.pack()

def click(event):
    e.config(state=NORMAL)
    e.delete(0, END)

e = Entry(root, width=50, borderwidth=2, font='bold')
e.insert(0, "Enter the Domain Address or IP")
e.config(state=DISABLED)
e.bind("<Button-1>",click)
e.pack(padx=20, pady=20)

input_frame = Frame(root, bg='#444444')

var = StringVar()
c = Checkbutton(input_frame, text="Force SSL", variable=var, onvalue="-ssl", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c.deselect()
#c.pack(anchor=NW)
c.grid(row=0, column=0, sticky=W)
c.config(selectcolor="#000000")

var6 = StringVar()
c6 = Checkbutton(input_frame, text="No SSL During the scan", variable=var6, onvalue="-nossl", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c6.deselect()
#c6.pack(anchor=SW)
c6.grid(row=1, column=0, sticky=W)
c6.config(selectcolor="#000000")

var1 = StringVar()
c1 = Checkbutton(input_frame, text="Port Scan", variable=var1, onvalue="-port", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c1.deselect()
#c1.pack(anchor=W)
c1.grid(row=2, column=0, sticky=W)
c1.config(selectcolor="#000000")

def click(event):
    l.config(state=NORMAL)
    l.delete(0, END)

l = Entry(input_frame, width=16, borderwidth=2)
l.insert(0, "Enter Port Number")
l.config(state=DISABLED)
l.bind("<Button-1>",click)
#l.pack(padx=40, pady=5, anchor=W)
l.grid(row=2, column=1, sticky=W)

var2 = StringVar()
c2 = Checkbutton(input_frame, text="Maximum Scan Time", variable=var2, onvalue="-maxtime", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c2.deselect()
#c2.pack(anchor=W)
c2.grid(row=3, column=0, sticky=W)
c2.config(selectcolor="#000000")

def click(event):
    l1.config(state=NORMAL)
    l1.delete(0, END)

l1 = Entry(input_frame, width=16, borderwidth=2)
l1.insert(0, "Enter Scan Time")
l1.config(state=DISABLED)
l1.bind("<Button-1>",click)
#l1.pack(padx=40, pady=5, anchor=W)
l1.grid(row=3, column=1, sticky=W)

var4 = StringVar()
c4 = Checkbutton(input_frame, text="OS Scanning", variable=var4, onvalue="-O", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c4.deselect()
#c4.pack(anchor=SW)
c4.grid(row=4, column=0, sticky=W)
c4.config(selectcolor="#000000")

var5 = StringVar()
c5 = Checkbutton(input_frame, text="No DNS Lookup for the hosts", variable=var5, onvalue="-nolookups", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c5.deselect()
#c5.pack(anchor=SW)
c5.grid(row=5, column=0, sticky=W)
c5.config(selectcolor="#000000")

var7 = StringVar()
c7 = Checkbutton(input_frame, text="Output the file", variable=var7, onvalue="-o", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c7.deselect()
#c7.pack(anchor=SW)
c7.grid(row=6, column=0, sticky=W)
c7.config(selectcolor="#000000")

def click(event):
    l2.config(state=NORMAL)
    l2.delete(0, END)

l2 = Entry(input_frame, width=16, borderwidth=2)
l2.insert(0, "Enter Port Number")
l2.config(state=DISABLED)
l2.bind("<Button-1>",click)
#l2.pack(padx=40, pady=5, anchor=W)
l2.grid(row=6, column=1, sticky=W)

var8 = StringVar()
c8 = Checkbutton(input_frame, text="Select a Format", variable=var8, onvalue="-Format", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c8.deselect()
#c8.pack(anchor=SW)
c8.grid(row=7, column=0, sticky=W)
c8.config(selectcolor="#000000")

def click(event):
    l3.config(state=NORMAL)
    l3.delete(0, END)

l3 = Entry(input_frame, width=16, borderwidth=2)
l3.insert(0, "Enter a Format")
l3.config(state=DISABLED)
l3.bind("<Button-1>",click)
#l3.pack(padx=40, pady=5, anchor=W)
l3.grid(row=7, column=1, sticky=W)

input_frame.pack(anchor=NW)


submitbutton= Button(root, text="Show Results", font= 'bold', command=output, padx=20, pady=5, bg='#087cf4', fg='#ffffff')
submitbutton.pack(pady=30)

LF=LabelFrame(root,text="Output")
LF.pack(padx=10, pady=10)

root.mainloop()