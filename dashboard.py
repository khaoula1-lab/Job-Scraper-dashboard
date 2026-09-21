import pandas as pd
from pymongo import MongoClient
import streamlit as st
import plotly.express as px
#On se connecte à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db= client["jobscrapper"]
collection = db["offres"]

st.title("Dashboard - Offres d'emploi Data")
data = list(collection.find())
df = pd.DataFrame(data) 
st.dataframe(df)