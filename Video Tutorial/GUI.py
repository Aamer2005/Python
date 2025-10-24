from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email=='aamer' and password=='1234':
        messagebox.showinfo('Login Successfull')
    else :
        messagebox.showerror('Login Failed')

root = Tk()

root.title("Login Form")
root.iconbitmap('web-logo.ico')

#size the window
root.minsize(400,500)
root.maxsize(1000,1100)
#root.geometry('200x350')

root.configure(background='#0096DC')

img = Image.open('web-logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text='Art',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack()
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))#ipady->height of input

password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack()
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))#height of input

login_btn = Button(root,text='Submit',bg = 'white',fg='black',width=30,height=3,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

root.mainloop()