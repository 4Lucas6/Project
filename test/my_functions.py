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


a = 0
set_a = 0
flie_name = "dataword1.txt"

def change_file(f_name):
    global flie_name
    flie_name = f_name
    with open(flie_name, "r", encoding="utf-8") as file:
        data = file.read()
        data_split = data.split(" ")
        numpy_data = np.array(data_split)

        num_split = len(numpy_data)
        num_row = num_split / 3
        new_array = numpy_data.reshape(int(num_row), 3)
        random_numbers = random.sample(range(0, int(num_row)), int(num_row))

with open(flie_name, "r", encoding="utf-8") as file:
    data = file.read()
    data_split = data.split(" ")
    numpy_data = np.array(data_split)

    num_split = len(numpy_data)
    num_row = num_split / 3
    new_array = numpy_data.reshape(int(num_row), 3)
    random_numbers = random.sample(range(0, int(num_row)), int(num_row))

show_text = ""
count = 0
count2 = 0
check_buttom = 0




def delete_txt():
    global new_array
    global data
    
    try:

        index = int(index_input.get()) -1


        a = str(new_array[index][0])
        b = str(new_array[index][1])
        c = str(new_array[index][2])
        if index == 0:
            data = data.replace(f"{a} {b} {c} ","")
        else:
            data = data.replace(f" {a} {b} {c}" or f"{a} {b} {c} ","")

        with open(flie_name, "w", encoding="utf-8") as file:
            file.write(data)
            data_split = data.split(" ")
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)

        txt_label.config(text="ลบคำศัพท์ออกแล้ว!")
    except:
        txt_label.config(text="ไม่มีคำศัพท์ลำดับที่คุณกรอกมาในไฟล์!")

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
                with open(flie_name, "at", encoding="utf-8") as file:
                    file.write(" " + eng_word + " " + th_word + " " + read_th)
                    txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!")
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
            with open(flie_name, "at", encoding="utf-8") as file:
                file.write(" " + eng_word + " " + th_word + " " + read_th)
                txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!")
                input_eng.delete(0, tk.END)
                input_th.delete(0, tk.END)
                input_read_th.delete(0, tk.END)
        else:
            txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")
    
def play_mp3():
    qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in show_text)
    qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in show_text)
    try:
        if qc_th == True:
            tts = gTTS(show_text,lang='th')
            tts.save('speech.mp3')
            playsound('speech.mp3')
            os.remove('speech.mp3')
        else:
            tts = gTTS(show_text,lang='en')
            tts.save('speech.mp3')
            playsound('speech.mp3')
            os.remove('speech.mp3')
    except:
        result_label.config(text="ไม่มีอินเตอร์เน็ตใช้ไม่ได้")

def reset_word():
    global random_numbers
    global count
    global check_buttom
    global reset_buttom
    global loop_buttom
    global set_a
    loop_buttom.config(state=tk.DISABLED)
    reset_buttom.config(state=tk.DISABLED)
    loop_buttom.config(image=photo3)
    reset_buttom.config(image=photo5)
    random_numbers = random.sample(range(0, int(num_row)), int(num_row))
    start_button.config(state=tk.NORMAL)
    read_and_Type.config(state=tk.NORMAL)
    entry.config(state=tk.NORMAL)
    set_a = 0
    
    count = 0
    
def set_global_a():
    global set_a
    set_a = 1
    entry.config(state=tk.DISABLED)

def openNew_windows(name):
    name.deiconify()

def hide_windows(name):
    name.withdraw()

def closeAll():
    root.destroy() 
    add_txt_windows.destroy()
     
def set_count_to_zero():
    global count
    global set_a

    loop_buttom.config(state=tk.DISABLED)
    reset_buttom.config(state=tk.DISABLED)
    loop_buttom.config(image=photo3)
    reset_buttom.config(image=photo5)

    if set_a == 1:
        set_global_a()
        
    else:
         set_a = 0
         entry.config(state=tk.NORMAL)
    count = 0
    start_count()

