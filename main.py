# PROGRAM K01-MIF2123-F01

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : main.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Rabu, 1 Januari 2025
# Deskripsi : Subprogram F01 - Main Program

# KAMUS
# main : procedure
# __name__ : string

# ALGORITMA
from src.main_picture import *

def main() :
    # DESKRIPSI LOKAL
    # Fungsi utama main program.

    # KAMUS LOKAL
    # arg : integer
    # query , database : string

    # ALGORITMA LOKAL
    arg = 1
    print("Selamat Datang!!")
    while (arg != 3) :
        print("===================================")
        print("Pilihan Menu :")
        print("1. Pencarian Gambar Serupa")
        print("2. Image Detailing & Reconstruction")
        print("3. Exit Program")
        print("===================================")
        arg = int(input("Masukkan pilihan Anda (1 / 2 / 3) : "))
        while (not(1 <= arg <= 3)) :
            print("Maaf, input Anda tidak valid!")
            arg = int(input("Masukkan pilihan Anda (1 / 2) : "))
        if (arg == 1) :
            print("==================================================")
            print("Selamat Datang di Menu 1 : Pencarian Gambar Serupa")
            print("==================================================")
            query = str(input("Masukkan path query citra : "))
            database = str(input("Masukkan path database citra : "))
            terminal_information(query , database)
        elif (arg == 2) :
            print("===========================================================")
            print("Selamat Datang di Menu 2 : Image Detailing & Reconstruction")
            print("===========================================================")
            query = str(input("Masukkan path query citra : "))
            rekonstruksi_citra(query)
        else :
            print("============================================")
            print("Menu 3 : Terima Kasih & Sampai Jumpa Kembali")
            print("============================================")
            break

if (__name__ == "__main__") :
    main()