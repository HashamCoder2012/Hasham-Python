from tkinter import *
from tkinter import messagebox

from PIL import Image,ImageTk


root=Tk()
root.title("Denumination Calculator")
root.geometry("500x500")

upload=Image.open("C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham Python/Image.png")
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image)
label.place(x=20,y=20)
label1=Label(root,text="Hey user!,Welcome to denomination calculator")
label1.place(x=50,y=400)

def msg():
    MsgBox=messagebox.showinfo("Alert","do you want to calculatr the demonition count")
    if MsgBox=="ok":
        topwin()

button1=Button(root,text="Lets get started!",command=msg,bg="brown",fg='white')
button1.place(x=180,y=180)

def topwin():
    top=Toplevel()
    top.title("toplevel")
    top.geometry("400x400")

    label=Label(top,text="enter total amount")
    entry=Entry(top)
    lbl=Label(top,text="Here are number of notes for each denomination")

    l1=Label(top,text="1000")
    l2=Label(top,text="500")
    l3=Label(top,text="100")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        global amount
        amount=int(entry.get())
        note1000=amount//1000
        amount=amount%1000
        note500=amount//500
        amount=amount%500
        note100=amount//100
        amount=amount%100

        t1.insert(END,str(note1000))
        t2.insert(END,str(note500))
        t3.insert(END,str(note100))
    btn=Button(top,text="Calculate",command=calculator)
    label.place(x=30,y=50)
    entry.place(x=180,y=50)
    btn.place(x=150,y=100)
    lbl.place(x=30,y=150)

    l1.place(x=80,y=200)
    l2.place(x=80,y=230)
    l3.place(x=80,y=260)

    t1.place(x=180,y=200)
    t2.place(x=180,y=230)
    t3.place(x=180,y=260)
    
    top.mainloop()
root.mainloop()