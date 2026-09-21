import pandas as pd
from pymongo import MongoClient
import streamlit as st
import plotly.express as px
import os
from dotenv import load_dotenv
import pymongo
load_dotenv()
#On se connecte à la base de données MongoDB
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db= client["jobscrapper"]
collection = db["offres"]

st.set_page_config(page_title = "ScrapJob your job searcher", page_icon="sj.png", layout= "wide")
st.sidebar.image("scrapjobimg.png", width=900)
st.markdown("<h1 style='color: #1800AD;'>Dashboard - Offres d'emploi Data</h1>", unsafe_allow_html=True)
data = list(collection.find())
df = pd.DataFrame(data) 
villes = df['ville'].unique()
ville_choisie  = st.sidebar.selectbox('Sélectionnez une ville', villes)
df_filtered = df[df['ville']== ville_choisie] 
nbr_offres = len(df_filtered)
col1, col2 = st.columns(2)
with col1:
    st.metric("nombre d'offres d'emploi", nbr_offres)
with col2:
    st.metric("nombre de villes", len(villes))
st.dataframe(df_filtered, column_config={"lien": st.column_config.LinkColumn("Lien")})
top_postes= df_filtered["poste"].value_counts().head(10)
fig1= px.bar(x= top_postes.index, y= top_postes.values, title= f"Top 10 des postes les plus recherchés à {ville_choisie}", labels={"x":"Postes", "y":"Nombre d'offres"})
st.plotly_chart(fig1)