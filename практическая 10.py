from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Checkbutton
import tkinter.messagebox as mb
from tkinter.ttk import Combobox


window = Tk()
window.title("Могутнов Ярослав Романович Уб-22")
window.geometry('1000x600') 

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

def kalkul():
    a=combo.get()
    b=int(txt1.get())
    c=int(txt2.get())
    if a == '-':
        l=b-c
        lbl.configure(text=l)
    elif a == '+':
        l=b+c
        lbl.configure(text=l)
    elif a == '*':
        l=b*c
        lbl.configure(text=l)
    elif a== '/':
        l=b/c
        lbl.configure(text=l)


txt1 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt1.place(x = 60, y = 250, width=200, height=100,)

combo = Combobox(tab1, font=("Times New Romane", 20))
combo.place(x=300, y = 255, width=100, height=80)
combo['values'] = ('+', '-', '*', '/')

txt2 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt2.place(x = 440, y = 250, width=200, height=100)

btn1 = Button(tab1, text="=", font=("Times New Romane", 30), command=kalkul)
btn1.place(x=680, y = 255, width=100, height=80)

lbl = Label(tab1, text="", font=("Times New Romane", 30))
lbl.place(x=780, y = 250, width=200, height=100 )


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Вторая')

def clicked():
    a=chk_state1.get()
    if a == True:
        mb.showinfo('', 'Вы выбрали первый вариант ответа!')
    b=chk_state2.get()
    if b == True:
        mb.showinfo('', 'Вы выбрали второй вариант ответа!')
    c=chk_state3.get()
    if c == True:
        mb.showinfo('', 'Вы выбрали третий вариант ответа!')
    if a != True and b != True and c!= True:
        mb.showinfo('', ' Вы не выбрали вариант ответа!!!')   

chk_state1 = BooleanVar()
chk_state1.set(0) 
chk1 = Checkbutton(tab2, text='Первый', var=chk_state1, onvalue=1, offvalue=0,)
chk1.grid(column=100, row=50)

chk_state2 = BooleanVar()
chk_state2.set(0) 
chk2 = Checkbutton(tab2, text='Второй', var=chk_state2, onvalue=1, offvalue=0)
chk2.grid(column=150, row=50) 

chk_state3 = BooleanVar()
chk_state3.set(0) 
chk3 = Checkbutton(tab2, text='Третий', var=chk_state3, onvalue=1, offvalue=0)
chk3.grid(column=200, row=50) 

btn = Button(tab2, text="Сохранить", command=clicked)
btn.grid(column=150, row=100)

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Работа с текстом')
tab_control.pack(expand=1, fill='both')
def f():
    with open('E:\python\практическая 10\\практическая 10.txt') as f:
        z=""
        for line in f.readlines():
            z+=line
        lbl5.configure(text=z)
btn5 = Button(tab3, text="Копировать из файла", font=("Times New Romane", 30), command=f)
btn5.place(x=300, y = 0, width=500, height=80)
lbl5 = Label(tab3, text='', font=("Times New Romane", 30))
lbl5.place(x=0, y = 100, width=1000, height=100 )
window.mainloop()
