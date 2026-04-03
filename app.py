import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("artifacts/model_trainer/model.keras")

class_names = [
    "adenocarcinoma",
    "large.cell.carcinoma",
    "normal",
    "squamous.cell.carcinoma"
]

st.title("🩺 Chest Cancer Classification")

uploaded_file = st.file_uploader("Upload Chest Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = img.resize((224, 224))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.resnet50.preprocess_input(img)

    # Prediction
    prediction = model.predict(img)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Prediction: {predicted_class}")
    st.write("Confidence:", np.max(prediction))
    st.subheader("Prediction Result")

    if predicted_class == "normal":
        st.success("🟢 Normal (No Cancer Detected)")
    else:
        st.error(f"🔴 Detected: {predicted_class}")
