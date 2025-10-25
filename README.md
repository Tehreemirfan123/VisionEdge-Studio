# VisionEdge Studio

**VisionEdge Studio** is an interactive image processing web app built with **Streamlit** that allows users to visualize and experiment with different **edge detection algorithms** such as **Sobel**, **Laplacian**, and **Canny**.  

The app provides an intuitive interface for uploading images, adjusting algorithm parameters in real-time, and comparing original and processed images side-by-side — perfect for learning, research, and computer vision demonstrations.

---

## Features

- Upload any image (JPG, JPEG, PNG, BMP)
- Apply different edge detection algorithms:
  - **Sobel Operator**
  - **Laplacian Operator**
  - **Canny Edge Detector**
- Interactive parameter tuning:
  - Kernel size selection
  - Direction control (for Sobel)
  - Canny thresholds and Gaussian blur settings
- Automatic preprocessing (Gaussian smoothing)
- Side-by-side comparison of input and output images
- Clean, centered UI with a built-in footer and theme customization

---

## Tech Stack

- **Python 3.13.7**
- **Streamlit** (for UI and deployment)
- **OpenCV (cv2)** (for image processing)
- **NumPy**
- **Pillow (PIL)**

---

## Setup and Installation

Follow these steps to set up **VisionEdge Studio** locally on your system.

### 1️⃣ Clone the repository

- git clone https://github.com/Tehreemirfan123/VisionEdge-Studio
- cd VisionEdge-Studio

### 2️⃣ Create a Virtual Environment

- On windows, run:
    - python -m venv venv
    - venv\Scripts\activate


### 3️⃣ Install Dependencies

With the virtual environment active, install all required libraries, run:

- pip install streamlit opencv-python pillow numpy

### 4️⃣ Run the Application

Start the Streamlit app by running:

- streamlit run app.py

Once it starts, your browser will automatically open the app at:

- http://localhost:8501

---

### Additional Features Implemented

- Auto-expanding sidebar controls upon image upload for user convenience
- Kernel size dropdown (odd values only) for accurate Gaussian blurring
- Custom pointer cursor for all dropdowns
- Dynamic footer with developer credit
- Fully centered, minimal UI theme for a clean and modern look

---

### 💻 Developer

Developed with ❤️ by Tehreem Irfan
© 2025 VisionEdge Studio

--- 

## Screenshots and Images

### App UI
<img src="Screenshots/AppUI.jpg" width="600"/>

- Figure 1 – Shows the actual default UI of the app (VisionEdge Studio).

### Image Uploading 
<img src="Screenshots/ImageUpload.jpg" width="600"/>

- Figure 2 – Shows an image being uploaded from user's computer.

### Algorithm Controls
<img src="Screenshots/AlgorithmsControl.jpg" height="500"/>

- Figure 3 – Shows the algorithms and parameters controlling tab.

### Sobel Edge Detection Example
<img src="Screenshots/SobelOperator.jpg" width="600"/>

- Figure 4 – Sobel Edge Detection changing parameters (Direction and Kernel size).

### Laplacian Edge Detection Example
<img src="Screenshots/LaplacianOperator.jpg" width="600"/>

- Figure 5 – Laplacian Edge Detection changing parameter (Kernel size).

### Canny Edge Detection Example
<img src="Screenshots/CannyOperator.jpg" width="600"/>

- Figure 6 – Canny Edge Detection changing parameters (Lower/upper thresholds, sigma and kernel size).
