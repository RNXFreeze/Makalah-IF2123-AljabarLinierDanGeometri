import numpy as np
import cv2
import matplotlib.pyplot as plt

def apply_svd_denoising(image, k):
    """
    Apply SVD denoising to an image.

    Args:
    image (numpy.ndarray): The input image (2D grayscale).
    k (int): Number of singular values to retain.

    Returns:
    numpy.ndarray: The denoised image.
    """
    # Convert image to float type for SVD
    image_float = image.astype(float)

    # Compute the SVD
    U, S, VT = np.linalg.svd(image_float, full_matrices=False)

    # Reconstruct the image with only the top k singular values
    S_k = np.zeros_like(S)
    S_k[:k] = S[:k]
    S_k_matrix = np.diag(S_k)

    # Reconstruct the image
    denoised_image = U @ S_k_matrix @ VT
    denoised_image = np.clip(denoised_image, 0, 255)  # Clip to valid range
    denoised_image = denoised_image.astype(np.uint8)

    return denoised_image

def main():
    # Load the image
    image_path = 'path_to_your_image.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Image not found.")
        return

    # Apply SVD denoising
    k = 50  # Number of singular values to retain
    denoised_image = apply_svd_denoising(image, k)

    # Display the original and denoised images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(denoised_image, cmap='gray')
    plt.title('Denoised Image')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
