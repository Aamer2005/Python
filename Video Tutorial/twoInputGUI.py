from tkinter import *
from PIL import ImageTk,Image


def calulate_sum():
    var1 = float(input1.get())
    var2 = float(input2.get())
    operation = input3.get()
    
    result=''
    if operation=='+':
        result=var1+var2
    elif operation=='-':
        result=var1-var2
    elif operation=='*':
        result=var1*var2
    elif operation=='/':
        result=var1/var2
    else:
        second = Tk()
        second.mainloop()

    str = 'OUTPUT : {}'.format(result)
    output_label.config(text=str)


root = Tk()

root.title("Calculator")
root.minsize(250,350)
root.configure(background='#0096DC')


input_label1 = Label(root,text='Enter INPUT 1 ',bg='black',fg='white')
input_label1.pack(pady=(10,5))
input1 = Entry(root,width=30)
input1.pack(pady=(10,10))

input_label2 = Label(root,text='Enter INPUT 2 ',bg='black',fg='white')
input_label2.pack(pady=(10,5))
input2 = Entry(root,width=30)
input2.pack(pady=(10,10))

input_label3 = Label(root,text='Enter Operation ',bg='black',fg='white')
input_label3.pack(pady=(10,5))
input3 = Entry(root,width=30)
input3.pack(pady=(10,10))

output_label = Label(root,text='OUTPUT',bg='black',fg='white')
output_label.pack(pady=(10,5))

btn_label = Button(root,text="Answer",bg='red',fg='black',width=25,command=calulate_sum)
btn_label.pack(pady=(10,10))

root.mainloop()