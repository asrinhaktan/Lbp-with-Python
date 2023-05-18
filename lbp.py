import numpy as np 
import matplotlib.pyplot as plt  
from tkinter import *  
from tkinter import filedialog  

# LBP için bir fonksiyon tanımladık
def lbp(image):
    rows, cols = image.shape  # Resim boyutlarını aldık
    lbp_image = np.zeros_like(image)  # LBP resmi için dizi oluşturduk

    # Her bir pikseli tarayarak LBP değerlerini hesapladık
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            center = image[i, j]  # Merkez pikselin değerini aldık
            code = 0  # LBP kodunu sıfırladık
            code |= (image[i-1, j-1] > center) << 7  # 7. bit
            code |= (image[i-1, j] > center) << 6  # 6. bit
            code |= (image[i-1, j+1] > center) << 5  # 5. bit
            code |= (image[i, j+1] > center) << 4  # 4. bit
            code |= (image[i+1, j+1] > center) << 3  # 3. bit
            code |= (image[i+1, j] > center) << 2  # 2. bit
            code |= (image[i+1, j-1] > center) << 1  # 1. bit
            code |= (image[i, j-1] > center) << 0  # 0. bit
            lbp_image[i, j] = code  # LBP değerini kaydettik

    return lbp_image  # LBP resmini döndürdük

# LBP öznitelik çıkarma fonksiyonunu tanımladık
def lbp_feature_extraction(image_path):
    img = plt.imread(image_path)  # Görüntüyü okuduk

    # Gri görüntü oluşturduk
    gray_img = np.dot(img[...,:3], [0.299, 0.587, 0.114])

    # LBP uyguladık
    lbp_img = lbp(gray_img)

    # Histogram hesapladık
    histogram = np.histogram(lbp_img.ravel(), 256, [0, 256])[0]

    # Sonuçları ekrana yazdırdık
    fig, ax = plt.subplots(1, 2, figsize=(10,5))
    ax[0].imshow(lbp_img, cmap='gray')
    ax[0].set_title('LBP Resmi')
    ax[1].plot(histogram)
    ax[1].set_title('LBP Histogramı')
    plt.show()

# GUI'yi oluşturduk
def browse_file():
    file_path = filedialog.askopenfilename()
    print(file_path)
    lbp_feature_extraction(file_path)

root = Tk()
root.title("LBP Öznitelik Çıkarma || Asrin Haktan Sahin")
root.geometry("500x400")

browse_button = Button(root, text="resim yukle", command=browse_file)
browse_button.pack()

root.mainloop()
