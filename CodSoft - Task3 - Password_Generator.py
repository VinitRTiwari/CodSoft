from tkinter import *
from tkinter import messagebox
import random
import string
def password():
    try:
        length = int(entryValue.get())
        if length <= 0:
            messagebox.showinfo("Error", "Password length can't be 0")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "\n".join(random.choice(characters) for i in range(length)) 
        entryPassword.delete(0, END)
        entryPassword.insert(0, password)
    
    except:
        messagebox.showinfo("Error", "Please enter valid number")

a = Tk()
a.title("Password Generator")
a.geometry("300x400")
a.config({"bg":"red"})
label1 = Label(a, text="Enter Length for Password :", bg="red",font=("Arial",16))
label1.pack()
entryValue = Entry(a,bg="green",font=("Arial",16))
entryValue.pack(pady=10)
passwordBtn = Button(a, text="Generate Password", command=password,bg="gray",font=("Arial",16))
passwordBtn.pack()
label2 = Label(a, text="Password Generated :",bg="red",font=("Arial",16))
label2.pack()
entryPassword = Listbox(a, bg="green",font=("Arial",16))
entryPassword.pack(pady=10)
a.mainloop()