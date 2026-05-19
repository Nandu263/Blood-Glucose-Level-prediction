import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import mysql.connector

from model import predict
from database import save_data, delete_record
from auth import login
from utils import health_warning

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Blood Glucose System", layout="wide")

# ---------------- LOGIN ----------------
role = login()

if role is None:
    st.warning("Please login")
    st.stop()

st.title("🩸 Blood Glucose Prediction System")

# ---------------- DB CONNECTION ----------------
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bloodglucose_dp",
        port=3306   # change to 3307 if needed
    )

# ---------------- DOCTOR DASHBOARD ----------------
if role == "doctor":

    st.subheader("👨‍⚕️ Doctor Dashboard")

    try:
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM records", conn)
        conn.close()
    except Exception as e:
        st.error(f"Database error: {e}")
        st.stop()

    st.dataframe(df)

    # ---------------- DELETE ----------------
    st.subheader("🗑️ Delete Record")
    record_id = st.number_input("Enter Record ID to Delete", min_value=1)

    if st.button("Delete Record"):
        delete_record(record_id)
        st.success("✅ Record deleted successfully")

    # ---------------- BAR GRAPH ----------------
    st.subheader("📊 Age-wise Distribution")

    if not df.empty and "age" in df.columns:
        bins = [20, 30, 40, 50, 60, 70, 80]
        labels = ["21-30", "31-40", "41-50", "51-60", "61-70", "71-80"]

        df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
        grouped = df.groupby("age_group").size()

        plt.figure()
        grouped.plot(kind="bar")
        plt.xlabel("Age Group")
        plt.ylabel("Patients")
        plt.title("Patient Age Distribution")

        st.pyplot(plt)

    # ---------------- PIE CHART ----------------
    st.subheader("🥧 Risk Distribution")

    if not df.empty and "status" in df.columns:
        risk_counts = df["status"].value_counts()

        plt.figure()
        plt.pie(
            risk_counts,
            labels=risk_counts.index,
            autopct="%1.1f%%",
            startangle=140
        )
        plt.title("Health Risk Distribution")

        st.pyplot(plt)

    # ---------------- HEATMAP ----------------
    st.subheader("📊 Correlation Heatmap")

    if not df.empty:
        required_cols = ["age", "glucose", "bmi"]
        if all(col in df.columns for col in required_cols):
            data = df[required_cols]

            plt.figure()
            sns.heatmap(data.corr(), annot=True, cmap="coolwarm")

            st.pyplot(plt)

# ---------------- PATIENT DASHBOARD ----------------
elif role == "patient":

    st.subheader("🧑 Patient Dashboard")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 100, 25)
    glucose = st.number_input("Glucose", 50, 300, 110)
    bp = st.number_input("Blood Pressure", 50, 200, 80)
    skin = st.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.number_input("Insulin", 0, 300, 80)
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)

    if st.button("Predict"):

        if name.strip() == "":
            st.error("⚠️ Please enter patient name")
            st.stop()

        data = [1, glucose, bp, skin, insulin, bmi, dpf, age]

        try:
            glucose_val, status, risk, suggestion, confidence = predict(data)
        except Exception as e:
            st.error(f"Prediction error: {e}")
            st.stop()

        st.success(f"🩸 Predicted Glucose: {glucose_val} mg/dL")
        st.info(f"📊 Status: {status}")
        st.warning(f"⚠️ Risk Level: {risk}")
        st.write(f"💡 Suggestion: {suggestion}")
        st.write(f"📈 Confidence: {confidence}%")

        st.error(health_warning(status))

        # SAVE DATA
        save_data((name, age, glucose, bmi, status))

        # ---------------- SCATTER ----------------
        st.subheader("📈 HbA1c vs Glucose")

        hba1c = np.random.uniform(4, 15, 100)
        g = hba1c * 30 + np.random.randn(100) * 50

        plt.figure()
        plt.scatter(hba1c, g)
        plt.xlabel("HbA1c")
        plt.ylabel("Glucose")
        plt.title("HbA1c vs Glucose Relationship")

        st.pyplot(plt)

        # ---------------- PIE ----------------
        st.subheader("🥧 Your Risk Level")

        labels = ["Low", "Medium", "High"]
        sizes = [0, 0, 0]

        if risk == "Low":
            sizes = [1, 0, 0]
        elif risk == "Medium":
            sizes = [0, 1, 0]
        else:
            sizes = [0, 0, 1]

        plt.figure()
        plt.pie(sizes, labels=labels, autopct="%1.0f%%")
        plt.title("Your Risk Category")

        st.pyplot(plt)