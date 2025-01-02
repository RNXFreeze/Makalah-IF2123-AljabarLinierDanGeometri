# PROGRAM K01-MIF2123-F02

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : main_picture.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Rabu, 1 Januari 2025
# Deskripsi : Subprogram F02 - Main Picture

# KAMUS
# terminal_information , image_detailing : procedure

# ALGORITMA
from picture_conversion import *
from data_centering import *
from pca_computation import *
from noise_reduction import *
from similarity_computation import *
from retrieval_output import *

def terminal_information(query : str , database : str) -> None :
    # DESKRIPSI LOKAL
    # Fungsi untuk melakukan proses pencarian informasi dan melempar ke tipe fungsi output yang bersesuaian.

    # KAMUS LOKAL
    # list_query , avg : list of float
    # matrix , matrix_query : matrix of float
    # database , query : string
    # size : integer
    # i : integer (index)

    # ALGORITMA LOKAL
    matrix = data_picture(database)
    if (len(matrix) > 1) :
        avg = find_average(matrix)
        matrix = data_centering(matrix)
        list_query = convert_picture(query)
        size = len(list_query)
        for i in range (size) :
            list_query[i] = list_query[i] - avg[i]
        information_retrival(list_query , matrix , database)
    else :
        print("Error : Database terlalu sedikit, minimal ada 2 buah data.")

def image_detailing(query : str) -> None :
    # DESKRIPSI LOKAL
    # Fungsi untuk melakukan proses rekonstruksi citra dengan image detailing.

    # KAMUS LOKAL
    # query : string

    # ALGORITMA LOKAL
    rekonstruksi_citra(query)