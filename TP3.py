import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Charger les données (remplacez 'votre_dataset.csv' par le nom de votre fichier CSV)
data = pd.read_csv("data_diass_janvier.csv", encoding="ISO-8859-1")
st.header("TABLEAU DE BORD")
st.subheader("Affichage du Dataset")
st.write(data)

st.set_option('deprecation.showPyplotGlobalUse', False)
#---------------------------------------ANALYSE DES GRAPHES-------------------------------------------
#Variation Plant Energy

st.subheader('Graphique Variation Plant Energy kWh')
plt.plot(data['Date'],data ["Plant Energy (kWh)"])
plt.title('Variation Plant Energy kWh')
plt.xlabel('Date')
plt.ylabel('Plant Energy(kWh)')
st.pyplot()

#Variation Plant Insolation
st.subheader('Graphique Variation Plant Power (kW)')
plt.plot(data['Date'],data ["Plant Power (kW)"])
plt.title('Variation Plant Power (kW)')
plt.xlabel('Date')
plt.ylabel('Plant Power (kW)')
st.pyplot()

#Variation Plant Power
st.subheader('Graphique Variation Plant Insolation  (kWh/m2)')
plt.plot(data['Date'],data ["Plant Insolation  (kWh/m2)"])
plt.title('Variation Plant Insolation  (kWh/m2)')
plt.xlabel('Date')
plt.ylabel('Plant Insolation  (kWh/m2)')
st.pyplot()

#Variation Plant Irradiance  (W/m2)
st.subheader('Graphique Variation Plant Irradiance  (W/m2)')
plt.plot(data['Date'],data ["Plant Irradiance  (W/m2)"])
plt.title('Variation Plant Irradiance  (W/m2)')
plt.xlabel('Date')
plt.ylabel('Plant Irradiance  (W/m2)')
st.pyplot()

#Variation Plant Irradiance (Horizontal)
st.subheader('Graphique Variation Plant Irradiance (Horizontal) (W/m2)')
plt.plot(data['Date'],data ["Plant Irradiance (Horizontal) (W/m2)"])
plt.title('Variation Plant Irradiance (Horizontal)')
plt.xlabel('Date')
plt.ylabel('Plant Irradiance (Horizontal) (w/m2')
st.pyplot()

#Variation Plant Temperature (Ambient) (ÂºC)
st.subheader('Graphique Variation Plant Temperature (Ambient) (°C)')
plt.plot(data['Date'],data ["Plant Temperature (Ambient) (°C)"])
plt.title('Variation Plant Temperature (Ambient) (°C)')
plt.xlabel('Date')
plt.ylabel('Plant Temperature (Ambient) (°C)')
st.pyplot()

#Variation Plant Temperature (Panel) (°C)
st.subheader('Graphique Variation Plant Temperature (Panel) (°C)')
sns.lineplot(x=data['Date'],y=data ["Plant Temperature (Panel) (°C)"])
st.pyplot()

st.subheader('Synthèse graphique')
# Graphique interactif avec plotly
fig = px.scatter_matrix(data, dimensions=data.columns, title='Matrice de dispersion interactive')
st.plotly_chart(fig)
sns.pairplot(data)
st.pyplot()

