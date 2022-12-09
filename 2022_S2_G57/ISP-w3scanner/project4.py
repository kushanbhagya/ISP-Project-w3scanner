from tkinter import *
from tkinter import ttk
import subprocess
import os
import sys
from PIL import Image, ImageTk

root = Tk()
root.title('w3scanner')
root.geometry("960x800")
#root.resizable(False, True)
#root.configure(bg='#444444')

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame, bg='#444444')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas, bg='#444444')

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#bg = PhotoImage(file="bg2.png")

#bg_label = Label(root, image=bg)
#bg_label.place(x=0, y=0, width=800, height=500)

#v_s = Scrollbar(root)
#v_s.pack(side=RIGHT, fill=Y)

#h_s = Scrollbar(root, orient='horizontal')
#h_s.pack(side=BOTTOM, fill=X)

#textarea = Text(root, width=25, height=15, Wrap=NONE, yscrollcommand=v_s.set, xscrollcommand=h_s.set)

image = Image.open("logo.png")
resize_image = image.resize((200, 93))
img = ImageTk.PhotoImage(resize_image)

label1 = Label(second_frame, image=img, bg='#444444')
label1.image = img
label1.pack(pady=20)

def program01():
    subprocess.Popen(['python3', 'project3.py'])
    sys.exit(0)

def program02():
    subprocess.Popen(['python3', 'project4.py'])
    sys.exit(0)

def program03():
    subprocess.Popen(['python3', 'project5.py'])
    sys.exit(0)

def click(event):
    l1.config(state=NORMAL)
    l1.delete(8, END)

frame = Frame(second_frame, pady=10, bg='#444444')
Button(frame, text="Whatweb", command = program01, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=0,padx=10)
Button(frame, text="Nmap", command = program02, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=1,padx=10)
Button(frame, text="Nikto", command = program03, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=2,padx=10)
frame.pack()

mylabel = Label(second_frame, text ="Nmap", font= "Arial 18 bold", padx=5, pady=5, bg='#444444', fg='#ffffff')
mylabel.pack()

def output():
    L = subprocess.getstatusoutput("nmap "+var.get()+" "+var1.get()+" "+var2.get()+" "+var12.get()+" "+var11.get()+" "+var10.get()+" "+var9.get()+" "+e.get()+" "+var3.get()+" "+l1.get()+" "+var4.get()+" "+l2.get()+" "+var5.get()+" "+var6.get()+" "+l3.get()+" "+var7.get()+" "+var8.get())
    Resultlabel1 = Label(LF, text=L)
    Resultlabel1.pack()

def click(event):
    e.config(state=NORMAL)
    e.delete(0, END)

e = Entry(second_frame, width=50, borderwidth=2, font='bold')
e.insert(0, "Enter the Domain Address or IP")
e.config(state=DISABLED)
e.bind("<Button-1>",click)
e.pack(padx=20, pady=5)

input_frame = Frame(second_frame, bg='#444444')


mylabel1 = Label(input_frame, text ="Base Uses", font= "Arial 15 bold", padx=15, pady=5, bg='#444444', fg='#ffffff')
#mylabel1.pack(anchor=W)
mylabel1.grid(row=0, column=0, sticky=W)

