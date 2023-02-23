import sys

def tampilkanMenu():
    print("===========================")
    print("=    Pilihan Phone Book   =")
    print("===========================")
    print("= 1. lihat semua kontak   =")
    print("= 2. menambah kontak baru =")
    print("= 3. hapus kontak         =")
    print("= 4. cari kontak          =")
    print("= 5. update nama kontak   =")
    print("= 6. update nomor kontak  =")
    print("= 7. keluar               =")
    print("===========================")
    

def lihatKontak():
    file = open("Contact Book.txt", "r")
    print(file.read())

def tambahKontak():
    inputUser= input("Masukkan nama dan nomor telepon (nama -- nomor): ")
    print("Nomor telepon berhasil ditambahkan")
    file = open("Contact Book.txt", "a")
    file.write("\n")
    file.write(inputUser)

def hapusKontak():
    nama= input("Masukkan nama kontak yang ingin dihapus: ")
    with open("Contact Book.txt", "r") as file:
        lines = file.read()
    with open("Contact Book.txt", "w") as file:
        removed=False
        for line in lines:
            if not nama.lower() in lines.lower():
                file.write(line)
            else:
                removed=True
        if removed:
            print(f"Kontak berhasil dihapus")
        else:
            print(f"kontak tidak ditemukan")

def cariKontak(nama):
    with open("Contact Book.txt", "r") as file:
        isi=file.read()
        if nama in isi:
            print("Kontak terdaftar\n")
        else:
            print("Kontak tidak terdaftar")

def updateNama():
    nama= input("Masukkan nama kontak: ")
    namaBaru= input("Masukkan nama baru: ")
    file = open("Contact Book.txt", "r")
    text= file.read()
    textBaru= text.replace(nama, namaBaru)
    file = open("Contact Book.txt", "w")
    file.write(textBaru)
    print("Nama kontak telah diupdate")

def updateNomor():
    nomor= input("Masukkan nomor kontak: ")
    nomorBaru= input("Masukkan nomor baru: ")
    file = open("Contact Book.txt", "r")
    text= file.read()
    textBaru= text.replace(nomor, nomorBaru)
    file = open("Contact Book.txt", "w")
    file.write(textBaru)
    print("Nomor kontak telah diupdate")


    




while True:
    tampilkanMenu()
    pilih = int(input("Apa yang ingin kamu lakukan(1-7): "))
    if pilih == 1:
        lihatKontak()
        input()
    elif pilih==2:
        tambahKontak()
        input()
    elif pilih==3:
        hapusKontak()
        input()
    elif pilih==4:
        nama= input("Nama kontak yang ingin dicari: ")
        cariKontak(nama)
        input()
    elif pilih==5:
        updateNama()
        input()
    elif pilih==6:
        updateNomor()
        input()
    else:
        print("Terimakasih telah menggunakan phone book!")
        sys.exit()



