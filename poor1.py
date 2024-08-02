
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("ll")
root.geometry("800x800")
def polygon():
     polygon2=canvas.create_polygon(10, 30, 200, 200, 200, 30, fill="#80CBC4", outline="#004D40")
     polygon2lambda['state']=DISABLED
     

def oval():
     oval2=canvas.create_oval(80, 100, 400, 50, fill="#80CBC4", outline="#004D40")
     oval2['state']=DISABLED

     

def rectangle():
     global rectangle2
     rectangle2=canvas.create_rectangle(60, 300, 200, 100, fill="#80CBC4", outline="#004D40")
rectangle2['state']=DISABLED
     

def  clear():
     canvas.delete('all')
canvas = Canvas(bg="white", width=500, height=450)
canvas.pack(anchor=CENTER, expand=1)
btn1=Button(root,text='polyon',command=lambda:polygon)
btn1.pack()
btn2=Button(root,text='oval',command=lambda:oval)
btn2.pack()
btn3=Button(root,text='rextangle',command=lambda:rectangle)
btn3.place(x=10,y=50)
btn4=Button(root,text='clear',command=clear)
btn4.place(x=50,y=80)



root.mainloop()



