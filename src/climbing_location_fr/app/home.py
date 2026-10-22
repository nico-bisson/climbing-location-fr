import streamlit as st

st.set_page_config(
    page_title="À la découverte de l'escalade en France",
    page_icon="🧗",
    layout="wide",
)

st.title("🧗 À la découverte des sites d’escalade en France")

st.markdown("""
Cette application explore les équipements d’escalade recensés dans la base de
données des équipements sportifs du ministère français des Sports. [source](https://equipements.sports.gouv.fr/pages/donnees/)
### Au programme
- 📍 **Où grimper ?** Répartition par coordonnées, département et région.
- 🌿 **Nature ou artificiel ?** Falaises, blocs et structures artificielles.
- 🏠 **Intérieur ou extérieur ?** Explorez les types d’installations.
- 📅 **Depuis quand ?** Dates et périodes de mise en service.
- 🔑 **À qui appartiennent-ils ?** Propriétaires, gestionnaires et conditions d’accès.

**L’objectif : transformer des données brutes en une vision plus claire du
paysage de l’escalade en France.**
""")
