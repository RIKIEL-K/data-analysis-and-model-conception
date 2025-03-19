import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns



df = pd.read_csv("BeansDataSet.csv")

# Encoder les catégories "Channel" et "Region" en valeurs numériques pour les corrélations
df['Channel_Encoded'] = df['Channel'].map({'Online': 1, 'Store': 0})
df['Region_Encoded'] = df['Region'].map({'North': 0, 'Center': 1, 'South': 2})

# Sélectionner uniquement les colonnes numériques
df_corr = df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino', 'Channel_Encoded', 'Region_Encoded']]

# Calculer la matrice de corrélation
corr = df_corr.corr()

# Affichage de la heatmap
st.subheader("Heatmap des Corrélations")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
plt.title("Heatmap des Corrélations entre les Ventes et les Variables")
st.pyplot(fig)

# Afficher les résultats sous forme de graphique de corrélation entre produits et zones
st.subheader("Corrélations entre les Ventes de Produits et les Variables")
fig, ax = plt.subplots(figsize=(10, 6))

# Visualiser les relations entre les zones, canaux et ventes
sns.scatterplot(x='Region_Encoded', y='Robusta', hue='Channel', data=df, ax=ax, palette='Set1', s=100)
plt.title('Corrélation entre la Région et les Ventes de Robusta')
plt.xlabel('Région')
plt.ylabel('Ventes de Robusta')
st.pyplot(fig)



# Encoder les catégories "Channel" et "Region" en valeurs numériques pour une meilleure visualisation
df['Channel_Encoded'] = df['Channel'].map({'Online': 1, 'Store': 0})
df['Region_Encoded'] = df['Region'].map({'South': 0, 'Center': 1, 'North': 2})

# Sélectionner le produit pour afficher l'histogramme
st.subheader("Visualisation des Ventes par Produit avec un Diagramme en Points")
product = st.selectbox("Choisissez le produit :", ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino'])

# Création du diagramme en points
fig = px.scatter(
    df,
    x="Region_Encoded",
    y=product,
    color="Channel",  # Utiliser la variable 'Channel' pour colorier les points
    hover_data=["Region", "Channel"],  # Afficher les détails au survol
    labels={"Region_Encoded": "Région", product: f"Ventes de {product}", "Channel": "Canal"},  # Labels personnalisés
    title=f"Diagramme en Points : Ventes de {product} selon la Région et le Canal"
)

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)