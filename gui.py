from tkinter import *

root = Tk()
root.title("Aplikasi Kurir")
root.geometry("500x500")

def Hitung():
    if radioJenis.get() == 'r':
        harga = reguler*int(inputBerat.get())*int(inputJarak.get())
        if radioAsuransi.get() == 'y':
            asuransi = 0.05*harga
            harga = harga + asuransi
        else: 
            asuransi =0
        
    else:
        Harga = express*int(inputBerat.get())*int(inputJarak.get())
        if radioAsuransi.get() == 'y':
            asuransi = 0.05*harga
            harga = harga + asuransi
        else:
            asuransi =0

    labelHasil = Label(root, text=f'''
================== TOTAL HARGA ==================
Nama : {inputNama.get()}
Jarak : {inputJarak.get()}
Berat : {inputBerat.get()}
Jenis : {radioJenis.get()}
Asuransi : {asuransi}
Total Harga : {harga}    
''')
    labelHasil.grid(column=0, row=7)


reguler = 9000
express = 18000

labelNama = Label(root, text="Nama Pengirim =")
labelJarak = Label(root, text="Jarak Pengiriman =")
labelBerat = Label(root, text="Berat Barang =")
labelJenis = Label(root, text="Jenis Pengiriman =")
labelAsuransi = Label(root, text="Asuransi =")

labelNama.grid(column=0, row=1)
labelJarak.grid(column=0, row=2)
labelBerat.grid(column=0, row=3)
labelJenis.grid(column=0, row=4)
labelAsuransi.grid(column=0, row=5)

inputNama = Entry(root, width=10)
inputJarak = Entry(root, width=10)
inputBerat = Entry(root, width=10)

inputNama.grid(column=1, row=1)
inputJarak.grid(column=1, row=2)
inputBerat.grid(column=1, row=3)

radioJenis = StringVar()
radioJenis1 = Radiobutton(root, value='r', variable=radioJenis, text="Reguler")
radioJenis2 = Radiobutton(root, value='e', variable=radioJenis, text="Express")

radioJenis1.grid(column=1, row=4)
radioJenis2.grid(column=2, row=4)

radioAsuransi = StringVar()
radioAsuransi1 = Radiobutton(root, value='y', variable=radioAsuransi, text="Ya")
radioAsuransi2 = Radiobutton(root, value='t', variable=radioAsuransi, text="Tidak")

radioAsuransi1.grid(column=1, row=5)
radioAsuransi2.grid(column=2, row=5)

button = Button(root, text="Hitung", command=Hitung)
button.grid(column=0, row=6)




root.mainloop()