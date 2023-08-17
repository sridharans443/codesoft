from tkinter import *
import random

import pyperclip
w=Tk()
w.title("password generator")
w.geometry("350x200")

passwordLabel=Label(w,text='Password Generator',font=('Arial Rounded MT Bold',20,'bold'),bg='gray20',fg='white')
passwordLabel.place(x=30,y=15)

password_entry = Entry(w, font=("Eras Bold ITC", 20),width=10, bg='gray',fg='black')
password_entry.place(x=80,y=70)

def generate():
   
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    password = ""
  
    for x in range(8):
        password = password + random.choice(pass1)
        
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    
    return password

def copy():
    random_password=generate()
    pyperclip.copy(random_password)
  
copyButton=Button(w,text='Generate & Copy',font=('OCR A Extended',13,'bold'),command=copy,bg="red",fg="white")
copyButton.place(x=80,y=120)

