# PROGRAM K01-GeprekMumbul-F08

# IDENTITAS
# Kelompok     : 01 - Geprek Mumbul
# NIM/Nama - 1 : 13523021 - Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 13523044 - Muhammad Luqman Hakim
# NIM/Nama - 3 : 13523092 - Muhammad Izzat Jundy
# Instansi     : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan      : Teknik Informatika (IF)
# Nama File    : retrival_output.py
# Topik        : Tugas Besar 2 Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal      : Senin, 16 Desember 2024
# Deskripsi    : Subprogram F08 - Retrival & Output
# PJ F08       : 13523021 - Muhammad Raihan Nazhim Oktana

# KAMUS
# picture_index : function
# information_retrival , display_output , array_names_percents : procedure

# ALGORITMA
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
from PIL import Image
from similarity_computation import *

def picture_index(folder_path : str , index : int) -> tuple[str , str] :
    # DESKRIPSI LOKAL
    # Fungsi untuk mengambil path dan name dari file picture pada indeks yang diinginkan.

    # KAMUS LOKAL
    # folder , images : list of string
    # file , name , path , folder_path : string
    # index : integer

    # ALGORITMA LOKAL
    folder = os.listdir(folder_path)
    images = []
    for file in folder :
        if (file.lower().endswith(('.jpg' , '.png' , '.jpeg'))) :
            images.append(file)
    name = images[index]
    path = os.path.join(folder_path , name)
    return (path , name)

def information_retrival(query : list[float] , matrix : list[list[float]] , type : str , database : str , audio_type : str) -> None :
    # DESKRIPSI LOKAL
    # Fungsi untuk melakukan proses pencarian informasi dan melempar ke tipe fungsi output yang bersesuaian.

    # KAMUS LOKAL
    # query , percent : list of float
    # matrix : matrix of float
    # data : list of tuple of integer and float
    # type , database , audio_type : string

    # ALGORITMA LOKAL
    (data , percent) = jarak_euclidean(query , matrix)
    audio_type = "Waveform"
    return display_output(data , percent , type , database , audio_type)

def array_names_percents(data : list[tuple[int , float]] , percent : list[float] , type : str , database : str) -> list[tuple[str , float]] :
    # DESKRIPSI LOKAL
    # Fungsi untuk mengembalikan kumpulan nama file hasil pencarian yang telah terurut.

    # KAMUS LOKAL
    # data : list of tuple of integer and float
    # type , database , name : string
    # percent : list of float
    # res : list of tuple of string and float
    # size : integer
    # i : integer (index)

    # ALGORITMA LOKAL
    size = len(data)
    res = [["" , 0.0] for i in range (size)]
    for i in range (len(data)) :
        (_ , name) = picture_index(database , data[i][0] - 1)
        res[i][0] = name
        res[i][1] = percent[i]
    return res

def display_output(data : list[tuple[int , float]] , percent : list[float] , type : str , database : str , audio_type : str) -> None :
    # DESKRIPSI LOKAL
    # Fungsi untuk menampilkan output berupa urutan hasil query yang tepat ke layar.

    # KAMUS LOKAL
    # data : list of tuple of integer and float
    # percent : list of float
    # type , database , path , name , audio_type : string

    # ALGORITMA LOKAL
    if (len(data) > 0) :
        if (type == "picture") :
            print("Berikut adalah daftar informasi gambar yang serupa :")
            for i in range (len(data)) :
                (path , name) = picture_index(database , data[i][0] - 1)
                print(f"{i + 1}. {name}\t({percent[i]}%)")
                Image.open(path)
    else :
        print("Tidak ada daftar informasi gambar pada database yang serupa dengan query (≥55%).")