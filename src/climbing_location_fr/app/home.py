import streamlit as st

st.set_page_config(
    page_title="À la découverte de l'escalade en France",
    page_icon="🧗",
    layout="wide",
)

st.title("🧗 À la découverte des sites d’escalade en France")

st.markdown("""
Cette application explore les équipements d’escalade recensés dans la
[base de données des équipements sportifs du ministère des Sports](https://equipements.sports.gouv.fr/pages/donnees/).

### Au programme
- 🗺️ **Où grimper ?** Explorez les sites d’escalade en milieu naturel en France grâce à une carte interactive.
- 🌿 **Nature ou artificiel ?** Comparez les équipements d’escalade en milieu naturel et artificiel.
- 🏠 **Quels types d’installations ?** Découvrez les structures intérieures et extérieures.
- 📅 **Quand ont-ils été mis en service ?** Explorez les dates et périodes de mise en service des équipements.
- 🔑 **À qui appartiennent-ils ?** Consultez les informations sur les propriétaires, les gestionnaires et les conditions d’accès.

**L’objectif : valoriser les données publiques pour mieux comprendre et explorer le paysage de l’escalade en France.**
""")