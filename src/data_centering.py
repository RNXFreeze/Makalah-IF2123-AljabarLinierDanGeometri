# PROGRAM K01-MIF2123-F01

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : data_centering.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Rabu, 1 Januari 2025
# Deskripsi : Subprogram F02 - Data Centering

# KAMUS
# find_average : function
# data_centering : procedure

# ALGORITMA
def find_average(matrix : list[list[float]]) -> list[float] :
    # DESKRIPSI LOKAL
    # Sebuah fungsi untuk menghitung rata-rata intensitas di posisi yang bersesuaian.

    # KAMUS LOKAL
    # matrix : matrix of float
    # avg : list of float
    # row , col : integer
    # i , j : integer (index)

    # ALGORITMA LOKAL
    row = len(matrix)
    col = len(matrix[0])
    avg = [0.0 for i in range (col)]
    for i in range (row) :
        for j in range (col) :
            avg[j] = avg[j] + matrix[i][j]
    for i in range (len(avg)) :
        avg[i] = avg[i] / row
    return avg

def data_centering(matrix : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Sebuah prosedur untuk mengurangi nilai setiap elemen intensitas dengan rata-rata yang bersesuaian.

    # KAMUS LOKAL
    # matrix : matrix of float
    # avg : list of float
    # row , col : integer
    # i , j : integer (index)

    # ALGORITMA LOKAL
    avg = find_average(matrix)
    row = len(matrix)
    col = len(matrix[0])
    for i in range (row) :
        for j in range (col) :
            matrix[i][j] = matrix[i][j] - avg[j]
    return matrix