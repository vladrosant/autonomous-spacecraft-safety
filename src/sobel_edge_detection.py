import cv2
import numpy as np
import time, os

# carrega a imagem em tons de cinza
img = cv2.imread('src/imsample/space_debris_sample.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("erro no arquivo de imagem sample")

# comeca o timer para analise de performance
start_time = time.time()

# aplica o operador sobel nas direcoes x e y
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# combina os dois gradientes
sobel_edges = cv2.magnitude(sobel_x, sobel_y)
sobel_edges = np.uint8(np.absolute(sobel_edges))

processing_time = time.time() - start_time
print(f"Tempo de processamento Sobel: {processing_time:.4f} segundos")

# tentativa de automatizar a nomenclatura das imagens
base_path = 'src/imoutput/sobel/sobel_edges_output'
file_extension = '.jpg'
file_path = base_path + file_extension
counter = 1
while os.path.exists(file_path):
    file_path = f"{base_path}-{counter}{file_extension}"
    counter += 1

cv2.imwrite(file_path, sobel_edges)
print(f"Arquivo salvo como: {file_path}")
cv2.imshow('Sobel Edges', sobel_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
