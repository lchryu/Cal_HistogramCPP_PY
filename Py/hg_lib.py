import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Thực hiện cân bằng histogram
    equ = cv2.equalizeHist(img)

    # Vẽ histogram của ảnh gốc
    plt.figure(figsize=(10, 5))
    plt.subplot(231), plt.imshow(img, cmap="gray"), plt.title("Ảnh gốc")
    plt.subplot(234), plt.hist(img.flatten(), 256, [0, 256], color="r"), plt.title("Histogram ảnh gốc")

    # Hiển thị ảnh đã cân bằng histogram
    plt.subplot(232), plt.imshow(equ, cmap="gray"), plt.title("Ảnh đã cân bằng histogram")
    plt.subplot(235), plt.hist(equ.flatten(), 256, [0, 256], color="r"), plt.title("Histogram ảnh đã cân bằng")

    plt.show()

    # Lưu ảnh đã cân bằng histogram
    cv2.imwrite("equ_histogram.jpg", equ)

# Thay đổi đường dẫn tới ảnh của bạn
image_path = "1_car.jpg"

# Gọi hàm cân bằng histogram
histogram_equalization(image_path)