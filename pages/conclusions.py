import streamlit as st


st.title("Conclusions")
st.subheader("Analyse et interpretation des tendances")

st.write("https://github.com/RIKIEL-K/data-analysis-and-model-conception")


st.markdown("""
    <div>
    <p>Par le calcul des totaux par region et par canaux, on constate que: <p>
    <p>
        <strong>La région Sud</strong> a les ventes les plus élevées pour tous les types de café.
        La <strong>région Nord</strong> suit avec des ventes significatives, mais inférieures à celles du Sud.
        La <strong>région Centre</strong> a les ventes les plus basses pour tous les types de café.
    </p>
    <p>
        La region du sud est donc la plus rentable ce qui est un facteur qu'on utilisera par la suite pour donner des directives
    </p>
    
</div>
    <div>
    <p>En ce qui concerne les moyennes : </p>
    <p>
        Les ventes en magasin montrent des moyennes élevées pour le type de café Robusta, ce qui indique une préférence des clients en magasin pour ce produit. 
        Les ventes de Lungo et Espresso sont également significatives, tandis que les ventes de Arabica, Latte et Cappuccino sont relativement faibles.
</div>

""", unsafe_allow_html=True)

st.markdown("""
    <div>
    <p>De plus,il vend plus en de café en magasin qu'en ligne .Et le café le plus vendu en magasin est le Robusta.Il pourrais mettre l'accent sur le Latté et le Cappuccino car ce sont les produits les moins vendus en magasin. </p>  
    </div>

""", unsafe_allow_html=True)

st.subheader("Suggestions de données supplementaires à collecter")
st.markdown("""
        <div>
        <p>Les données recoltées par Beans&Pods sont insuffisantes.Il ne permette pas de comprendre l'evolution des ventes, des préférences clients et de prédire les achats des clients.
        Voici les données que l'entreprise doit collecter en plus :
        </p>
             <ul>
                <li><strong>l'age du client: </strong>Collecter l'âge des clients peut aider à comprendre les données démographiques et à cibler des groupes d'âge spécifiques.</li>
                <li><strong>Genre du client: </strong>Collecter des informations sur le genre peut aider à comprendre les préférences de café en fonction des différents genres.</li>
                <li><strong>Date d'achat: </strong> Collecter la date d'achat peut aider à identifier les tendances saisonnières et les périodes de vente de pointe.</li>
                <li><strong>Statut de fidélité du client: </strong>Collecter des informations sur le statut de fidélité des clients peut aider à identifier les clients réguliers et à les récompenser.</li>
                <li><strong>Prix du produit: </strong>Collecter le prix de chaque produit vendu peut aider à analyser l'impact des prix sur les ventes.</li>
                <li><strong>Remise appliquée: </strong>Collecter des informations sur les remises appliquées peut aider à comprendre l'efficacité des promotions et des réductions.</li>
              </ul>
        </div>
         """, unsafe_allow_html=True)

st.subheader("Recommandations pour la nouvelle campagne de marketing")
st.markdown("""
    <div>      
    <p></p>
    <ul>
        <li><strong>Focus sur la région Sud :</strong> La région Sud a les ventes les plus élevées pour la plupart des types de café. Investir dans des campagnes de marketing ciblant cette région pourrait générer des revenus plus élevés.</li>
        <li><strong>Promouvoir les ventes en ligne :</strong> Les canaux de vente en ligne montrent des chiffres de vente significatifs. Améliorer les stratégies de marketing en ligne et les promotions pourrait augmenter les ventes.</li>
        <li><strong>Cibler les types de café populaires :</strong> Les grains de Robusta et Arabica ont des ventes élevées. Les campagnes de marketing mettant en avant ces types de café populaires pourraient attirer plus de clients.</li>
        <li><strong>Analyser les préférences des clients :</strong> Collecter des données supplémentaires sur les préférences des clients, telles que les types de café préférés, la fréquence d'achat et les retours. Ces informations peuvent aider à adapter les campagnes de marketing pour répondre aux besoins des clients.</li>
        <li><strong>Promotions saisonnières :</strong> Envisager des promotions saisonnières et des réductions pour attirer plus de clients pendant les périodes de pointe.</li>
        <li><strong>Élargir la gamme de produits :</strong> Explorer les opportunités d'introduire de nouveaux produits ou saveurs de café en fonction des retours des clients et des tendances du marché.</li>
    </ul>
    </div>
    
            """, unsafe_allow_html=True)




