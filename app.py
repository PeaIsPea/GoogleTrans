from tkinter import*
from PIL import Image, ImageTk
from googletrans import Translator

root = Tk()
root.title('Google Spider')
root.geometry("500x630")
root.iconbitmap('logo.ico')

bg = Image.open('bg.jpg')
render = ImageTk.PhotoImage(bg)
img = Label(root,image=render)
img.place(x=0,y=0)

name = Label(root,text ="MARVEL",fg="#FFFFFF",bd = 0,bg ="#FF0000")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box = Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)


def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    t= Translator()
    a= t.translate(INPUT, src="vi",dest="en")
    b= a.text
    box1.insert(END,b)



clear_btn =Button(button_frame,text="Clear",font=(("Arial"),10,'bold'),bg='#FF0000',fg='#FFFFFF',command=clear)
clear_btn.place(x = 290, y= 310)

tran_btn =Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg='#FF0000',fg='#FFFFFF',command=translate)
tran_btn.place(x = 150, y= 310)

box1= Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)




root.mainloop()