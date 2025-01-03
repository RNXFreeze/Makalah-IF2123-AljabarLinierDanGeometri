# PROGRAM K01-MIF2123-F05

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : data_centering.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Kamis, 2 Januari 2025
# Deskripsi : Subprogram F05 - PCA Computation

# KAMUS
# transpose , multiply , svd_decomposition : function
# make_covarians get_keigen , get_z : procedure

# ALGORITMA
import numpy as np
from data_centering import *

def transpose(matrix : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Membuat fungsi untuk melakukan transpose terhadap suatu matrix.

    # KAMUS LOKAL
    # matrix , res : matrix of float
    # row , col : integer
    # i , j : integer (index)

    # ALGORITMA LOKAL
    row = len(matrix)
    col = len(matrix[0])
    res = [[0.0 for j in range (row)] for i in range (col)]
    for i in range (row) :
        for j in range (col) :
            res[j][i] = matrix[i][j]
    return res

def multiply(m1 : list[list[float]] , m2 : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Membuat fungsi untuk melakukan perkalian terhadap 2 buah matrix.

    # KAMUS LOKAL
    # matrix , res , m1 , m2 : matrix of float
    # row , col , size : integer
    # i , j , k : integer (index)

    # ALGORITMA LOKAL
    row = len(m1)
    col = len(m2[0])
    size = len(m2)
    res = [[0.0 for j in range (col)] for i in range (row)]
    for i in range (row) :
        for j in range (col) :
            for k in range (size) :
                res[i][j] = res[i][j] + (m1[i][k] * m2[k][j])
    return res

def make_covarians(matrix : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Membuat matriks covarians berdasarkan spesifikasi yang diberikan.

    # KAMUS LOKAL
    # matrix , covarians , transposed = matrix of float;
    # n , size : integer
    # i , j : integer (index)

    # ALGORITMA LOKAL
    n = len(matrix)
    transposed = transpose(matrix)
    covarians = multiply(transposed , matrix)
    size = len(covarians)
    for i in range (size) :
        for j in range (size) :
            covarians[i][j] = covarians[i][j] / n
    return covarians

def svd_decomposition(covarians : list[list[float]]) -> tuple[list[list[float]] , list[list[float]] , list[list[float]]] :
    # DESKRIPSI LOKAL
    # Melakukan SVD (Singular Value Decomposition) menggunakan fungsi bantuan dari numpy.

    # KAMUS LOKAL
    # matrix , covarians , eigen_vector , diagonal_matrix , singular_value : matrix of float

    # ALGORITMA LOKAL
    matrix = np.array(covarians)
    eigen_vector , diagonal_matrix , singular_value = np.linalg.svd(matrix)
    diagonal_matrix = np.diag(diagonal_matrix)
    return (eigen_vector , diagonal_matrix , singular_value)

def get_keigen(matrix : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Menghitung matrix Z berdasarkan perkalian matrix yang sudah distandarisasi dan eigen_vector sebanyak rank.

    # KAMUS LOKAL
    # matrix , covarians , eigen_vector , k_eigen_vector : matrix of float
    # k , size : integer
    # i , j : integer (index)

    # ALGORITMA LOKAL
    matrix = data_centering(matrix)
    covarians = make_covarians(matrix)
    (eigen_vector , _ , _) = svd_decomposition(covarians)
    k = np.linalg.matrix_rank(np.array(matrix))
    size = len(eigen_vector)
    k_eigen_vector = [[0.0 for j in range (k)] for i in range (size)]
    for i in range (size) :
        for j in range (k) :
            k_eigen_vector[i][j] = eigen_vector[i][j]
    return k_eigen_vector

def get_z(matrix : list[list[float]] , k_eigen_vector : list[list[float]]) -> list[list[float]] :
    # DESKRIPSI LOKAL
    # Menghitung matrix Z berdasarkan perkalian matrix yang sudah distandarisasi dan eigen_vector sebanyak rank.

    # KAMUS LOKAL
    # matrix , k_eigen_vector , res : matrix of float
    # i , j : integer (index)

    # ALGORITMA LOKAL
    matrix = data_centering(matrix)
    res = multiply(matrix , k_eigen_vector)
    return res