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

""", unsafe_allow_html=True)