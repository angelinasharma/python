import tkinter
import time
from typing_extensions import Text


window = tkinter.Tk()
window.wm_minsize(width=512, height=512)

def button_clicked():
    Text1.config(text="Aah, liked that!!")
    time.sleep(1)
    Text1.config(text="Press the button...")

Text1 = tkinter.Label(text="Press the button...").place(x = 200, y = 0)

Button1 = tkinter.Button(text="Press Me", command=button_clicked)
Button1.pack()

window.mainloop()
