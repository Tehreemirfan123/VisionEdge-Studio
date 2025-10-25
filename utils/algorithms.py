# utils/algorithms.py
from PIL import Image
import numpy as np
import cv2

# --- Helper Function for image conversion (from Chatgpt) ---
def prepare_image(image):
    """Converts a PIL Image to grayscale numpy array for OpenCV processing."""
    if image.mode != "L":
        image = image.convert("L")  # convert to grayscale
    return np.array(image)

# --- Chatgpt functions for algorithms --- 
# --- Sobel Operator ---
def apply_sobel(image, ksize=1, direction='Both'):
    gray = prepare_image(image)
    ddepth = cv2.CV_64F

    if direction == 'X':
        sobel = cv2.Sobel(gray, ddepth, 1, 0, ksize=ksize)
    elif direction == 'Y':
        sobel = cv2.Sobel(gray, ddepth, 0, 1, ksize=ksize)
    else:
        sx = cv2.Sobel(gray, ddepth, 1, 0, ksize=ksize)
        sy = cv2.Sobel(gray, ddepth, 0, 1, ksize=ksize)
        sobel = np.sqrt(sx ** 2 + sy ** 2)

    sobel = np.uint8(255 * (sobel / (sobel.max() + 1e-8)))
    return sobel

# --- Laplacian Operator ---
def apply_laplacian(image, ksize=1):
    gray = prepare_image(image)
    ddepth = cv2.CV_64F
    lap = cv2.Laplacian(gray, ddepth, ksize=ksize)
    lap = np.uint8(255 * (np.absolute(lap) / (lap.max() + 1e-8)))
    return lap

# --- Canny Operator ---
def apply_canny(image, lower_thresh, upper_thresh, sigma=1.0, ksize=1):

    # Accept PIL Image or numpy array
    if isinstance(image, Image.Image):
        arr = np.array(image.convert("L"))
    else:
        arr = image.copy()
        # If color image, convert to grayscale
        if arr.ndim == 3:
            arr = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur if kernel size > 1
    if ksize > 1:
        arr = cv2.GaussianBlur(arr, (ksize, ksize), sigmaX=float(sigma))

    # Ensure thresholds are between 0 and 255
    lower = int(max(0, min(255, lower_thresh)))
    upper = int(max(0, min(255, upper_thresh)))

    edges = cv2.Canny(arr, lower, upper)
    return edges
