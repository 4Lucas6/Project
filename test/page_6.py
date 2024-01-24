import tkinter as tk
from tkinter.font import Font
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

from tkinter import messagebox

from page_2 import open_page2

def change_to_themeblue():
    with open("theme.txt", "w") as file:
        file.write("themeblue.txt")

def change_to_themered():
    with open("theme.txt", "w") as file:
        file.write("themered.txt")

def change_to_themepurple():
    with open("theme.txt", "w") as file:
        file.write("themepurple.txt")

def open_page6(previous_root):
    previous_root.destroy()
    root = tk.Tk()
    root.title("โปรแกรมท่องศัพท์ภาษาอังกฤษ")
    #root.resizable(False, False)
    root.minsize(width=650, height=650)
    root.maxsize(width=650, height=650)
    root.configure(bg='#D3F2FF')

    frame = tk.Frame(root,bg='#D3F2FF')
    frame.grid(row=0,column=0,padx=50)

    style = ttk.Style()
    style.configure("TButton", font=("Kumothin", 18))

    ba = tk.PhotoImage(file="ba.png")
    up = tk.PhotoImage(file="up2.png")

    themelabel = tk.Label(frame,text="เลือกธีมที่ต้องการ", font=("Kumothin", 30, "bold"),bg='#D3F2FF')
    themelabel.grid(row=0,column=0,pady=20,padx=110)

    themeblue_button = tk.Button(frame,text="เปลี่ยนธีมเป็นน้ำเงิน", font=("Kumothin", 30, "bold"),command=lambda: change_to_themeblue())
    themeblue_button.grid(row=1,column=0,pady=20,padx=110)

    themered_button = tk.Button(frame,text="เปลี่ยนธีมเป็นสีแดง", font=("Kumothin", 30, "bold"),command=lambda: change_to_themered())
    themered_button.grid(row=2,column=0,pady=20,padx=110)

    themepurple_button = tk.Button(frame,text="เปลี่ยนธีมเป็นสีม่วง", font=("Kumothin", 30, "bold"),command=lambda: change_to_themepurple)
    themepurple_button.grid(row=3,column=0,pady=20,padx=110)

    s_button = tk.Button(frame,image=ba,borderwidth=0, bg='#D3F2FF', command=lambda: back_to_page1(root))
    s_button.grid(row=4,column=0,pady=20,sticky='w')

    add_word_button = tk.Button(frame,image=up,borderwidth=0, bg='#D3F2FF',command=lambda: open_page2(root))
    add_word_button.grid(row=4,column=0,pady=20,sticky='e')


    
    root.mainloop()

def back_to_page1(current_root):
    current_root.destroy()
    import page_1
    page_1.open_page1()
