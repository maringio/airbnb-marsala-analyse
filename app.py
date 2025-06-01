import streamlit as st
import pandas as pd

st.title("🏠 Prezzi Airbnb a Marsala – Dati, tendenze e osservazioni")

st.markdown("""
WBenvenuti all’analisi dei dati degli alloggi Airbnb a Marsala 🇮🇹.
Qui troverai una panoramica iniziale sul numero e le caratteristiche degli annunci su Airbnb a Marsala.
""")

df = pd.read_csv("listings.csv")
st.write("Anzahl Einträge:", len(df))
st.dataframe(df.head())

image = Image.open("preise_pro_monat_bereinigt.png")
st.image(image, caption="Durchschnittlicher Airbnb-Preis pro Monat in Marsala", use_column_width=True)

from PIL import Image

st.subheader("📊 Preisentwicklung pro Monat")
st.markdown("Die Preise für eine Übernachtung in Marsala sind erstaunlich konstant – es zeigt sich keine starke Saisonalität.")
image = Image.open("preise_pro_monat_bereinigt.png")
st.image(image, caption="Durchschnittlicher Airbnb-Preis pro Monat in Marsala", use_column_width=True)
