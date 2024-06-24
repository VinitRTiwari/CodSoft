from tkinter import *
a = Tk()
a.geometry ( "450x500" )                          #Size of GUI application
a.title("Calculator...")                          #Title of GUI application
a.resizable(False,False)                     
expression = ""
text_show = StringVar()

#function define input by clicking button

def click(num):
    global expression
    expression = expression + str(num)
    text_show.set(expression)

#function that clear display screen

def clear():
    global expression
    expression = ""
    text_show.set("")

#function that handle exception and display output

def equal():
    global expression
    try:
        output = str(eval(expression))
        text_show.set(output)
        expression = ""
    except:
        text_show.set("ERROR")
        expression = ""
    
 #Screen to show output   
e1 = Entry(a, textvariable = text_show ,bg="black",fg="white",font=("Helvetica",29,"bold"))
e1.grid(row=0,column=0,columnspan = 4)
#Buttons of calculator....
b1 = Button(a,text = "1",command=lambda : click(1),height=5,width=16,bg="black",fg="white")
b1.grid(row=4,column=0)
b2 = Button(a,text = "2",command=lambda : click(2),height=5,width=16,bg="black",fg="white")
b2.grid(row=4,column=1)
b3 = Button(a,text = "3",command=lambda : click(3),height=5,width=16,bg="black",fg="white")
b3.grid(row=4,column=2)
bAdd = Button(a,text = "+",command=lambda : click("+"),height=5,width=10,bg="black",fg="white")
bAdd.grid(row=4,column=3)
b4 = Button(a,text = "4",command=lambda : click(4),height=5,width=16,bg="black",fg="white")
b4.grid(row=3,column=0)
b5 = Button(a,text = "5",command=lambda : click(5),height=5,width=16,bg="black",fg="white")
b5.grid(row=3,column=1)
b6 = Button(a,text = "6",command=lambda : click(6),height=5,width=16,bg="black",fg="white")
b6.grid(row=3,column=2)
bSub = Button(a,text = "-",command=lambda : click("-"),height=5,width=10,bg="black",fg="white")
bSub.grid(row=3,column=3)
b7 = Button(a,text = "7",command=lambda : click(7),height=5,width=16,bg="black",fg="white")
b7.grid(row=2,column=0)
b8 = Button(a,text = "8",command=lambda : click(8),height=5,width=16,bg="black",fg="white")
b8.grid(row=2,column=1)
b9 = Button(a,text = "9",command=lambda : click(9),height=5,width=16,bg="black",fg="white")
b9.grid(row=2,column=2)
bMulti = Button(a,text = "*",command=lambda : click("*"),height=5,width=10,bg="black",fg="white")
bMulti.grid(row=2,column=3)
bClear = Button(a,text = "C", command=lambda: clear(),height=5,width=51,bg="black",fg="white")
bClear.grid(row=1,column=0,columnspan=3)
bDiv = Button(a,text = "/",command=lambda : click("/"),height=5,width=10,bg="black",fg="white")
bDiv.grid(row=1,column=3)
b0 = Button(a,text = "0",command=lambda : click(0),height=5,width=34,bg="black",fg="white")
b0.grid(row=5,column=0,columnspan=2)
bDot = Button(a,text = ".",command=lambda : click("."),height=5,width=16,bg="black",fg="white")
bDot.grid(row=5,column=2)
bEqual = Button(a,text = "=",command=lambda: equal(),height=5,width=10,bg="black",fg="white")
bEqual.grid(row=5,column=3)
a.mainloop()