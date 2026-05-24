# 🩸 Blood Glucose Prediction System

## 📌 Project Overview
The Blood Glucose Prediction System is a machine learning-based healthcare application developed using Python, Streamlit, and MySQL.

The system predicts blood glucose levels and identifies diabetes risk based on patient health parameters.

The project provides:
- Patient glucose prediction
- Risk analysis
- Doctor dashboard
- Data visualization
- Record management using MySQL database

---

# 🚀 Features

## 👨‍⚕️ Doctor Module
- View patient records
- Delete patient records
- Visual analytics:
  - Age-wise distribution
  - Risk distribution pie chart
  - Correlation heatmap

## 🧑 Patient Module
- Enter health details
- Predict blood glucose level
- View diabetes risk
- Get health suggestions
- Visual charts for analysis

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Streamlit | Web application |
| MySQL | Database |
| Scikit-learn | Machine learning |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Heatmaps and charts |

---

# 📂 Project Structure

blood_glucose_advanced/
│
├── app.py
├── model.py
├── database.py
├── auth.py
├── utils.py
├── requirements.txt
├── diabetes.csv
├── model.pkl
└── README.md

---

# ⚙️ Installation Steps

## Step 1: Install Python

Download Python:
https://www.python.org/downloads/

---

## Step 2: Install XAMPP

Download and install XAMPP:
https://www.apachefriends.org/index.html

Start:
- Apache
- MySQL

---

# 🗄️ Database Setup

## Open phpMyAdmin

Open:
http://localhost/phpmyadmin

---

## Create Database

```sql
CREATE DATABASE bloodglucose_dp;