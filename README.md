# 🩺 Chest Cancer Classification using Deep Learning

## 📌 Project Overview

This project focuses on classifying chest cancer images into four categories using a deep learning model. It handles class imbalance and improves performance on difficult classes using techniques like class weighting and focal loss.

---

## 🚀 Features

* Transfer Learning using ResNet50
* Data Augmentation for better generalization
* Class Imbalance Handling using Class Weights
* Focal Loss for improved minority class prediction
* Early Stopping to prevent overfitting
* Streamlit Web App for real-time prediction
* Evaluation using Confusion Matrix, Precision, Recall, F1-score

---

## 🧠 Model Details

* **Base Model:** ResNet50 (pretrained on ImageNet)
* **Optimizer:** Adam
* **Loss Function:** Categorical Focal Loss
* **Regularization:** Dropout + EarlyStopping

### 📂 Classes

* Adenocarcinoma
* Large Cell Carcinoma
* Normal
* Squamous Cell Carcinoma

---

## 📊 Results

* **Accuracy:** ~70%
* Strong performance on majority classes
* Improved precision for minority class
* Balanced performance across classes

---

## ⚠️ Challenges

* Class imbalance in dataset
* Limited samples for certain classes
* Visual similarity between classes

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy
* Scikit-learn
* Streamlit

---

## 📁 Project Structure

```
src/
  chest_cancer/
    components/
    pipeline/
    config/
main.py
app.py
params.yaml
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/prachii-15/chest-cancer-classification-mlops.git
cd chest-cancer-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Training Pipeline

```bash
python main.py
```

### 4️⃣ Run Frontend App

```bash
streamlit run app.py
```

---

## 💡 Key Learnings

* Handling class imbalance using class weights
* Using focal loss for difficult classes
* Importance of evaluation metrics beyond accuracy
* Building end-to-end ML pipeline (MLOps structure)
* Creating ML web app using Streamlit

---

## 📌 Future Improvements

* Increase dataset size
* Improve minority class recall
* Deploy model on cloud
* Use advanced architectures (EfficientNet, Vision Transformers)

---

## 👩‍💻 Author

Prachi Mehta

---

⭐ If you like this project, consider giving it a star!
