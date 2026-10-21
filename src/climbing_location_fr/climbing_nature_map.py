import folium
import pandas as pd
from folium.plugins import MarkerCluster

from climbing_location_fr.data import cleaner_data

def parse_date(date, period):
        try:
            return int(date)
        except (ValueError, TypeError):
            try: str(period)
            except (ValueError, TypeError):
                return 'inconnue'

bool_matcher = {
    True: {"liberté": "libre", "saison": "saisonnier"},
    False: {"liberté": "non libre", "saison": "non saisonnier"},
}

data = cleaner_data(pd.read_csv('data/equipements_escalade.csv'))

data = data[['equip_nom', 'equip_service_date', 'equip_service_periode',
              'inst_nom', 'equip_type_name', 'equip_x', 'equip_y', 
              'inst_adresse', 'inst_cp','new_name',
              'equip_acc_libre', 'equip_saison', 'equip_utilisateur_filter']
              ].dropna().iloc[:,:]

natural = ["Site d'escalade en falaise", "Site de blocs d'escalade",
            "Cascade de glace", "Via ferrata / Via corda"]

artificial = ["Structure Artificielle d'Escalade", 
              "Salle de blocs artificiels d'escalade", 
              "Blocs artificiels d'escalade"]


data = data.query('equip_type_name in @natural')

mapper_color = {"Site d'escalade en falaise" : 'green',
                "Site de blocs d'escalade": "orange",
                "Cascade de glace": "lightblue",
                "Via ferrata / Via corda": "red"}

map = folium.Map(location = [47, 1],
                   zoom_start = 6,
                   tiles = "OpenTopoMap")

marker_clusters = {
    key: MarkerCluster(
        disableClusteringAtZoom=12,
        spiderfyOnMaxZoom=True, # markers pas superposés ! marche pas ??
        icon_create_function=f"""
        function(cluster) {{
            return new L.DivIcon({{
                html: '<div style="background-color:{mapper_color[key]};'
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
    for key in mapper_color.keys()
}


for nom, date, period, inst_nom, cat, lon, lat, narrow_adress, cp, city, \
acc_libre, saison , public in data.itertuples(index=False, name=None):

    parsed_date = parse_date(date, period)
    text_html = f"""
    <div style="width: 200px; line-height: 1.5;">
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
                                   color=mapper_color[cat]),
                  tooltip="Click me",
                  ).add_to(marker_clusters[cat])

map.save('my_map.html')
#webbrowser.open('my_map.html')
