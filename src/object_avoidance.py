import cv2, time
import numpy as np

# comeca o timer para analise de performance
start_time = time.time()

# Load edge-detected image (from chosen method)
img = cv2.imread('src/imoutput/canny/canny_edges_output-27.jpg', 0)
if img is None:
    raise ValueError("Edge-detected image not found. Please make sure 'edge_output.jpg' is available.")

# Define parameters for navigation
h, w = img.shape
center_x, center_y = w // 2, h // 2
move_direction = {"x": 0, "y": 0}

# Function to calculate center of the detected object
def calculate_object_center(edges):
    # Detect contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Get the largest contour (assuming it's the main object)
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            return cx, cy
    return None

# Calculate object center
object_center = calculate_object_center(img)

if object_center:
    obj_x, obj_y = object_center

    # Determine movement based on object's position relative to center
    if obj_x < center_x:
        move_direction["x"] = 1  # Move right
    elif obj_x > center_x:
        move_direction["x"] = -1  # Move left

    if obj_y < center_y:
        move_direction["y"] = 1  # Move down
    elif obj_y > center_y:
        move_direction["y"] = -1  # Move up

    print(f"Object detected at: ({obj_x}, {obj_y})")
    print(f"Suggested move direction: {move_direction}")
    processing_time = time.time() - start_time
    print(f"Tempo de processamento Sobel: {processing_time:.4f} segundos")
else:
    print("No significant object detected. No maneuver required.")
