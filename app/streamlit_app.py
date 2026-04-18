import streamlit as st
import csv
import os

st.title("Smart Traffic Dashboard")

file_path = "output/logs.csv"

if not os.path.exists(file_path):
    st.error("Run main.py first")
    st.stop()

data = []

with open(file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

st.dataframe(data)