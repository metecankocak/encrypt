from tkinter import *
from PIL import ImageTk, Image



window = Tk()

window.title("IDK")

window.minsize(350,700)

img = ImageTk.PhotoImage(Image.open("topsecret.png"))
panel = Label(window, image = img, height=220, width=200)
panel.pack(fill = "both")





window.mainloop()

