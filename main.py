import tkinter as tk
from tkinter import ttk, PhotoImage
import random

def change_image():
    global image_counters
    
    random_image = random.choice(myArray)
    image_counters[random_image] += 1
    
    img = PhotoImage(file=random_image).subsample(1)
    canvas.itemconfig(image_item, image=img)
    canvas.image = img
    
    update_counters_label()

def update_counters_label():
    count_label2.config(text=f"Ön üz: {image_counters['coin1.png']}/{sum(image_counters.values())}")
    count_label3.config(text=f"Arxa üz: {image_counters['coin2.png']}/{sum(image_counters.values())}")

root = tk.Tk()
root.title("Metal pul atma")
root.configure(bg='gray')

canvas = tk.Canvas(root, width=530, height=330, bg='gray')
canvas.pack()

canvas.create_rectangle(10, 10, 320, 320, fill="green")
for i, coords in enumerate([(330, 10, 520, 155), (330, 165, 520, 320)]):
    canvas.create_rectangle(*coords, fill="lightyellow")
    canvas.create_text(425, 90 + i * 160, font=("Arial", 24), fill="white")

myArray = ['coin1.png', 'coin2.png']

image_counters = {image: 0 for image in myArray}

img = PhotoImage()  
image_item = canvas.create_image(20, 20, anchor=tk.NW, image=img)

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=5, background='#4CAF50', foreground='black')

button = ttk.Button(root, text="Qəpiyi at", command=change_image, style='TButton')
button.pack(pady=10)

count_label2 = tk.Label(root, bg='lightyellow', font=('Arial', 15))
count_label2.place(x=370, y=70)

count_label3 = tk.Label(root, bg='lightyellow', font=('Arial', 15))
count_label3.place(x=370, y=230)

root.mainloop()
