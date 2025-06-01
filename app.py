import streamlit as st
import pandas as pd

# Titel und Einleitung
st.title("🏠 Prezzi Airbnb a Marsala – Dati, tendenze e osservazioni")

st.markdown("""
Benvenuti all’analisi dei dati degli alloggi Airbnb a Marsala 🇮🇹.  
Qui troverai una panoramica iniziale sul numero e le caratteristiche degli annunci su Airbnb a Marsala.
""")

# CSV einlesen und Vorschau anzeigen
df = pd.read_csv("listings.csv")
st.write("Numero di elementi:", len(df))
st.dataframe(df.head())

# Bild über GitHub-Link einbinden
st.subheader("📊 Sviluppo prezzi al mese")
st.markdown("""
I prezzi per un pernottamento a Marsala sono relativamente costanti. Non c'è una stagionalità forte.
l prezzo medio su Airbnb per notte a Marsala è di circa **88 Euro**.
""")

st.image(
    "https://raw.githubusercontent.com/maringio/airbnb-marsala-analyse/main/preise_pro_monat_bereinigt.png",
    caption="Durchschnittlicher Airbnb-Preis pro Monat in Marsala",
    use_container_width=True
)
