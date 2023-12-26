import tkinter as tk
from tkinter import PhotoImage
import random
import pygame
from PIL import Image, ImageTk
import imageio
spisokvse=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
spisokbuk=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spisokcif=['0','1','2','3','4','5','6','7','8','9']
a=[]
b=[]
c=[]
d=[]
a.append(random.choice(spisokvse))
b.append(random.choice(spisokvse))
c.append(random.choice(spisokvse))
d.append(random.choice(spisokvse))

for i in range(1,4):
    if any(item in a for item in spisokcif):
        a.append(random.choice(spisokbuk))
    else:
        a.append(random.choice(spisokvse))
    if i==3 and not any(item in a for item in spisokcif):
        a=a[:-1]
        a.append(random.choice(spisokcif))

for i in range(1,4):
    if any(item in b for item in spisokcif):
        b.append(random.choice(spisokbuk))
    else:
        b.append(random.choice(spisokvse))
    if i==3 and not any(item in b for item in spisokcif):
        b=b[:-1]
        b.append(random.choice(spisokcif))
    
for i in range(1,4):
    if any(item in c for item in spisokcif):
        c.append(random.choice(spisokbuk))
    else:
        c.append(random.choice(spisokvse))
    if i==3 and not any(item in c for item in spisokcif):
        c=c[:-1]
        c.append(random.choice(spisokcif))

for i in range(1,4):
    if any(item in d for item in spisokcif):
        d.append(random.choice(spisokbuk))
    else:
        d.append(random.choice(spisokvse))
    if i==3 and not any(item in d for item in spisokcif):
        d=d[:-1]
        d.append(random.choice(spisokcif))

akod=''.join(a)
bkod=''.join(b)
ckod=''.join(c)
dkod=''.join(d)
correct_code= akod + bkod + ckod + dkod
print('код=',correct_code)

def check_code():
    entered_code = code_entry.get() + code_entry2.get() + code_entry3.get() + code_entry4.get()
    if entered_code == correct_code:
        result_label.config(text="Код верный")
    else:
        result_label.config(text="Код неверный")

root = tk.Tk()
root.geometry('1024x720')
root.title("Проверка кода")

bg_image = tk.PhotoImage(file='neeko.ppm')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


gif_path = "neeko.gif" 
gif = imageio.mimread(gif_path)
frame_image = Image.fromarray(gif[0])
frame_photo = ImageTk.PhotoImage(frame_image)

label = tk.Label(root, image=frame_photo)
label.pack()

def update_frame(idx):
    frame_image = Image.fromarray(gif[idx])
    frame_photo = ImageTk.PhotoImage(frame_image)
    label.configure(image=frame_photo)
    label.image = frame_photo
    root.after(50, update_frame, (idx + 1) % len(gif))

update_frame(0)

code_entry = tk.Entry(root, width=8)
code_entry.pack(pady=10)

code_separator = tk.Label(root, text="-")
code_separator.pack()

code_entry2 = tk.Entry(root, width=8)
code_entry2.pack(pady=10)

code_separator2 = tk.Label(root, text="-")
code_separator2.pack()

code_entry3 = tk.Entry(root, width=8)
code_entry3.pack(pady=10)

code_separator3 = tk.Label(root, text="-")
code_separator3.pack()

code_entry4 = tk.Entry(root, width=8)
code_entry4.pack(pady=10)


pygame.init()

check_button = tk.Button(root, text="Проверить", command=check_code)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

audio_file = "neeko.mp3"
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(-1)

input("Нажмите Enter, чтобы остановить проигрывание...")

root.mainloop()