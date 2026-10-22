
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import st_folium
from climbing_location_fr.app.cache_data import load_data
#from climbing_location_fr.app.ui import mapper_color_type

st.set_page_config(layout="wide")
st.set_page_config(
    page_title="Carte intéractive de l'escalade naturelle",
    layout='wide'   
)

st.title("Carte intéractive de l'escalade naturelle")


def parse_date(date, period):
        try:
            return int(date)
        except (ValueError, TypeError):
            try: str(period)
            except (ValueError, TypeError):
                return 'inconnue'

mapper_color_type = {
    "Site d'escalade en falaise": "green",
    "Site de blocs d'escalade": "orange",
    "Cascade de glace": "lightblue",
    "Via ferrata / Via corda": "red"
}     

bool_matcher = {
    True: {"liberté": "libre", "saison": "saisonnier"},
    False: {"liberté": "non libre", "saison": "non saisonnier"},
}

_, data_natural, _ = load_data()

data_to_plot = data_natural[[
     'equip_nom', 'equip_service_date', 'equip_service_periode',
     'inst_nom', 'equip_type_name', 'equip_x', 'equip_y', 
     'inst_adresse', 'inst_cp','new_name',
     'equip_acc_libre', 'equip_saison', 'equip_utilisateur_filter']] \
.dropna(subset=["equip_x", "equip_y", "equip_type_name"]).iloc[0:100,:]


map = folium.Map(location = [47, 1],
                   zoom_start = 6,
                   tiles = "OpenTopoMap")

marker_clusters = {
    key: MarkerCluster(
        disableClusteringAtZoom=10,
        spiderfyOnMaxZoom=True, # markers pas superposés ! marche pas ??
        icon_create_function=f"""
        function(cluster) {{
            return new L.DivIcon({{
                html: '<div style="background-color:{mapper_color_type[key]};'
                    + 'color:white;border-radius:50%;'
                    + 'width:40px;height:40px;'
                    + 'display:flex;align-items:center;'
                    + 'justify-content:center;">'
                    + cluster.getChildCount()
                    + '</div>',
                className: 'marker-cluster',
                iconSize: new L.Point(40, 40)
            }});
        }}
        """
    ).add_to(map)
    for key in mapper_color_type.keys()
}

for nom, date, period, inst_nom, cat, lon, lat, narrow_adress, cp, city, \
acc_libre, saison , public in data_to_plot.itertuples(index=False, name=None):
    parsed_date = parse_date(date, period)
    text_html = f"""
    <div style="width: 180px; font-size: 12px; line-height: 1.2;">
    <b>Nom de l'équipement:</b> {inst_nom}<br>
    <b>Année/période de mise en service :</b> {parsed_date}<br>
    <b>Nom de l'installation :</b> {inst_nom}<br>
    <b>Adresse :</b> {narrow_adress}, {cp}, {city}<br>
    <b>Accès au public:</b> {bool_matcher[acc_libre]['liberté']}, 
    {bool_matcher[saison]['saison']}<br>
    <b>Public:</b> {public}<br>
    </div>
    """

    folium.Marker(location= [lat, lon], 
                  popup=folium.Popup(text_html),
                  icon=folium.Icon(icon="info-sign", prefix="glyphicon", 
                                   color=mapper_color_type[cat]),
                  tooltip="Click me",
                  ).add_to(marker_clusters[cat])

st_folium(map, use_container_width=True, 
          returned_objects=[] ### this or it reruns the map at each click
          )
