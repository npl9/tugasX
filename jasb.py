from tkinter import *

root = Tk()

#mengubah background
root.config(background="navy blue")

label = Label(text="Informatika", font="Normal 25", background="navy blue", fg="white")

#label.pack()
label.grid(row=0, column=0)

#Entri digunakam untuk menginput data
data = Entry(font="Normal 20", bd=10)
data.grid(row=1, column=0)

def perintah():
    print(data.get())

    data.delete(0, END)

button = Button(text="-->", font="Normal 15", activebackground="orange", command=perintah)

button.grid(row=1, column=2)

teks = Text(width=30, height=30, bd=10, font="Normal 10")

teks.grid(row=2, column=2)

root.mainloop()