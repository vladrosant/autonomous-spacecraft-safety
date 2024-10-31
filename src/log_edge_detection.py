import cv2
import numpy as np
import time, os, json

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

# \/\/\/\/ processo de gravar o tempo de performance num json \/\/\/\/
log_file = 'src/performance_log.json'
method_name = "LoG Edge Detection"

if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        log_data = json.load(f)
else:
    log_data = {}
# adiciona o tempo de performance na lista correspondente
if method_name not in log_data:
    log_data[method_name] = []

log_data[method_name].append(processing_time)
# grava o log atualizado no arquivo
with open(log_file, 'w') as f:
    json.dump(log_data, f, indent=4)
# \/\/\/\/ fim processo de gravar o tempo... \/\/\/\/

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
