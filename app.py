import streamlit as st
import pandas as pd

st.title("Airbnb Preisanalyse – Marsala 🇮🇹")

df = pd.read_csv("listings.csv")
st.write("Anzahl Einträge:", len(df))

st.dataframe(df.head())
