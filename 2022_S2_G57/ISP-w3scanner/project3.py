from tkinter import *
from tkinter import ttk
import subprocess
import os
from PIL import Image, ImageTk
import sys

root = Tk()
root.title('w3scanner')
root.geometry("570x700")
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


frame = Frame(second_frame, pady=10, bg='#444444')
Button(frame, text="Whatweb", command = program01, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=0, padx=10)
Button(frame, text="Nmap", command = program02, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=1, padx=10)
Button(frame, text="Nikto", command = program03, bg='#087cf4', fg='#ffffff', font='bold').grid(row=0,column=2, padx=10)
frame.pack()

mylabel = Label(second_frame, text ="Whatweb", font= "Arial 18 bold", padx=5, pady=5, bg='#444444', fg='#ffffff')
mylabel.pack()

def output():
    L = subprocess.getstatusoutput("whatweb "+var.get()+" "+var1.get()+" "+var2.get()+" "+e.get())
    Resultlabel1 = Label(LF, text=L)
    Resultlabel1.pack()

def click(event):
    e.config(state=NORMAL)
    e.delete(0, END)

e = Entry(second_frame, width=50, borderwidth=2, font='bold')
e.insert(0, "Enter the Domain Address or IP")
e.config(state=DISABLED)
e.bind("<Button-1>",click)
e.pack(padx=20, pady=20)


var = StringVar()
c = Checkbutton(second_frame, text="Verbose output", variable=var, onvalue="-v", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c.deselect()
c.pack(anchor=NW)
c.config(selectcolor="#000000")

var1 = StringVar()
c1 = Checkbutton(second_frame, text="List all plugins", variable=var1, onvalue="-l", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c1.deselect()
c1.pack(anchor=W)
c1.config(selectcolor="#000000")

var2 = StringVar()
c2 = Checkbutton(second_frame, text="Do not display brief logging to STDOUT", variable=var2, onvalue="-q", offvalue="", padx=20, pady=5, bg='#444444', fg='#ffffff', highlightbackground="#444444", activebackground='#444444', font='bold')
c2.deselect()
c2.pack(anchor=SW)
c2.config(selectcolor="#000000")

submitbutton= Button(second_frame, text="Show Results", font='bold', command=output, padx=20, pady=5, bg='#087cf4', fg='#ffffff')
submitbutton.pack(pady=30)



LF=LabelFrame(second_frame,text="Output")

#scroll_bar = Scrollbar(LF)
#scroll_bar.pack( side = RIGHT, fill = Y )

#mycanvas = Canvas(LF, yscrollcommand = scroll_bar.set)
#mycanvas.pack()

#scroll_bar.config( command = mycanvas.yview)

#yscrollbar = ttk.Scrollbar(LF)
#yscrollbar.pack(side=RIGHT, fill="y")

#myframe = Frame(mycanvas, bg='#444444')

LF.pack(padx=10, pady=10)

root.mainloop()