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

from tkinter import messagebox
from page_2 import open_page2

i = 0
th_i = 0
eng_i = 0
mycanvas = ""


#########################################
def open_page3(previous_root):
    previous_root.destroy()
    root = tk.Tk()
    root.title("ตัวอย่างโปรแกรมที่ใช้ ttk")
    ##root.resizable(False, False)
    root.minsize(width=550, height=250)
    root.maxsize(width=650, height=500)
    root.configure(bg='#D3F2FF')

    frame = tk.Frame(root,bg='#D3F2FF')
    frame.grid(row=2,column=0,padx=50)


    style = ttk.Style()
    style.configure("TButton", font=("Kumothin", 18))

    mycanvas = ""

    def get_dataword_file():
        try:
            with open("dataword_status.txt", "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            return "dataword1.txt"  # ใช้ค่าเริ่มต้นหากไม่พบไฟล์
            
    file_name = get_dataword_file()

    def load_dataword_data():
        global num_row
        global new_array
        global random_numbers
        with open(get_dataword_file(), "r", encoding="utf-8") as file:
            data = file.read()
            data_split = data.split(" ")
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)
            random_numbers = random.sample(range(0, int(num_row)), int(num_row))
            
    def on_mousewheel(event):
        mycanvas.yview_scroll(-1 * (event.delta // 120), "units")

    def show_wordQWQ():
        global mycanvas
        wrapper1 = ttk.LabelFrame(frame)
        wrapper2 = ttk.LabelFrame(frame)
        wrapper1.grid(row=9, column=0, padx=0, pady=0)  


        mycanvas = Canvas(wrapper1)
        mycanvas.grid(row=1, column=0)
        mycanvas.config(width=550, height=300)  

        yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.grid(row=1, column=1, sticky="ns")  
        mycanvas.configure(yscrollcommand=yscrollbar.set)

        xscrollbar = ttk.Scrollbar(wrapper2, orient="horizontal", command=mycanvas.xview)
        xscrollbar.grid(row=0, column=0, sticky="ew")
        mycanvas.configure(xscrollcommand=xscrollbar.set)

        mycanvas.bind('<Enter>', lambda e: mycanvas.bind_all('<MouseWheel>', on_mousewheel))
        mycanvas.bind('<Leave>', lambda e: mycanvas.unbind_all('<MouseWheel>'))

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        myframe = ttk.Frame(mycanvas)
        mycanvas.create_window((0, 0), window=myframe, anchor="nw")

        for widget in myframe.winfo_children():
            if widget.grid_info()['column'] in [0, 1, 2]:
                widget.destroy()

        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
            data_split = data.split(" ")
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)
            random_numbers = random.sample(range(0, int(num_row)), int(num_row))

        labels = []
        indexlabel = ttk.Label(myframe, text=f"คำที่คุณเขียนผิดทั้งหมด มีจำนวน = {len(Wrong_word)} คำ", font=("Kumothin", 18)).grid(row=0, column=0)

        for i in range(len(Wrong_word)):
            labels.append(ttk.Label)
            q = ttk.Label(myframe, text=i+1, font=("Kumothin", 18)).grid(row=i+1, column=0)
            w = ttk.Label(myframe, text=Wrong_word[i, 0], font=("Kumothin", 18)).grid(row=i+1, column=1,)
            e = ttk.Label(myframe, text=Wrong_word[i, 1], font=("Kumothin", 18)).grid(row=i+1, column=2,)


        myframe.update_idletasks()
        mycanvas.config(scrollregion=mycanvas.bbox("all"))

    def clear_entry(event, name):
        name.delete(0, tk.END)

    def choese_test(event):
        global th_i,eng_i
        if th_i == 1:
            check_number_test_th()
        elif eng_i == 1:
            check_number_test_eng()



    
    def start_count_test_th():
        global new_array,random_numbers,i,th_i
        th_i = 1
        word_count = len(new_array)
        if i in range(word_count):
            a = new_array[random_numbers[i]][0]
            word_test.config(text=a)

        else:
            word_test.config(text="การทดสอบเสร็จสิน")
            th_i = 0
            i=0
        show_wordQWQ()
    def start_count_test_eng():
        global new_array,random_numbers,i,eng_i
        eng_i = 1
        word_count = len(new_array)
        if i in range(word_count):
            a = new_array[random_numbers[i]][1]
            word_test.config(text=a)
            
        else:
            word_test.config(text="การทดสอบเสร็จสิน")
            eng_i = 0
            show_wordQWQ()
            i=0


        
    Wrong_word = np.empty((0,3))
    Wrong_word_count = np.empty((0,2))
    def check_number_test_th():
        try:
            global new_array,random_numbers,i,Wrong_word,Wrong_word_count
            user_input = input_entry.get()
            user_word = str(user_input)
            qwq = new_array[random_numbers[i]]
            if user_word == str(new_array[random_numbers[i]][1]):
                i+=1
                print(i)
                start_count_test_th()
                input_entry.delete(0, tk.END)
                
            else:
                Wrong_word = np.append(Wrong_word, [qwq],axis=0)
                print(Wrong_word)
        except:
            label2.config(text="คุณได้ทดสอบเสร็จแล้ว")

    def check_number_test_eng():
        try:
            global new_array,random_numbers,i,Wrong_word,Wrong_word_count
            user_input = input_entry.get()
            user_word = str(user_input)
            qwq = new_array[random_numbers[i]]
            if user_word.lower() == str(new_array[random_numbers[i]][0]).lower():
                i+=1
                print(i)
                start_count_test_eng()
                input_entry.delete(0, tk.END)
                
            else:
                Wrong_word = np.append(Wrong_word, [qwq],axis=0)
                print(Wrong_word)
        except:
            label2.config(text="คุณได้ทดสอบเสร็จแล้ว")

    load_dataword_data()
    next_p3  = tk.PhotoImage(file="next2.png")
    test_eng = tk.PhotoImage(file="test_eng.png")
    test_th  = tk.PhotoImage(file="test_th.png")
    ba_p3    = tk.PhotoImage(file="ba.png")
    up_p3    = tk.PhotoImage(file="up2.png")


    label1 = tk.Label(frame,text="⠀", font=("Kumothin", 20),bg='#D3F2FF')
    label1.grid(row=0,column=0)

    word_test = tk.Label(frame, text="คำศัพท์", font=("Kumothin", 40, "bold"),bg='#D3F2FF')
    word_test.grid(row=1,column=0)

    label2 = tk.Label(frame,text="⠀", font=("Kumothin", 20),bg='#D3F2FF')
    label2.grid(row=2,column=0)



    input_entry = ttk.Entry(frame, text="input words",width=40,font=("Kumothin", 16))
    input_entry.grid(row=3,column=0,pady=10)
    input_entry.bind("<Button-1>", lambda event,name=input_entry:clear_entry(event,name))
    input_entry.bind("<Return>", choese_test)


    ok_button = tk.Button(frame, image=next_p3,borderwidth=0, bg='#D3F2FF')
    ok_button.grid(row=4,column=0,pady=5)




    test_Eng = tk.Button(frame, image=test_eng,borderwidth=0, bg='#D3F2FF',command=start_count_test_eng)
    test_Eng.grid(row=5,column=0,pady=5,sticky='w')

    test_Th = tk.Button(frame, image=test_th,borderwidth=0, bg='#D3F2FF',command=start_count_test_th)
    test_Th.grid(row=5,column=0,pady=5,sticky='e')

    s_button = tk.Button(frame,image=ba_p3,borderwidth=0, bg='#D3F2FF', command=lambda: back_to_page1(root))
    s_button.grid(row=6,column=0,pady=5,sticky='w')


    add_word_button = tk.Button(frame,image=up_p3,borderwidth=0, bg='#D3F2FF',command=lambda: open_page2(root))
    add_word_button.grid(row=6,column=0,pady=5,sticky='e')

    label1 = tk.Label(frame,text="⠀", font=("Kumothin", 35),bg='#D3F2FF')
    label1.grid(row=7,column=0)

    label2 = tk.Label(frame,text="⠀",bg='#D3F2FF')
    label2.grid(row=8,column=0)



    root.mainloop()

def back_to_page1(current_root):
    current_root.destroy()
    import page_1
    page_1.open_page1()

