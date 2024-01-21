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
from page_3 import open_page3
from page_4 import open_page4

num_show2 = 0
num_show = 0
a = 0
set_a = 0

#################################################################
def get_dataword_file():
    try:
        with open("dataword_status.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "dataword1.txt"  # ใช้ค่าเริ่มต้นหากไม่พบไฟล์
        
file_name = get_dataword_file()

# แก้ไขฟังก์ชัน 'check_dataword_file'
def check_dataword_file():
    current_file = get_dataword_file()
    if current_file == "dataword2.txt":
        tk.messagebox.showinfo("Dataword File Check", "Currently using dataword2.txt")
    elif current_file == "dataword3.txt":
        tk.messagebox.showinfo("Dataword File Check", "Currently using dataword3.txt")
    else:
        tk.messagebox.showinfo("Dataword File Check", "Not using dataword2.txt or dataword3.txt")


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
        
        
def check_for_dataword_change():
    # ตรวจสอบไฟล์ชั่วคราวเพื่อดูว่ามีการเปลี่ยนแปลงไฟล์ dataword หรือไม่
    try:
        with open("temp_dataword_file.txt", "r") as file:
            dataword_file = file.read().strip()
            return dataword_file
    except FileNotFoundError:
        return "dataword1.txt"
#################################################################   
show_text = ""
count = 0
count2 = 0
check_buttom = 0

  

"""
def closeAll():
    root.destroy() 
    add_txt_windows.destroy()
"""  

##########################

def open_page1():
    
    root = tk.Tk()
    root.title("ตัวอย่างโปรแกรมที่ใช้ ttk")
    ##root.resizable(False, False)
    root.minsize(width=550, height=250)
    root.maxsize(width=650, height=550)
    root.configure(bg='#D3F2FF')

    
    frame = tk.Frame(root,bg='#D3F2FF')
    frame.grid(row=0,column=0,padx=50)

    frame2 = tk.Frame(frame,bg='#D3F2FF')
    frame2.grid(row=3, column=0, pady=10)

    frame3 = tk.Frame(frame,bg='#D3F2FF')
    frame3.grid(row=6, column=0, pady=10)

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

    load_dataword_data()
    num = ttk.Entry(frame3,width=11,font=("Kumothin", 14))
    num.insert(0,"กรอกจำนวนคำศัพท์")
    num.bind("<Button-1>", lambda event,name=num:clear_entry(event,name))
    num.grid(row=2,column=1,padx=7)

    photo1 = tk.PhotoImage(file="next2.png")
    photo2 = tk.PhotoImage(file="playsong2.png")
    photo3 = tk.PhotoImage(file="rerun2.png")
    photo4 = tk.PhotoImage(file="up2.png")
    photo5 = tk.PhotoImage(file="random2.png")
    photo6 = tk.PhotoImage(file="playpro2.png")
    photo7 = tk.PhotoImage(file="test2.png")
    photo8 = tk.PhotoImage(file="group.png")
    photo9 = tk.PhotoImage(file="quiz.png")
    photo1H = tk.PhotoImage(file="rerun_h.png")
    photo2H = tk.PhotoImage(file="random_h.png")

    style = ttk.Style()
    style.configure("TButton", font=("Kumothin", 18))
#################################################################
    check_button = tk.Button(root, text="Check Dataword File", command=check_dataword_file)
    check_button.grid(row=0,column=0,pady=5,sticky='e')
#################################################################
    manual_button = ttk.Button(frame, text="คู่มือ",width=5)
    manual_button.grid(row=0,column=0,pady=5,sticky='e')

    label = tk.Label(frame, text="คำศัพท์", font=("Kumothin", 30, "bold"),bg='#D3F2FF')
    label.grid(row=0,column=0)

    labelread = tk.Label(frame,text="คำอ่าน",font=("Kumothin", 25, "bold"),bg='#D3F2FF')
    labelread.grid(row=1,column=0)

    entry = ttk.Entry(frame, text="input words",width=40,font=("Kumothin", 16),justify='center')
    entry.insert(0,"กรอกข้อความ")
    entry.bind("<Button-1>", lambda event,name=entry:clear_entry(event,name))
    entry.bind("<Return>", check_number)
    entry.grid(row=2,column=0,pady=5)

    ok_button = tk.Button(frame, image=photo1,borderwidth=0, bg='#D3F2FF',command=lambda event=None:check_number(event))
    ok_button.grid(row=3,column=0,pady=5)

    read_and_Type = tk.Button(frame, image=photo7,borderwidth=0, bg='#D3F2FF',command=lambda:(start_count(),show_messagebox2()))
    read_and_Type.grid(row=4,column=0,padx=(5,0),sticky='w')


    play_mp3_button = tk.Button(frame, image=photo2,borderwidth=0, bg='#D3F2FF',command=play_mp3)
    play_mp3_button.grid(row=4,column=0,padx=(0,5),sticky='e')

    loop_buttom = tk.Button(frame, image=photo3,borderwidth=0, bg='#D3F2FF',command=set_count_to_zero)
    loop_buttom.grid(row=5,column=0,padx=7,pady=5,sticky='w')


    add_word_button = tk.Button(frame, image=photo4,borderwidth=0, bg='#D3F2FF', command=lambda: open_page2(root))
    add_word_button.grid(row=5,column=0,padx=7,pady=5,sticky='e')


    show_word = "คำศัพท์ที่มีทั้งหมด = " + str(num_row)
    result_label = tk.Label(frame3,text=show_word,font=("Kumothin", 20, "normal"),bg='#D3F2FF')
    result_label.grid(row=1,column=0,columnspan=4,pady=(0,5))

    reset_buttom = tk.Button(frame3, image=photo5,borderwidth=0, bg='#D3F2FF',command=reset_word)
    reset_buttom.grid(row=2,column=0,padx=7)


    loop_buttom.config(state=tk.DISABLED)
    reset_buttom.config(state=tk.DISABLED)

    

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


    start_button = tk.Button(frame3, image=photo6,borderwidth=0, bg='#D3F2FF',command=lambda: (start_count(),set_global_a(),show_messagebox()))
    start_button.grid(row=2,column=2,padx=7)

    group_button = tk.Button(frame,image=photo8,borderwidth=0, bg='#D3F2FF', command=lambda: open_page4(root))
    group_button.grid(row=7,column=0,padx=7,pady=5,sticky='w')

    quiz_button = tk.Button(frame,image=photo9,borderwidth=0, bg='#D3F2FF', command=lambda: open_page3(root))
    quiz_button.grid(row=7,column=0,padx=7,pady=5,sticky='e')

    
    root.mainloop()

if __name__ == "__main__":
    open_page1()