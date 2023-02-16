from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pickle


def new_task():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")


def delete_task():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TODO')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=new_task
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


def save_list():
    file_name = filedialog.asksaveasfilename(initialdir='F:\Programs\Python projects\TODO\data',
                                             title='Save File',
                                             filetypes=(
                                                 ('Dat Files', '*.dat'),
                                                 ('All Files', '*.*'))
                                             )
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

        count = 0
        while count < lb.size():
            if lb.itemcget(count, 'fg') == '#dedede':
                lb.delete(lb.index(count))
            else:
                count += 1

        stuff = lb.get(0, END)

        output_file = open(file_name, 'wb')
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(initialdir='F:\Programs\Python projects\TODO\data',
                                           title='Open File',
                                           filetypes=(
                                               ('Dat Files', '*.dat'),
                                               ('All Files', '*.*'))
                                           )
    if file_name:
        lb.delete(0, END)
        input_file = open(file_name, 'rb')
        stuff = pickle.load(input_file)
        for i in stuff:
            lb.insert(END, i)


def delete_list():
    lb.delete(0, END)


my_menu = Menu(ws)
ws.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=delete_list)

ws.mainloop()
