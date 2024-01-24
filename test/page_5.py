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

def open_page5(previous_root):
    previous_root.destroy()
    root = tk.Tk()
    root.title("โปรแกรมท่องศัพท์ภาษาอังกฤษ")
    ##root.resizable(False, False)
    root.minsize(width=550, height=250)
    root.maxsize(width=650, height=600)
    root.configure(bg='#D3F2FF')

    frame = tk.Frame(root,bg='#D3F2FF')
    frame.grid(row=0,column=0,padx=50)

    frame2 = tk.Frame(frame,bg='#D3F2FF')
    frame2.grid(row=3, column=0, pady=10)

    frame3 = tk.Frame(frame,bg='#D3F2FF')
    frame3.grid(row=6, column=0, pady=10)

    teset_button = ttk.Button(frame,text="กลับหน้าหลัก",width= 35,command=lambda :back_to_page1(root))
    teset_button.grid(row=0,column=0)

    root.mainloop()

def back_to_page1(current_root):
    current_root.destroy()
    import page_1
    page_1.open_page1()
