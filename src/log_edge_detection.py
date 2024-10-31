import cv2
import numpy as np
import time, os

# carrega a imagem em tons de cinza
img = cv2.imread('src/imsample/space_debris_sample.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("erro no arquivo de imagem sample")

# comeca o timer para analise de performance
start_time = time.time()

# aplicacao de blur Gaussiano para diminuir o ruido
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# aplica o operador laplaciano
log_edges = cv2.Laplacian(blurred_img, cv2.CV_64F)
log_edges = np.uint8(np.absolute(log_edges))

processing_time = time.time() - start_time
print(f"Tempo de processamento LoG: {processing_time:.4f} segundos")

base_path = 'src/imoutput/log/log_edges_output'
file_extension = '.jpg'
file_path = base_path + file_extension
counter = 1
while os.path.exists(file_path):
    file_path = f"{base_path}-{counter}{file_extension}"
    counter += 1

cv2.imwrite(file_path, log_edges)
cv2.imshow('LoG Edges', log_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
