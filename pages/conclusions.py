import streamlit as st


st.title("Conclusions")
st.subheader("Analyse et interpretation des tendances")

st.markdown("""
    <div style="font-family: Arial, sans-serif; color: #333;">
    <p>Par le calcul des totaux par region et par canaux, on constate que: <p>
    <p style="font-size: 16px; line-height: 1.6;">
        <strong>La région Sud</strong> a les ventes les plus élevées pour tous les types de café.
        La <strong>région Nord</strong> suit avec des ventes significatives, mais inférieures à celles du Sud.
        La <strong>région Centre</strong> a les ventes les plus basses pour tous les types de café.
    </p>
    <p style="font-size: 16px; line-height: 1.6;">
        La region du sud est donc la plus rentable ce qui est un facteur qu'on utilisera par la suite pour donner des directives
    </p>
    
</div>
    <div style="font-family: Arial, sans-serif; color: #333;">
    <p>En ce qui concerne les moyennes : </p>
    <p style="font-size: 16px; line-height: 1.6; ">
        Les ventes en magasin montrent des moyennes élevées pour le type de café Robusta, ce qui indique une préférence des clients en magasin pour ce produit. 
        Les ventes de Lungo et Espresso sont également significatives, tandis que les ventes de Arabica, Latte et Cappuccino sont relativement faibles.
    </p>
    
    
    <p style="font-size: 16px; line-height: 1.6;">
        Les moyennes des ventes par canal montrent des différences dans les préférences des clients en ligne et en magasin. 
        Les clients en ligne préfèrent les types de café Arabica et Espresso, tandis que les clients en magasin préfèrent le type de café Robusta. 
        Les campagnes de marketing devraient être adaptées pour cibler ces préférences spécifiques afin d'optimiser les ventes.
    </p>

</div>

""", unsafe_allow_html=True)

