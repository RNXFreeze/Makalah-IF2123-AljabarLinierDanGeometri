# PROGRAM K01-MIF2123-F03

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : data_centering.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Kamis, 2 Januari 2025
# Deskripsi : Subprogram F03 - Picture Conversion

# KAMUS
# convert_picture , data_picture : procedure

# ALGORITMA
import os
from PIL import Image

def convert_picture(path : str) -> list[float] :
    # SPESIFIKASI LOKAL
    # Melakukan konversi gambar menjadi pixel RGB dengan bantuan PIL, lalu menyimpan hasil intensitasnya pada list of float.

    # KAMUS LOKAL
    # img : ImageFile
    # pixels : list of tuple of integer
    # res : list of float
    # path : string
    # size , n : integer
    # i : integer (index)

    # ALGORITMA LOKAL
    n = 32
    img = Image.open(path)
    img = img.resize((n , n) , Image.Resampling.LANCZOS)
    img = img.convert('RGB')
    pixels = list(img.getdata())
    size = n * n
    res = [0.0 for i in range (size)]
    for i in range (size) :
        res[i] = 0.2989 * pixels[i][0] + 0.5870 * pixels[i][1] + 0.1140 * pixels[i][2]
    return res

def data_picture(path_folder : str) -> list[list[float]] :
    # SPESIFIKASI LOKAL
    # Melakukan konversi semua file dalam suatu folder database menjadi list of vektor (list of float) / matrix of float.

    # KAMUS LOKAL
    # res : matrix of float
    # temp : list of float
    # path_folder , path_file , name : string

    # ALGORITMA LOKAL
    res = []
    for name in os.listdir(path_folder) :
        path_file = os.path.join(path_folder, name)
        if name.lower().endswith(('.png' , '.jpg' , '.jpeg')) :
            temp = convert_picture(path_file)
            res.append(temp)
    return res