def start_count():
    num_loop = int(num.get())
    global a
    if num_loop > int(num_row):
        num_loop = int(num_row)
        if a == 0:
            result_label.config(text="คุณใส่ศัพท์เกินแต่เราแก้ให้เป็นจำนวนสูงสุดแล้วนะ!")
            a = 1
    global count
    global count2
    global show_text
    global random_numbers
    global reset_buttom
    global loop_buttom
    try:

        start_button.config(state=tk.DISABLED)
        read_and_Type.config(state=tk.DISABLED)


        if count in range(int(num_loop)):
            show_text = new_array[random_numbers[count], count2]
            show_textread = new_array[random_numbers[count], 2]
            label.config(text=str(show_text))
            labelread.config(text=str(show_textread))
            count2 += 1
            

            if count2 > 1:
                count2 = 0
                count += 1
                result_label.config(text=show_word)
        else:
            label.config(text="คำศัพท์หมดแล้วว!")
            result_label.config(text=show_word)
            labelread.config(text="คำอ่าน")
            loop_buttom.config(state=tk.NORMAL)
            reset_buttom.config(state=tk.NORMAL)
            loop_buttom.config(image=photo1H)
            reset_buttom.config(image=photo2H)
            
            a = 0
           
               

    except ValueError:
        result_label.config(text="มีอะไรผิดพลาดโปรดใส่ข้อมูลให้ครบ")
        start_button.config(state=tk.NORMAL)

def clear_entry(event, name):
    name.delete(0, tk.END)

def check_number(event):
    global set_a
    try:
        if set_a == 1:
            start_count()
        else:
            user_input = entry.get()
            user_word = str(user_input)
            if user_word.lower() == show_text.lower():
                    start_count()
                    entry.delete(0, tk.END)
            else:
                result_label.config(text="ผิด! ลองอีกครั้ง")
    except ValueError:
        result_label.config(text="โปรดใส่ตัวเลขที่ถูกต้อง")

num_show2 = 0
num_show = 0
def show_messagebox():
    global num_show2
    if num_show2 == 0:
        messagebox.showinfo("วิธีการใช้งาเบื้องต้น", "จะมีคำศัพท์และคำอ่านถูกแสดงตรงกลางหน้าจอ ผู้ใช้สามารถกดปุ่มถัดไปเพื่อให้คำสั่งศัพท์ถูกแสดงจนครบกำหนด")
        num_show2 = 1
    else:
        pass

def show_messagebox2():
    global num_show
    if num_show == 0:
        messagebox.showinfo("วิธีการใช้งาเบื้องต้น", "จะมีคำศัพท์และคำอ่านถูกแสดงตรงกลางหน้าจอ ให้ผู้ใช้กรอกตามตัวอักษรที่เห็นและกดปุ่มถัดไป หรือ Enter บนคีย์บอร์ด เพื่อไปคำศัพท์ถัดไป")
        num_show = 1
    else:
        pass


def on_mousewheel(event):
    mycanvas.yview_scroll(-1 * (event.delta // 120), "units")

def on_horizontal_scroll(*args):
    mycanvas.xview(*args)

def show_wordQWQ():

    for widget in myframe.winfo_children():
        if widget.grid_info()['column'] in [0, 1, 2, 3]:
            widget.destroy()

    with open(flie_name, "r", encoding="utf-8") as file:
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
        labels.append(label)
        q = ttk.Label(myframe, text=i+1, font=("Kumothin", 18)).grid(row=i+1, column=0, padx=(20, 30))
        w = ttk.Label(myframe, text=new_array[i, 0], font=("Kumothin", 18)).grid(row=i+1, column=1, padx=(50, 30))
        e = ttk.Label(myframe, text=new_array[i, 1], font=("Kumothin", 18)).grid(row=i+1, column=2, padx=(30, 30))
        r = ttk.Label(myframe, text=new_array[i, 2], font=("Kumothin", 18)).grid(row=i+1, column=3, padx=(20, 25))

    myframe.update_idletasks()
    mycanvas.config(scrollregion=mycanvas.bbox("all"))