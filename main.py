from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("IDK")

window.minsize(350,700)

img = ImageTk.PhotoImage(Image.open("topsecret.png"))
panel = Label(window, image = img, height=220, width=200)
panel.pack(fill = "both")

title_label= Label(text="Lütfen dosyanızın adını yazın.",)
title_label.pack()
title_entry = Entry(width=30)
title_entry.pack()

text_label= Label(text="Lütfen şifrelemek istediğiniz metni yazın.")
text_label.pack()
my_text= Text(height=10, width=40)
my_text.pack()








window.mainloop()

