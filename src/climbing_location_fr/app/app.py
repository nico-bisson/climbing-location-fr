import streamlit as st


home = st.Page(
    "pages/home.py",
    title="🧗 À la découverte des équipements d'escalade en France",
)

comparatif = st.Page(
    "pages/comparatif.py",
    title="🌿🧱 Comparatif escalade naturelle et escalade artificielle",
)

sunburst = st.Page(
    "pages/sunburst.py",
    title="🔗 Relation type d'installation et accès",
)

carte = st.Page(
    "pages/interactive_map.py",
    title="🗺️🌿 Carte interactive de l'escalade naturelle",
    icon="",
    default=True,
)



pg = st.navigation([home, comparatif, sunburst, carte])
pg.run()