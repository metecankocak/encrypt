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
my_text= Text(height=15, width=45)
my_text.pack()

password_label= Label(text= "Lütfen şifrenizi giriniz.")

password_label.pack()
password_entry = Entry(width=30, )
password_entry.pack()

save_button = Button(text="Kaydet ve şifrele")
save_button.pack()

decrypt_button=Button(text="şifreyi çöz")
decrypt_button.pack()

my_text.pack()








window.mainloop()