var = StringVar()
c = Checkbutton(input_frame, text="Fast Scan", variable=var, onvalue="-F", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c.deselect()
#c.pack(anchor=NW)
c.grid(row=1, column=0, sticky=W)
c.config(selectcolor="#000000")

var9 = StringVar()
c9 = Checkbutton(input_frame, text="Trace Route the target", variable=var9, onvalue="-traceroute", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c9.deselect()
#c9.pack(anchor=SW)
c9.grid(row=2, column=0, sticky=W)
c9.config(selectcolor="#000000")

var4 = StringVar()
c4 = Checkbutton(input_frame, text="Port Scan", variable=var4, onvalue="-p", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c4.deselect()
#c4.pack(anchor=SW)
c4.grid(row=3, column=0, sticky=W)
c4.config(selectcolor="#000000")

def click(event):
    l2.config(state=NORMAL)
    l2.delete(0, END)

l2 = Entry(input_frame, width=16, borderwidth=2)
#l2.insert(0, "Enter Port Number")
l2.config(state=DISABLED)
l2.bind("<Button-1>",click)
#l2.pack(padx=40, pady=5)
l2.grid(row=3, column=1, sticky=W)

var6 = StringVar()
c6 = Checkbutton(input_frame, text="Exclude IP Address", variable=var6, onvalue="-exclude", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c6.deselect()
#c6.pack(anchor=SW)
c6.grid(row=4, column=0, sticky=W)
c6.config(selectcolor="#000000")

def click(event):
    l3.config(state=NORMAL)
    l3.delete(0, END)

l3 = Entry(input_frame, width=16, borderwidth=2)
#l3.insert(0, "Enter Exclude IP Address")
l3.config(state=DISABLED)
l3.bind("<Button-1>",click)
#l3.pack(padx=40, pady=5, anchor=W)
l3.grid(row=4, column=1, sticky=W)

var5 = StringVar()
c5 = Checkbutton(input_frame, text="Scan with default NCE script", variable=var5, onvalue="-sC", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c5.deselect()
#c5.pack(anchor=SW)
c5.grid(row=5, column=0, sticky=W)
c5.config(selectcolor="#000000")


mylabel2 = Label(input_frame, text ="Discovery Options", font= "Arial 15 bold", padx=15, pady=5, bg='#444444', fg='#ffffff')
#mylabel2.pack(anchor=W)
mylabel2.grid(row=7, column=0, sticky=W)

var10 = StringVar()
c10 = Checkbutton(input_frame, text="Ping Scan only", variable=var10, onvalue="-sP", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c10.deselect()
#c10.pack(anchor=SW)
c10.grid(row=8, column=0, sticky=W)
c10.config(selectcolor="#000000")

var1 = StringVar()
c1 = Checkbutton(input_frame, text="Scan without Ping Requests", variable=var1, onvalue="-Pn", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c1.deselect()
#c1.pack(anchor=W)
c1.grid(row=9, column=0, sticky=W)
c1.config(selectcolor="#000000")

var11 = StringVar()
c11 = Checkbutton(input_frame, text="TCP SYN Ping", variable=var11, onvalue="-PS", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c11.deselect()
#c11.pack(anchor=SW)
c11.grid(row=10, column=0, sticky=W)
c11.config(selectcolor="#000000")

var12 = StringVar()
c12 = Checkbutton(input_frame, text="TCP ACK Ping", variable=var12, onvalue="-PA", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c12.deselect()
#c12.pack(anchor=SW)
c12.grid(row=11, column=0, sticky=W)
c12.config(selectcolor="#000000")


mylabel3 = Label(input_frame, text ="OS & Service Detection", font= "Arial 15 bold", padx=15, pady=5, bg='#444444', fg='#ffffff')
#mylabel3.pack(anchor=W)
mylabel3.grid(row=0, column=2, sticky=W)

var2 = StringVar()
c2 = Checkbutton(input_frame, text="Operating System Detection", variable=var2, onvalue="-A", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c2.deselect()
#c2.pack(anchor=SW)
c2.grid(row=1, column=2, sticky=W)
c2.config(selectcolor="#000000")

var7 = StringVar()
c7 = Checkbutton(input_frame, text="Service Detection", variable=var7, onvalue="-sV", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c7.deselect()
#c7.pack(anchor=SW)
c7.grid(row=2, column=2, sticky=W)
c7.config(selectcolor="#000000")


mylabel4 = Label(input_frame, text ="Other", font= "Arial 15 bold", padx=15, pady=5, bg='#444444', fg='#ffffff')
#mylabel4.pack(anchor=W)
mylabel4.grid(row=4, column=2, sticky=W)

var8 = StringVar()
c8 = Checkbutton(input_frame, text="Firewall/IDS Evation", variable=var4, onvalue="-f", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c8.deselect()
#c8.pack(anchor=SW)
c8.grid(row=5, column=2, sticky=W)
c8.config(selectcolor="#000000")

var3 = StringVar()
c3 = Checkbutton(input_frame, text="Scan Random Hosts", variable=var3, onvalue="-iR", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c3.deselect()
#c3.pack(anchor=SW)
c3.grid(row=6, column=2, sticky=W)
c3.config(selectcolor="#000000")

def click(event):
    l1.config(state=NORMAL)
    l1.delete(0, END)


l1 = Entry(input_frame, width=17, borderwidth=2)
#l1.insert(0, "Enter Hosts Number")
l1.config(state=DISABLED)
l1.bind("<Button-1>",click)
#l1_placeholder = Label(l1, text='Enter Hosts Number', fg='gray', bg='white')
#l1_placeholder.place(x=0, y=0)
#l1_placeholder.bind('<Button-1>', lambda e: l1.focus())
#l1.pack(padx=40, pady=5, anchor=W)
l1.grid(row=6, column=3, sticky=W)

input_frame.pack()


submitbutton= Button(second_frame, text="Show Results", command=output, padx=20, pady=5, font='bold', bg='#087cf4', fg='#ffffff')
submitbutton.pack(pady=10)

LF=LabelFrame(second_frame,text="Output")

#mycanvas = Canvas(LF)
#mycanvas.pack(side=LEFT)

#yscrollbar = ttk.Scrollbar(LF, orient="vertical", command=mycanvas.yview)
#yscrollbar.pack(side=RIGHT, fill="y")

#myframe = Frame(mycanvas)

LF.pack(padx=10, pady=10)



root.mainloop()