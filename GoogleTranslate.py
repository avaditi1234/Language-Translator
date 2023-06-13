from tkinter import*
from tkinter import ttk
# Translator-class,googletrans-module,languages-part of a module
from googletrans import Translator,LANGUAGES
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    #translate is a function of class Translator
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text
#for fetching data
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    #from starting to end(1 to end)
    msg = Sor_txt.get(1.0,END)
    textget = change(text=msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Light Blue')

lab_txt=Label(root,text="Translator",font=("Time New Roman",35,"bold"),bg='White')
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg='Black',bg='Light Blue')
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt=Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text= list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")
#3d view-relief raised
#command is a keyword to use the builtin function data
button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Converted Text",font=("Time New Roman",20,"bold"),bg='Light Blue')
lab_txt.place(x=100,y=360,height=20,width=300)
#destination
dest_txt=Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)
root.mainloop()