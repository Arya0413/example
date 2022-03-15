from tkinter import*
def add():
    a=float(e1.get())
    b=float(e2.get())
    c=a+b
    l3.config(text=c)
t=Tk()
t.geometry('500x500')
t.title("SUM")
e1=Entry()
e2=Entry()
l1=Label(text="Find the sum")
l3=Label(text="")
p=Button(t,text="ADD",command=add)
l1.place(x=200,y=50)
e1.place(x=100,y=100)
e2.place(x=250,y=100)
l3.place(x=200,y=150)
p.place(x=400,y=100)
