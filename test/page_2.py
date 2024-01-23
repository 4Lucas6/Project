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

        

    

############################################
def open_page2(previous_root):
    
   

    previous_root.destroy()
    add_txt_windows = tk.Tk()
    add_txt_windows.title("ตัวอย่างโปรแกรมที่ใช้ ttk")
    add_txt_windows.resizable(False, False)
    add_txt_windows.minsize(width=550, height=250)
    add_txt_windows.maxsize(width=650, height=1000)
    add_txt_windows.configure(bg='#D3F2FF')

    frame = tk.Frame(add_txt_windows,bg='#D3F2FF')
    frame.grid(row=0, column=0, padx=50, pady=10)

    frame2 = tk.Frame(add_txt_windows,bg='#D3F2FF')
    frame2.grid(row=2, column=0, padx=50, pady=10)

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
            
    
    def clear_entry(event, name):
        name.delete(0, tk.END)
        
    def delete_txt():
        #try:
        index = int(index_input.get()) -1
        
        with open(get_dataword_file(), "r", encoding="utf-8") as file:
            data = file.read()
            data_split = data.split(" ")
            print(data_split)
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)


        a = str(new_array[index][0])
        b = str(new_array[index][1])
        c = str(new_array[index][2])
        
        if index == 0:
            data = data.replace(f"{a} {b} {c} ","")
        else:
            data = data.replace(f" {a} {b} {c}" or f"{a} {b} {c} ","")

        print(data)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(data)
            data_split = data.split(" ")
            print(data_split)
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)

        txt_label.config(text="ลบคำศัพท์ออกแล้ว!",bg='#D3F2FF')
        #except:
            #txt_label.config(text="ไม่มีคำศัพท์ลำดับที่คุณกรอกมาในไฟล์!")

    def check_word(event):
        content = str(input_eng.get())
        if re.sub(r"[^\w]", "", content.lower()) not in words.words():
            input_eng.config(foreground="red")
        else:
            input_eng.config(foreground="black")


    def write_txt():
        eng_word = input_eng.get()
        th_word = input_th.get()
        read_th = input_read_th.get()
        if re.sub(r"[^\w]", "", eng_word.lower()) not in words.words():
            a = messagebox.askquestion('แจ้งเตือน',"คำศัพท์ของคุณอาจจะผิดต้องการเพิ่มลงไฟล์ไหม")
            if a == "yes":
                qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in eng_word)
                qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in th_word)
                qc_read_th = all(ord(char) < 3676 and ord(char) > 3584 for char in read_th)
                if qc_eng and qc_th and qc_read_th == True:
                    with open(file_name, "at", encoding="utf-8") as file:
                        file.write(" " + eng_word + " " + th_word + " " + read_th)
                        txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!",bg='#D3F2FF')
                        input_eng.delete(0, tk.END)
                        input_th.delete(0, tk.END)
                        input_read_th.delete(0, tk.END)
                else:
                    txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")
        else:
            qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in eng_word)
            qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in th_word)
            qc_read_th = all(ord(char) < 3676 and ord(char) > 3584 for char in read_th)
            if qc_eng and qc_th and qc_read_th == True:
                with open(file_name, "at", encoding="utf-8") as file:
                    file.write(" " + eng_word + " " + th_word + " " + read_th)
                    txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!",bg='#D3F2FF')
                    input_eng.delete(0, tk.END)
                    input_th.delete(0, tk.END)
                    input_read_th.delete(0, tk.END)
                    
            else:
                txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")

    txt_label = tk.Label(add_txt_windows, text="")
    txt_label.grid(row=4, column=0, pady=5)

    def on_mousewheel(event):
        mycanvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_horizontal_scroll(*args):
        mycanvas.xview(*args)

    def show_wordQWQ():

        for widget in myframe.winfo_children():
            if widget.grid_info()['column'] in [0, 1, 2, 3]:
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
        indexlabel = ttk.Label(myframe, text="ลำดับ", font=("Kumothin", 18)).grid(row=0, column=0, padx=(20, 30))
        wordlabel = ttk.Label(myframe, text="คำศัพท์", font=("Kumothin", 18)).grid(row=0, column=1, padx=(40, 30))
        wordTHlabel = ttk.Label(myframe, text="คำแปล", font=("Kumothin", 18)).grid(row=0, column=2, padx=(0, 30))
        readlabel = ttk.Label(myframe, text="คำอ่าน", font=("Kumothin", 18)).grid(row=0, column=3, padx=(20, 25))

        for i in range(int(num_row)):
            labels.append(ttk.Label)
            q = ttk.Label(myframe, text=i+1, font=("Kumothin", 18)).grid(row=i+1, column=0, padx=(20, 30))
            w = ttk.Label(myframe, text=new_array[i, 0], font=("Kumothin", 18)).grid(row=i+1, column=1, padx=(50, 30))
            e = ttk.Label(myframe, text=new_array[i, 1], font=("Kumothin", 18)).grid(row=i+1, column=2, padx=(30, 30))
            r = ttk.Label(myframe, text=new_array[i, 2], font=("Kumothin", 18)).grid(row=i+1, column=3, padx=(20, 25))

        myframe.update_idletasks()
        mycanvas.config(scrollregion=mycanvas.bbox("all"))
    load_dataword_data()
    up_p2 = tk.PhotoImage(file="up_p2.png")
    de_p2 = tk.PhotoImage(file="de.png")
    ba_p2 = tk.PhotoImage(file="ba.png")
    all_p2 = tk.PhotoImage(file="all.png")


    style = ttk.Style()
    style.configure("TButton", font=("Kumothin", 18))


    input_th = ttk.Entry(frame , width=35, font=("Kumothin", 18))
    input_th.grid(row=1, column=0, pady=5)
    input_th.insert(0,"กรอกข้อความภาษาไทย")
    input_th.bind("<Button-1>", lambda event, entry=input_th: clear_entry(event, entry))


    input_eng = ttk.Entry(frame, width=35, font=("Kumothin", 18))
    input_eng.grid(row=2, column=0, pady=5)
    input_eng.insert(0,"กรอกข้อความภาษาอังกฤษ")
    input_eng.bind("<KeyRelease>", check_word)
    input_eng.bind("<Button-1>", lambda event, entry=input_eng: clear_entry(event, entry))

    input_read_th = ttk.Entry(frame , width=35, font=("Kumothin", 18))
    input_read_th.grid(row=3, column=0, pady=5)
    input_read_th.insert(0,"กรอกข้อความคำอ่านภาษาไทย")
    input_read_th.bind("<Button-1>", lambda event, entry=input_read_th: clear_entry(event, entry))

    oK2_button = tk.Button(frame,image=up_p2,borderwidth=0, bg='#D3F2FF',command=write_txt)
    oK2_button.grid(row=4, column=0, pady=5)


    #########

    index_input = ttk.Entry(frame , width=20, font=("Kumothin", 16))
    index_input.grid(row=5, column=0, pady=0 ,sticky='w')
    index_input.insert(0,"กรอก")
    index_input.bind("<Button-1>", lambda event, entry=index_input: clear_entry(event, entry))

    delete_button = tk.Button(frame,image=de_p2,borderwidth=0, bg='#D3F2FF',command=delete_txt)
    delete_button.grid(row=5, column=0, pady=0,sticky='e')

    #########

    wrapper1 = ttk.LabelFrame(add_txt_windows)
    wrapper2 = ttk.LabelFrame(add_txt_windows)

    mycanvas = Canvas(wrapper1)
    mycanvas.grid(row=1, column=0)
    mycanvas.config(width=550, height=300)  

    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
    yscrollbar.grid(row=1, column=1, sticky="ns")  
    mycanvas.configure(yscrollcommand=yscrollbar.set)

    xscrollbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=mycanvas.xview)
    xscrollbar.grid(row=10, column=0, sticky="ew")
    mycanvas.configure(xscrollcommand=xscrollbar.set)

    mycanvas.bind('<Enter>', lambda e: mycanvas.bind_all('<MouseWheel>', on_mousewheel))
    mycanvas.bind('<Leave>', lambda e: mycanvas.unbind_all('<MouseWheel>'))

    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    myframe = ttk.Frame(mycanvas)
    mycanvas.create_window((0, 0), window=myframe, anchor="nw")

    wrapper1.grid(row=1, column=0, padx=10, pady=10)  
    wrapper2.grid(row=2, column=0, padx=10, pady=10) 

    s_button = tk.Button(frame2, image=ba_p2,borderwidth=0, bg='#D3F2FF', command=lambda: back_to_page1(add_txt_windows))
    s_button.grid(row=0, column=0 ,padx=(0,10))

    s_w_button = tk.Button(frame2,image=all_p2,borderwidth=0, bg='#D3F2FF', command=show_wordQWQ)
    s_w_button.grid(row=0, column=1 ,padx=(0,0))



    add_txt_windows.mainloop()

def back_to_page1(current_root):
    current_root.destroy()
    import page_1
    page_1.open_page1()
