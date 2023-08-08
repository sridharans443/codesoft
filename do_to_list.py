from tkinter import*
from tkinter import messagebox
from tkinter import ttk

w=Tk()
w.title("TO DO LIST")
w.geometry("600x700")
w.configure(bg="#D8F8FF")

a1=Label(w,text="TO DO LIST",font=("Arial Rounded MT Bold",25))
a1.place(x=180,y=30)


task=Label(w,text="Enter task to add:",font=("Arial Rounded MT Bold",18))
task.place(x=10,y=90)

task_bt=Entry(w,width=80,bd=5)
task_bt.place(x=50,y=135)

to_do=Label(w,text="Pending tasks:",font=("Arial Rounded MT Bold",18))
to_do.place(x=10,y=210)



# Listbox with all the tasks with a Scrollbar
tasks = Listbox(w, selectbackground='Gold', bg='Silver', font=("Arial Rounded MT Bold", 12), height=18, width=35)

scroller = Scrollbar(w, orient=VERTICAL, command=tasks.yview)
scroller.place(x=415, y=280, height=345)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=115, y=280)


# Adding items to the Listbox
with open('tasks.txt', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()


# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open('tasks.txt', 'w') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()


#Button

add_btn = Button(w, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: add_item(task_bt, tasks))
add_btn.place(x=190, y=170)

delete_btn = Button(w, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=280, y=170)


