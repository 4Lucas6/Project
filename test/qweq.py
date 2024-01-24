import tkinter as tk

def draw_canvas_with_red_border():
    root = tk.Tk()
    root.title("Canvas with Red Border")
    root.configure(bg='#D3F2FF')
    canvas_width = 400
    canvas_height = 300
    border_width = 5
    
    

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bd=border_width)
    canvas.pack()

    # สร้างสี่เหลี่ยมพื้นหลังสีขาว
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill='red')

    root.mainloop()

# เรียกฟังก์ชันเพื่อแสดงผล
draw_canvas_with_red_border()
