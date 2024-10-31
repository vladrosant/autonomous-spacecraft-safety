import cv2
import numpy as np
import time, os, json

# carrega a imagem em tons de cinza
img = cv2.imread('src/imsample/ebris_sample_1.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("erro no arquivo de imagem sample")

# comeca o timer para analise de performance
start_time = time.time()

# aplicacao de blur Gaussiano para diminuir o ruido
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

canny_edges = cv2.Canny(blurred_img, 100, 200)

processing_time = time.time() - start_time
print(f"Tempo de processamento para Canny: {processing_time:.4f} segundos")

# \/\/\/\/ processo de gravar o tempo de performance num json \/\/\/\/
log_file = 'src/performance_log.json'
method_name = "Metodo Canny"

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

# tentativa de automatizar a nomenclatura das imagens
base_path = 'src/imoutput/canny/canny_edges_output'
file_extension = '.jpg'
file_path = base_path + file_extension
counter = 1
while os.path.exists(file_path):
    file_path = f"{base_path}-{counter}{file_extension}"
    counter += 1

cv2.imwrite(file_path, canny_edges)
print(f"Arquivo salvo como: {file_path}")
cv2.imshow('Canny Edges', canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
