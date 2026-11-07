
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Membaca gambar asli
gambar = cv2.imread("kunci.jpeg")

if gambar is None:
    print("Gambar kunci.jpeg tidak ditemukan!")
    exit()

# Mengubah gambar ke RGB
gambar = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

# Mean Filter
mean3 = cv2.blur(gambar, (3, 3))
mean5 = cv2.blur(gambar, (5, 5))

# Gaussian Filter
gaussian3 = cv2.GaussianBlur(gambar, (3, 3), 0)
gaussian5 = cv2.GaussianBlur(gambar, (5, 5), 0)

# Median Filter
median3 = cv2.medianBlur(gambar, 3)
median5 = cv2.medianBlur(gambar, 5)

# Sharpening
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpening = cv2.filter2D(gambar, -1, kernel)

# Menyimpan hasil gambar
hasil = {
    "Citra Asli": gambar,
    "Mean 3x3": mean3,
    "Mean 5x5": mean5,
    "Gaussian 3x3": gaussian3,
    "Gaussian 5x5": gaussian5,
    "Median 3x3": median3,
    "Median 5x5": median5,
    "Sharpening": sharpening
}

os.makedirs("hasil_filter", exist_ok=True)

for nama, citra in hasil.items():
    nama_file = nama.lower().replace(" ", "_") + ".png"
    plt.imsave("hasil_filter/" + nama_file, citra)

# Menampilkan semua hasil
plt.figure(figsize=(12, 10))

for i, (nama, citra) in enumerate(hasil.items()):
    plt.subplot(3, 3, i + 1)
    plt.imshow(citra)
    plt.title(nama)
    plt.axis("off")

plt.tight_layout()
plt.show()

# Menampilkan nilai intensitas
print("Nilai intensitas piksel:")
for nama, citra in hasil.items():
    print(nama, ":", citra[100, 100])

print("Semua hasil filter berhasil disimpan!")
