import tkinter as tk
from tkinter import ttk
from tkinter import *

win = tk.Tk()
win.title("Kalkulator v1.0")
win.resizable(False,False)

inputan =""
def hapus():
    global inputan
    inputan = ""
    input_text.set("")

def layar(angka):
    global inputan
    inputan = inputan + str(angka)
    input_text.set(inputan)
    
def operasi():
    inputan = screen.get()
    hasil = str(eval(inputan))
    input_text.set(hasil)
    inputan = ""

#####################################################################################
input_text = StringVar()

screen = ttk.Entry(win,width=35,textvariable=input_text)
screen.grid(sticky="W",column=0,row=0,columnspan=3,padx=10,pady=10)

button0 = ttk.Button(win,text="0",width=10,command = lambda: layar(0))
button0.grid(column=1,row=4, )

button1 = ttk.Button(win,text="1",width=10,command = lambda: layar(1))
button1.grid(column=0,row=3, )

button2 = ttk.Button(win,text="2",width=10,command = lambda: layar(2))
button2.grid(column=1,row=3, )

button3 = ttk.Button(win,text="3",width=10,command = lambda: layar(3))
button3.grid(column=2,row=3, )

button4 = ttk.Button(win,text="4",width=10,command = lambda: layar(4))
button4.grid(column=0,row=2, )

button5 = ttk.Button(win,text="5",width=10,command = lambda: layar(5))
button5.grid(column=1,row=2, )

button6 = ttk.Button(win,text="6",width=10,command = lambda: layar(6))
button6.grid(column=2,row=2, )

button7 = ttk.Button(win,text="7",width=10,command = lambda: layar(7))
button7.grid(column=0,row=1, )

button8 = ttk.Button(win,text="8",width=10,command = lambda: layar(8))
button8.grid(column=1,row=1, )

button9 = ttk.Button(win,text="9",width=10,command = lambda: layar(9))
button9.grid(column=2,row=1, )

button_hapus = ttk.Button(win,text="C",width=10,command = hapus)
button_hapus.grid(column=0,row=4, )

button_bagi = ttk.Button(win,text="/",command = lambda: layar("/"))
button_bagi.grid(column=3,row=1, )

button_kali = ttk.Button(win,text="*",command = lambda: layar("*"))
button_kali.grid(column=3,row=2, )

button_tambah = ttk.Button(win,text="+",command = lambda: layar("+"))
button_tambah.grid(column=3,row=3, )

button_kurang = ttk.Button(win,text="-",command = lambda: layar("-"))
button_kurang.grid(column=3,row=4, )

button_titik = ttk.Button(win,text=".",width =10, command = lambda: layar("."))
button_titik.grid(column=2,row=4, )

button_enter = ttk.Button(win,text="=",width=10,command = lambda:operasi())
button_enter.grid(column=3,row=0, )

watermark = ttk.Label(win,text="made by @arya_m.k") 
watermark.grid(sticky="W",column=0,row=5,columnspan=2)
#####################################################################################

win.mainloop()
