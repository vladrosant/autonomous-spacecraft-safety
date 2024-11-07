import cv2, time, os, json
import numpy as np

# carrega a imagem em tons de cinza
img = cv2.imread('src/imsample/debris_sample_2.jpg', cv2.IMREAD_GRAYSCALE)
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

# parametros de navegacao
h, w = img.shape
center_x, center_y = w // 2, h // 2
move_direction = {"x": 0, "y": 0}

# calcula centro do objeto detectado
def calculate_object_center(edges):
    # detecta contorno
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # maior contorno = provavelmente objeto principal
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            return cx, cy
    return None

# calcula centro do obj
object_center = calculate_object_center(sobel_edges)

if object_center:
    obj_x, obj_y = object_center

    # faz a maneuver baseado na posição relativa do centro do objeto e o centro da img
    if obj_x < center_x:
        move_direction["x"] = 1  # Move right
    elif obj_x > center_x:
        move_direction["x"] = -1  # Move left

    if obj_y < center_y:
        move_direction["y"] = 1  # Move down
    elif obj_y > center_y:
        move_direction["y"] = -1  # Move up

    print(f"Objeto detectado em: ({obj_x}, {obj_y})")
    print(f"Direcao surgerida: {move_direction}")
else:
    print("Nenhum objeto detectado. Sem manobras.")
