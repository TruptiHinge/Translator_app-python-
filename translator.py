from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

window = Tk()

window.title("Translator")
window.geometry("450x300")
window.config(bg="Blue")

def change(text="type",src="english",dest="marathi"):

    text1 = text
    src1 = src
    dest1 = dest


    trans = Translator()
    trans1 = trans.translate(text,src1=src,dest1=dest)
    return trans1.text()


def data():
    
    s = combo_source.get()
    d = combo_dest.get()
    msg = source_txt.get(1.0,END)
    textGet = change(text=msg, src=s,dest=d)
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textGet)


lab_txt = Label(window,text="Text Translator",font=("Dubai Medium",30),bg="Blue",fg="White",)
lab_txt.place(x=100,y=40,height=50,width=280)

lab_txt = Label(window,text="Source Text",font=("Dubai Medium",20),bg="Blue",fg="Black")
lab_txt.place(x=100,y=100,height=20,width=300)

frame = Frame(window)
frame.pack(side=BOTTOM)


source_txt = Text(frame,font=("Dubai Medium",30),wrap=WORD)
source_txt.place(x=10,y=130,height=80,width=430)

list_text = list(LANGUAGES.values())

combo_source= ttk.Combobox(frame,value=list_text)
combo_source.place(x=10,y=215,height=40,width=130)
combo_source.set("english",)

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=150,y=215,height=40,width=140)

combo_dest = ttk.Combobox(frame,value=list_text)
combo_dest.place(x=300,y=215,height=40,width=140)
combo_dest.set("english")

lab_txt = Label(window,text="Destination Text",font=("Dubai Medium",25),bg="Blue",fg="White")
lab_txt.place(x=100,y=280,height=20,width=300)

destination_txt = Text(frame,font=("Dubai Medium",30),wrap=WORD)
destination_txt.place(x=10,y=320,height=80,width=440)


window.mainloop()