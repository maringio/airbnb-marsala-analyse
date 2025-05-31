import streamlit as st
import pandas as pd

st.title("🏠 Prezzi Airbnb a Marsala – Dati, tendenze e osservazioni")

st.markdown("""
WBenvenuti all’analisi dei dati degli alloggi Airbnb a Marsala 🇮🇹.
Qui troverai una panoramica iniziale sul numero e le caratteristiche degli annunci su Airbnb.
""")

df = pd.read_csv("listings.csv")
st.write("Anzahl Einträge:", len(df))
st.dataframe(df.head())
