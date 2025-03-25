import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import statsmodels.api as sm


df = pd.read_csv("BeansDataSet.csv")

def scatter_plot(x, y, x_label, y_label, title):
    fig = px.scatter(df, x=x, y=y, labels={x: x_label, y: y_label}, title=title, trendline='ols')
    st.plotly_chart(fig)

st.title("Correlations")

# Encoder les catégories "Channel" et "Region" en valeurs numériques pour les corrélations
df['Channel_Encoded'] = df['Channel'].map({'Online': 1, 'Store': 0})
df['Region_Encoded'] = df['Region'].map({'North': 0, 'Center': 1, 'South': 2})

# Sélectionner uniquement les colonnes numériques
df_corr = df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino', 'Channel_Encoded', 'Region_Encoded']]

options = st.selectbox("Par",["Regions et Canaux","Les Cafés","Les canaux et les cafés"])


if options == "Les Cafés":
    # Corrélations entre les cafés
    corr_coffee = df_corr[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].corr()
    st.subheader("Corrélation entre les cafés")
    st.write(corr_coffee)

    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_coffee, annot=True, cmap="coolwarm", fmt='.2f')
    st.pyplot(plt)

elif options == "Les canaux et les cafés":
    # Corrélations entre les canaux et les cafés
    corr_channel_coffee = df_corr[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino', 'Channel_Encoded']].corr()[['Channel_Encoded']]
    st.write("Corrélation entre les Canaux et les Cafés")
    st.write(corr_channel_coffee)

    # Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_channel_coffee, annot=True, cmap="coolwarm", fmt='.2f')
    st.pyplot(plt)
elif options == "Regions et Canaux":
    # Corrélations avec les régions et les canaux
    corr_region_channel = df_corr.corr()[['Channel_Encoded', 'Region_Encoded']]
    st.write("Corrélation avec les Régions et les Canaux")
    st.write(corr_region_channel)

    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_region_channel, annot=True, cmap="coolwarm", fmt='.2f')
    st.pyplot(plt)
view = st.toggle("Voir les resultats")

if view :
    st.markdown("""
    <div>
    <p>Il existe une corrélation entre les ventes d' Espresso et de Latte</p>
    <p>De plus, On a egalement une corrélation entre les ventes d'Espresso et d'Arabica</p>
</div>

""", unsafe_allow_html=True)



