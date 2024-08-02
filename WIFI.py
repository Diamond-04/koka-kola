import tkinter as tk
from tkinter import messagebox 
app=tk.Tk()
app.title('password')
app.geometry('400x600')

var=tk.StringVar()
var_entry=tk.Entry(app,textvariable=var)
var_entry.place(x=40,y=400)


def handle_button(variable):
    var_entry.insert(variable,variable)
# def jack():
#     nuli = open('d:\WinUsers\Asus\Desktop\myprojectkkkkk.txt','a')
#     nuli.write(var_entry.get()+'\n')
# nuli.close()    
def check_password():
    password = "1234"
    info = var_entry.get()
    if len(info) == 4:
        if var_entry.get() == password:
            messagebox.showinfo("Hurray!", "Accecc granted")
            app.destroy()
        else:
            messagebox.askretrycancel("askretrycancel", "Wrong password!")
    else:
        messagebox.askretrycancel("askretrycancel", "You need to input 4 digit number")
            
    

number_button1=tk.Button(app,width=10,height=5,
                         text='1',fg='white',bg='purple',
                         command=lambda: handle_button(1))
number_button1.place(x=40,y=1)
number_button2=tk.Button(app,width=10,height=5,
                         text='2',fg='white',bg='purple',
                         command=lambda: handle_button(2))
number_button2.place(x=150,y=1)
number_button3=tk.Button(app,width=10,height=5,
                         text='3',fg='white',bg='purple',
                         command=lambda: handle_button(3))
number_button3.place(x=260,y=1)
number_button4=tk.Button(app,width=10,height=5,
                         text='4',fg='white',bg='purple',
                         command=lambda: handle_button(4))
number_button4.place(x=40,y=120)
number_button5=tk.Button(app,width=10,height=5,
                         text='5',fg='white',bg='purple',
                         command=lambda: handle_button(5))
number_button5.place(x=150,y=120)
number_button6=tk.Button(app,width=10,height=5,
                         text='6',fg='white',bg='purple',
                         command=lambda: handle_button(6))
number_button6.place(x=260,y=120)
number_button7=tk.Button(app,width=10,height=5,
                         text='7',fg='white',bg='purple',
                         command=lambda: handle_button(7))
number_button7.place(x=40,y=240)
number_button8=tk.Button(app,width=10,height=5,
                         text='8',fg='white',bg='purple',
                         command=lambda: handle_button(8))
number_button8.place(x=150,y=240)
number_button9=tk.Button(app,width=10,height=5,text='9',fg='white',bg='purple',
                         command=lambda: handle_button(9))
number_button9.place(x=260,y=240)

submit_button=tk.Button(app,width=10,height=5,text='Submit',fg='white',bg='purple',
                        command=lambda:check_password())
submit_button.place(x=260,y=350)



app.mainloop()

















