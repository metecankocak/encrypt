import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
from cryptography.fernet import Fernet


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
title_entry.get()
title_entry.focus()

text_label= Label(text="Lütfen şifrelemek istediğiniz metni yazın.")
text_label.pack()
my_text= Text(height=15, width=45)
my_text.pack()
my_text.get("1.0", END)

password_label= Label(text= "Lütfen şifrenizi giriniz.")

password_label.pack()
password_entry = Entry(width=30, )
password_entry.pack()
password_entry.get()

my_box= tkinter.messagebox


key = Fernet.generate_key()
cipher_suite = Fernet(key)

def click_save():

    if password_entry.get() != "mete":
        my_box.showinfo("Bilgi", "Hatalı şifre girdiniz.")

    elif not title_entry.get():
        my_box.showinfo("Bilgi", "dosya adı boş bırakılamaz.")
    elif not my_text.get("1.0", END):
        my_box.showinfo("Bilgi", "metin kutusunu boş bırakamazsınız.")
    elif not password_entry.get():
        my_box.showinfo("Bilgi", "şifre alanını boş bırakamazsınız.")
    else:
        secret_text = str(cipher_suite.encrypt(my_text.get("1.0", END).encode()))
        with (open("şifeler.txt", "r+", encoding="utf-8") as file):
            file.read()
            file.write(f"{title_entry.get()}, dosyasının şifresi:\n")

            file.write(secret_text)
            file.write("\n------------------------\n")





def click_decrypt():
    pass


save_button = Button(text="Kaydet ve şifrele", command=click_save)
save_button.pack()

decrypt_button=Button(text="şifreyi çöz")
decrypt_button.pack()

my_text.pack()





window.mainloop()

