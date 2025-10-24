from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_img():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter+=1
    
counter = 1 #global var
root = Tk()
root.minsize(300,400)
root.title('Wallpaper Changer')
root.config(background='black')

head_label=Label(root,text='Image Slider',bg='red',fg='white',width=30,height=3)
head_label.pack(pady=(10,10))

files = os.listdir('wallpapers')

img_arr = []
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_arr[0])
img_label.pack(pady=(10,10))


btn = Button(root,text='Next',bg='white',fg = 'black',width=30,height=3,command=rotate_img)
btn.pack(pady=(10,10))
root.mainloop()
