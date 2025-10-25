# app.py
import streamlit as st
from PIL import Image
import numpy as np
from utils.algorithms import apply_sobel, apply_laplacian, apply_canny

# --- HTML Styling for the pointer cusor usage ---
st.markdown("""
    <style>
    div[data-baseweb="select"] * {
        cursor: pointer !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Streamlit App Titles with HTML Styling ---
st.markdown("""
    <h1 style='text-align: center; font-style: italic; color: white;'>VisionEdge Studio</h1>
    <h3 style='text-align: center; color:#cc4444;'>Welcome to VisionEdge Studio!</h3>
    <p style='text-align: center; color: #EDF0DA; font-size:17px;'>
        Play with your image edges and visualize different edge detection algorithms.
    </p>
""", unsafe_allow_html=True)

# --- Using streamlit Documentation ---
# --- File Uploader ---
user_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png", "bmp"])

# --- Chatgpt Code for Algorithms --- 
if user_file:
    input_img = Image.open(user_file)
    st.success("Image uploaded successfully!")

    # --- Algorithm Selection by user ---
    with st.sidebar.expander("Algorithm Controls", expanded=True):
        option = st.selectbox("Select Algorithm", ("Sobel", "Laplacian", "Canny"))

        # --- Parameter Controls for user ---

        # --- Sobel Algorithm ---
        if option == "Sobel":
            ksize = st.sidebar.selectbox("Kernel size", [1, 3, 5, 7], index=1)
            direction = st.sidebar.selectbox("Direction", ["Both", "X", "Y"], index=0)
            output = apply_sobel(input_img, ksize, direction)

        # --- Laplacian Algorithm ---
        elif option == "Laplacian":
            ksize = st.sidebar.selectbox("Kernel size", [1, 3, 5, 7], index=1)
            output = apply_laplacian(input_img, ksize)

        # --- Canny Algorithm ---
        elif option == "Canny":
            lower = st.sidebar.slider("Lower Threshold", 0, 255, 50)
            upper = st.sidebar.slider("Upper Threshold", 0, 255, 150)
            sigma = st.sidebar.slider("Sigma (blur strength)", 0, 10, 1)
            blur_k = st.sidebar.selectbox("Kernel size", [1, 3, 5, 7], index=1)
            output = apply_canny(input_img, lower, upper, sigma, blur_k)

# --- Using streamlit Documentation ---
    # --- Display Input & Output Side by Side ---
    col1, col2 = st.columns(2)                       
    with col1:
        st.subheader("Input Image")
        st.image(input_img, caption="Uploaded Image", use_container_width=True)

    with col2:
        st.subheader("Output Image")
        st.image(output, caption=f"Result of {option} Edge Detection", use_container_width=True)

else:
    st.info("Please upload an image file to begin.")

# --- Footer for Copyright with HTML Styling ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'> Developed by Tehreem Irfan | VisionEdge Studio © 2025</p>",
    unsafe_allow_html=True
)
