from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

img = Image.open("lena.jpg")
img2 = img.filter(ImageFilter.MaxFilter(size=3))
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img2), plt.title('max filtered')
plt.xticks([]), plt.yticks([])
plt.show()