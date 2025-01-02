# PROGRAM K01-MIF2123-F06

# IDENTITAS
# Nama      : Muhammad Raihan Nazhim Oktana
# NIM       : 13523021
# Instansi  : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Jurusan   : Teknik Informatika (IF)
# Nama File : noise_reduction.py
# Topik     : Makalah Aljabar Linier dan Geometri 2024 (IF2123-24)
# Tanggal   : Kamis, 2 Januari 2025
# Deskripsi : Subprogram F06 - Noise Reduction

# KAMUS
# reduksi_noise , konstruksi_citra : procedure

# ALGORITMA
import numpy as np
import cv2
import matplotlib.pyplot as plt

def reduksi_noise(image) :
    # DESKRIPSI LOKAL
    # Subprogram ini akan melakukan penghilangan noise berdasarkan nilai-nilai singularnya.

    # KAMUS LOKAL
    # image_float , U , S , VT , S_k : matrix of float
    # denoised_image : img
    # k : integer

    # ALGORITMA LOKAL
    image_float = image.astype(float)
    U , S , VT = np.linalg.svd(image_float , full_matrices = False)
    k = 30
    S_k = np.zeros_like(S)
    S_k[:k] = S[:k]
    S_k_matrix = np.diag(S_k)
    denoised_image = U @ S_k_matrix @ VT
    denoised_image = np.clip(denoised_image , 0 , 255)
    denoised_image = denoised_image.astype(np.uint8)
    return denoised_image

def rekonstruksi_citra(path : str) :
    # DESKRIPSI LOKAL
    # Subprogram ini akan merekonstruksi citra berdasarkan hasil proses reduksi noise yang dilakukan.

    # KAMUS LOKAL
    # image , denoised_image : img

    # ALGORITMA LOKAL
    image = cv2.imread(path , cv2.IMREAD_GRAYSCALE)
    denoised_image = reduksi_noise(image)
    plt.figure(figsize = (10 , 5))
    plt.subplot(1 , 2 , 1)
    plt.imshow(denoised_image , cmap = 'gray')
    plt.title('Denoised Image')
    plt.axis('off')
    plt.show()