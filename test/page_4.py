import tkinter as tk
from tkinter import font
import numpy as np
import random
from tkinter import ttk, Canvas

from playsound import playsound
import os
import gtts
from gtts import gTTS

import re
import nltk
from nltk.corpus import words
from page_2 import open_page2
from page_5 import open_page5

from tkinter import messagebox
#################################################################
def change_to_dataword1():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword1.txt")
def change_to_dataword2():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword2.txt")
def change_to_dataword3():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword3.txt")
def change_to_dataword4():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword4.txt")
def change_to_dataword5():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword5.txt")
def change_to_dataword6():
    with open("dataword_status.txt", "w") as file:
        file.write("dataword6.txt")
#################################################################

def open_page4(previous_root):
    previous_root.destroy()
    root = tk.Tk()
    root.title("โปรแกรมท่องศัพท์ภาษาอังกฤษ")
    ##root.resizable(False, False)

    root.minsize(width=550, height=250)
    root.maxsize(width=650, height=600)
    root.configure(bg='#D3F2FF')

    
    frame = tk.Frame(root,bg='#D3F2FF')
    frame.grid(row=2,column=0,padx=50)

    photo1_p4 = tk.PhotoImage(file="1.png")
    photo2_p4 = tk.PhotoImage(file="2.png")
    photo3_p4 = tk.PhotoImage(file="3.png")
    photo4_p4 = tk.PhotoImage(file="4.png")
    photo5_p4 = tk.PhotoImage(file="5.png")
    photo6_p4 = tk.PhotoImage(file="6.png")
    ba_p4    = tk.PhotoImage(file="ba.png")
    up_p4   = tk.PhotoImage(file="up2.png")



    style = ttk.Style()
    style.configure("TButton", font=("Kumothin", 20))

    group2_Button = ttk.Button(frame,text ="หมวดหมู่",width= 7)
    group2_Button.grid(row=0,column=0,pady=5,sticky='w')

    manual_button = ttk.Button(frame, text="คู่มือ",width=5,command=lambda: open_page5(root))
    manual_button.grid(row=0,column=0,pady=5,sticky='e')


    label1 = tk.Label(frame,text="เลือกหมวดหมู่ที่ต้องการ", font=("Kumothin", 40),bg='#D3F2FF')
    label1.grid(row=1,column=0,padx= 60)

    label1 = tk.Label(frame,text="⠀", font=("Kumothin", 20),bg='#D3F2FF')
    label1.grid(row=0,column=0)
#################################################################
    am_button = tk.Button(frame,image=photo1_p4,borderwidth=0,bg='#D3F2FF', command=change_to_dataword2)
    am_button.grid(row=2,column=0,pady=15,sticky= 'w')
#################################################################
    op_button = tk.Button(frame,image=photo2_p4,borderwidth=0,bg='#D3F2FF', command=change_to_dataword3)
    op_button.grid(row=2,column=0,pady=15,sticky= 'e')

    lc_button = tk.Button(frame,image=photo3_p4,borderwidth=0,bg='#D3F2FF',command=change_to_dataword4)
    lc_button.grid(row=3,column=0,pady=15,sticky= 'w')

    it_button = tk.Button(frame,image=photo4_p4,borderwidth=0,bg='#D3F2FF',command=change_to_dataword5)
    it_button.grid(row=3,column=0,pady=15,sticky= 'e')

    sp_button = tk.Button(frame,image=photo5_p4,borderwidth=0,bg='#D3F2FF',command=change_to_dataword6)
    sp_button.grid(row=4,column=0,pady=15,sticky= 'w')

    an_button = tk.Button(frame,image=photo6_p4,borderwidth=0,bg='#D3F2FF',command=change_to_dataword1)
    an_button.grid(row=4,column=0,pady=15,sticky= 'e')

   
    s_button = tk.Button(frame,image=ba_p4,borderwidth=0, bg='#D3F2FF', command=lambda: back_to_page1(root))
    s_button.grid(row=6,column=0,pady=5,sticky='w')


    add_word_button = tk.Button(frame,image=up_p4,borderwidth=0, bg='#D3F2FF',command=lambda: open_page2(root))
    add_word_button.grid(row=6,column=0,pady=5,sticky='e')

    label1 = tk.Label(frame,text="⠀", font=("Kumothin", 20),bg='#D3F2FF')
    label1.grid(row=5,column=0)

    label1 = tk.Label(frame,text="⠀", font=("Kumothin", 20),bg='#D3F2FF')
    label1.grid(row=7,column=0)


    

    root.mainloop()

def back_to_page1(current_root):
    current_root.destroy()
    import page_1
    page_1.open_page1()