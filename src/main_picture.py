# PROGRAM K01-MIF2123-F01

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : main_picture.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Rabu, 1 Januari 2025
# Deskripsi : Subprogram F01 - Main Picture

# KAMUS
# terminal_information : procedure

# ALGORITMA
from picture_conversion import *
from data_centering import *
from pca_computation import *
from similarity_computation import *
from retrieval_output import *

def terminal_information(query : str , type : str , database : str) -> None :
    # DESKRIPSI LOKAL
    # Fungsi untuk melakukan proses pencarian informasi dan melempar ke tipe fungsi output yang bersesuaian.

    # KAMUS LOKAL
    # list_query , avg : list of float
    # matrix , matrix_query : matrix of float
    # type , database , audio_type , query : string
    # size : integer
    # i : integer (index)

    # ALGORITMA LOKAL
    audio_type = "Waveform"
    if (type == "picture") :
        matrix = data_picture(database)
        if (len(matrix) > 1) :
            avg = find_average(matrix)
            matrix = data_centering(matrix)
            list_query = convert_picture(query)
            size = len(list_query)
            for i in range (size) :
                list_query[i] = list_query[i] - avg[i]
            information_retrival(list_query , matrix , type , database , audio_type)
        else :
            print("Error : Database terlalu sedikit, minimal ada 2 buah data.")