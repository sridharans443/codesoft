from tkinter import *

root = Tk()
root.title("Calculator")
root.config(bg="black")
root.geometry("320x394")
root.resizable(False,False)
equation = ""

def show(value):
    global equation
    equation+=value
    entry.config(text=equation)
def clear():
    global equation
    equation = ""
    entry.config(text=equation)
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error!"
    entry.config(text=result)

entry = Label(root,text="",width=15,height=3,font="arial 20")
entry.grid(row=0,column=0,columnspan=4,sticky="nsew")


but_1 = Button(root,text="1",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("1"))
but_2 = Button(root,text="2",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("2"))
but_3 = Button(root,text="3",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("3"))
but_4 = Button(root,text="4",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("4"))
but_5 = Button(root,text="5",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("5"))
but_6 = Button(root,text="6",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("6"))
but_7 = Button(root,text="7",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("7"))
but_8 = Button(root,text="8",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("8"))
but_9 = Button(root,text="9",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("9"))
but_0 = Button(root,text="0",padx=72,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("0"))

but_clear = Button(root,text="C",font=("arial",10,"bold"),bd=1,padx=30,pady=15,bg="#3697f5",command=clear)
but_add = Button(root,text="+",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("+"))
but_minus = Button(root,text="-",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("-"))
but_divide = Button(root,text="÷",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("/"))
but_modu = Button(root,text="%",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("%"))
but_multi = Button(root,text="×",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("*"))
but_dot = Button(root,text=".",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("."))
but_equal = Button(root,text="=",width=10,pady=45,fg="black",bg="#fe9037",bd=1,command=calculate)

but_multi.grid(row=1,column=0,padx=1,pady=2)
but_modu.grid(row=1,column=1,padx=1,pady=2)
but_divide.grid(row=1,column=2,padx=1,pady=2)
but_clear.grid(row=1,column=3,padx=2,pady=2)

but_1.grid(row=2,column=0,pady=2)
but_2.grid(row=2,column=1,pady=2)
but_3.grid(row=2,column=2,pady=2)
but_minus.grid(row=2,column=3,pady=2)

but_4.grid(row=3,column=0,pady=2)
but_5.grid(row=3,column=1,pady=2)
but_6.grid(row=3,column=2,pady=2)
but_add.grid(row=3,column=3,pady=2)

but_7.grid(row=4,column=0,pady=2)
but_8.grid(row=4,column=1,pady=2)
but_9.grid(row=4,column=2,pady=2)
but_equal.grid(row=4,column=3,rowspan=2,pady=2)

but_0.grid(row=5,column=0,columnspan=2,pady=2)
but_dot.grid(row=5,column=2,pady=2)

#Centralize Window
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#root.mainloop()
