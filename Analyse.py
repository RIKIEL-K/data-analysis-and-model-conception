import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BeansDataSet.csv")

st.title("Analyse: Beans & Pods Inc")


st.subheader("Echantillons de données")
with st.form("Voir les données du formulaire"):
    lines_to_show = st.slider('Sélectionner le nombre de lignes à afficher', min_value=1, max_value=5, value=2)
    # Affichage des lignes sélectionnées
    st.write(df.head(lines_to_show))

    submitted = st.form_submit_button("voir")

st.header(f"Moyennes")
option = st.selectbox("Calculer la moyenne par",("Région","Canal"))
st.subheader(f"Moyenne des ventes par {option}")

# Sélectionne uniquement les colonnes numériques
df_numeric = df[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']]

# Calculer la moyenne des ventes par canal
df_avg_channel = df.groupby('Channel')[df_numeric.columns].mean()

if option=="Région":
    # Calcule la moyenne des ventes par région
    df_avg_region = df.groupby('Region')[df_numeric.columns].mean()
    st.write(df_avg_region)

    on = st.toggle("Voir l'analyse")

    if on:
        st.markdown("""
            <div>
          <h3>Régions avec les ventes les plus élevées et les plus basses</h3>
          <ul>
            <li><strong>Robusta :</strong> Ventes les plus élevées dans le Sud et les plus basses dans le Centre.</li>
            <li><strong>Arabica :</strong> Ventes les plus élevées dans le Sud et les plus basses dans le Centre.</li>
            <li><strong>Espresso :</strong> Ventes les plus élevées dans le Centre et les plus basses dans le Nord.</li>
            <li><strong>Lungo :</strong> Ventes les plus élevées dans le Centre et les plus basses dans le Sud.</li>
            <li><strong>Latte :</strong> Ventes les plus élevées dans le Centre et les plus basses dans le Nord.</li>
            <li><strong>Cappuccino :</strong> Ventes les plus élevées dans le Sud et les plus basses dans le Centre.</li>
          </ul>
          
          <h4>Conclusion</h4>
          <p>
            La région Sud a les ventes les plus élevées pour la majorité des types de café, sauf pour l'Espresso, le Lungo et le Latte où le Centre domine.
            La région Centre a les ventes les plus basses pour la majorité des types de café, sauf pour l'Espresso, le Lungo et le Latte où le Nord a les ventes les plus basses.
          </p>
        </div>

        """ , unsafe_allow_html=True)

    # Affichage du diagramme en barres des moyennes par région
    df_avg_region.plot(kind='bar', figsize=(10, 6))

    plt.ylabel('Ventes moyennes')
    plt.xlabel('Régions')
    plt.xticks(rotation=0)
    st.pyplot(plt)
else:
    df_avg_channel.columns = ["Robusta", "Arabica", "Espresso", "Lungo", "Latte", "Cappuccino"]
    st.write(df_avg_channel)

    # Affichage du diagramme en barres des moyennes par canal
    df_avg_channel.plot(kind='bar', figsize=(10,6))
    plt.title('Moyenne des ventes par canal')
    plt.ylabel('Ventes moyennes')
    plt.xlabel('Canaux')
    plt.xticks(rotation=0)
    st.pyplot(plt)

st.header("Totaux des ventes")

option = st.selectbox("Par",("Région","Canal"))

if option == "Canal":
    total_coffee_by_channel = df.groupby('Channel')[df_numeric.columns].sum()
    view = st.toggle("Voir")
    st.dataframe(total_coffee_by_channel)


    if view:
        st.markdown("""
                        <div>
              <h3>Rapports</h3>
             <ul>
                <li><strong>Online :</strong>6 619 931 produits vendus</li>
                <li><strong>Store :</strong>7 999 569 de produits vendus</li>
              </ul>

              <h4>Conclusion</h4>
              <p>
                    Il vend plus en magasin que en ligne.
              </p>
            </div>

            """, unsafe_allow_html=True)
else:
    # Calculer le nombre total de cafés vendus par région
    total_coffee_by_region = df.groupby('Region')[df_numeric.columns].sum()
    view = st.toggle("Voir")
    st.dataframe(total_coffee_by_region)
    if view:
        st.markdown("""
                        <div>
              <h3>Rapports</h3>
             <ul>
                <li>Au centre, sud et nord il vende plus de <strong>Robusta</strong></li>
                <li>Au sud, il vende globalement plus de café qu'au nord et au centre</li>
                <li>Au Centre, il vende globalement moins de café</li>
              </ul>
            </div>
    
            """, unsafe_allow_html=True)




# Sélectionner uniquement les colonnes de ventes (produits)
product_cols = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
st.subheader("Distribution des Ventes par Produit")

product= st.selectbox("Histogramme pour :",product_cols)

fig, ax = plt.subplots(figsize=(10,6))
ax.hist(df[product], bins=20, color='skyblue', edgecolor='black')
plt.title(f"Distribution des ventes de {product}")
plt.xlabel("Ventes")
plt.ylabel("Fréquence")
st.pyplot(fig)



