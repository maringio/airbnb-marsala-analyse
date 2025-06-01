import streamlit as st
import pandas as pd

# Titel und Einleitung
st.title("🏠 Prezzi Airbnb a Marsala – Dati, tendenze e osservazioni")

st.markdown("""
WBenvenuti all’analisi dei dati degli alloggi Airbnb a Marsala 🇮🇹.  
Qui troverai una panoramica iniziale sul numero e le caratteristiche degli annunci su Airbnb a Marsala.
""")

# CSV einlesen und Vorschau anzeigen
df = pd.read_csv("listings.csv")
st.write("Anzahl Einträge:", len(df))
st.dataframe(df.head())

# Bild über GitHub-Link einbinden
st.subheader("📊 Preisentwicklung pro Monat")
st.markdown("Die Preise für eine Übernachtung in Marsala sind erstaunlich konstant – es zeigt sich keine starke Saisonalität.")

st.image(
    "https://raw.githubusercontent.com/maringio/airbnb-marsala-analyse/main/preise_pro_monat_bereinigt.png",
    caption="Durchschnittlicher Airbnb-Preis pro Monat in Marsala",
    use_container_width=True
)
