# 🩺 Diabetes Risk Predictor App

A simple machine learning-powered web app built with **Streamlit** that predicts the risk level of diabetes based on user-input health metrics.

---

## 📌 Project Overview

This application predicts whether a person is at risk of developing diabetes using a **Random Forest Classifier** trained on selected features from the **Pima Indians Diabetes Dataset**.

The app takes user health metrics and classifies the diabetes risk into four levels:
- **Normal**
- **Low**
- **Medium**
- **High**

---

## ⚙️ Features Used in the Model

The machine learning model was trained using the following 5 features:

- **Glucose**
- **Age**
- **BMI** (Body Mass Index)
- **Diabetes Pedigree Function**
- **Insulin**

---

## 🧠 Model Info

- **Algorithm:** RandomForestClassifier
- **Library:** scikit-learn
- **Training Data:** Pima Indians Diabetes Dataset (8 features originally)
- **Selected Features:** 5 (see above)
- **Model Accuracy:** ~78% (approx.)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Licht005/diabetes-predictor-app.git
cd diabetes-predictor-app
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv diabetes_env
# Windows
diabetes_env\Scripts\activate
# macOS/Linux
source diabetes_env/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🚀 App Interface

The user interface is built using **Streamlit** and features:
- A clean input form for health metrics
- Risk prediction result with visual emphasis
- Expandable section explaining model accuracy
- Responsive design, works in web browsers

---

## 📁 Project Structure

```plaintext
diabetes-predictor-app/
│
├── model/
│   └── diabetes_model.pkl           # Trained ML model
├── app.py                           # Main Streamlit app
├── requirements.txt                 # Python dependencies
└── README.md                        # This documentation file
```

---

## 📊 Dataset Reference

The model was trained using the **Pima Indians Diabetes Dataset**, which includes diagnostic measurements for females of at least 21 years old of Pima Indian heritage. [Available on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## ⚠️ Disclaimer

> This application is for **educational purposes only** and should not be used for real medical diagnosis or treatment. Please consult a healthcare professional for clinical advice.

---

## 👨‍💻 Author

**Lucas**  
B.Tech Student - Robotics and AI  
Learning Data Science & Machine Learning  

---

## ⭐️ Give it a Star!

If you found this project helpful or interesting, consider starring the repo. It helps others discover and encourages continued development!
