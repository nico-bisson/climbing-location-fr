import streamlit as st
import plotly.express as px
from climbing_location_fr.app.ui import mapper_color_type, mapper_color_libre, mapper_color_saison 
from climbing_location_fr.app.cache_data import load_data

st.set_page_config(
    page_title='Sunburst',
    layout='wide'   
)

st.title("Sunburst des installations d'escalade")

st.markdown("""
De l'intérieur à l'extérieur : accès libre, accès saisonnier et type d'installation.  
Sunburst intéractif : Cliquez sur les cercles intérieurs pour sélectionner une partie des données à afficher.
""" )

data, _, _ = load_data()


bool_matcher = {
    True: {"equip_acc_libre": "libre", "equip_saison": "saisonnier"},
    False: {"equip_acc_libre": "non libre", "equip_saison": "non saisonnier"},
}


data["liberte_label"] = data["equip_acc_libre"].map(
    lambda value: bool_matcher[value]["equip_acc_libre"] # pyright: ignore[reportArgumentType]
)

data["saison_label"] = data["equip_saison"].map(
    lambda value: bool_matcher[value]["equip_saison"] # pyright: ignore[reportArgumentType]
)

data = (
    data.groupby(
        ["equip_type_name", "saison_label", "liberte_label"]
    )
    .size()
    .reset_index(name="count")
)

fig = px.sunburst(
    data,
    path=["liberte_label", "saison_label", "equip_type_name"],
    values="count",
    color="equip_type_name",
    color_discrete_map=mapper_color_type,
    width=800,  # Width in pixels
    height=800
)
# Attribuer une couleur à chaque secteur selon son niveau
colors = []

for label, ident in zip(fig.data[0].labels, fig.data[0].ids): # type: ignore
    parts = ident.split("/")

    if len(parts) == 1:
        # Cercle central : accès libre
        color = mapper_color_libre.get(label, "lightgray")

    elif len(parts) == 2:
        # Anneau du milieu : saisonnalité
        saison = parts[1]
        color = mapper_color_saison.get(saison, "lightgray")

    else:
        # Anneau extérieur : type d'équipement
        color = mapper_color_type.get(label, "lightgray")

    colors.append(color)

fig.update_traces(marker=dict(colors=colors))

st.plotly_chart(fig, width="stretch")