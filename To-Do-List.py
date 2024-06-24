from tkinter import *
from tkinter import messagebox

a =Tk()
a.title("To-Do List")
a.geometry("400x650")
a.config({"bg":"blue"})
def add_text():
    task = e.get()
    if task:
        l.insert( END, task)
        e.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter a task!")

def remove_text():
    selected = l.curselection()
    if selected:
        l.delete(selected)
    else:
        messagebox.showerror("Error", "Please select a task!")

l = Listbox(a, bg="Black", fg="White", font=("Arial",14))
l.pack(side=TOP, pady=10)
label = Label(a,text="Enter your task below...",bg="blue",font=("Arial",16))
label.pack(pady=25)
e = Entry(a)
e.pack()
addBtn = Button(a, text="Add Task", command=add_text, bg="gray",font=("Arial",12))
addBtn.pack(pady=10)
removeBtn = Button(a, text="Remove Task", command=remove_text, bg="gray",font=("Arial",12))
removeBtn.pack(pady=10)
a.mainloop()