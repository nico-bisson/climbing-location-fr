
import folium
import html
from folium.plugins import FastMarkerCluster
import streamlit as st
from streamlit_folium import st_folium
from climbing_location_fr.app.cache_data import load_data

st.set_page_config(layout='wide')
st.title("🗺️🌿Carte interactive de l'escalade naturelle")

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
.dropna(subset=["equip_x", "equip_y", "equip_type_name"])

layer_names = {
    "Site d'escalade en falaise": "🟢 Site d'escalade en falaise",
    "Site de blocs d'escalade": "🟠 Site de blocs d'escalade",
    "Cascade de glace": "🔵 Cascade de glace",
    "Via ferrata / Via corda": "🔴 Via ferrata / Via corda",
}

map = folium.Map(location = [47, 1],
                   zoom_start = 6,
                   tiles = "OpenTopoMap")

marker_clusters_data = {key: [] for key in mapper_color_type}

for nom, date, period, inst_nom, cat, lon, lat, narrow_adress, cp, city, \
acc_libre, saison, public in data_to_plot.itertuples(index=False, name=None):

    if cat not in marker_clusters_data:
        continue

    parsed_date = parse_date(date, period)

    # Escape text before inserting it into HTML
    inst_nom = html.escape(str(inst_nom))
    narrow_adress = html.escape(str(narrow_adress))
    cp = html.escape(str(cp))
    city = html.escape(str(city))
    public = html.escape(str(public))

    text_html = f"""
    <div style="width:180px;font-size:12px;line-height:1.4">
        <b>Nom de l'équipement :</b> {inst_nom}<br>
        <b>Année/période :</b> {parsed_date}<br>
        <b>Adresse :</b> {narrow_adress}, {cp}, {city}<br>
        <b>Accès au public :</b>
        {acc_libre},
        {saison}<br>
        <b>Public :</b> {public}
    </div>
    """

    marker_clusters_data[cat].append([
        lat,
        lon,
        text_html,
        mapper_color_type[cat],
    ])

# JavaScript callback: create each marker, popup and tooltip
callback = """
function(row) {
    var marker = L.marker([row[0], row[1]], {
        icon: L.divIcon({
            className: '',
            html: '<div style="' +
                'background-color:' + row[3] + ';' +
                'width:24px;height:24px;border-radius:50%;' +
                'border:2px solid white;' +
                'box-shadow:0 1px 4px #555;' +
                '"></div>',
            iconSize: [24, 24],
            iconAnchor: [12, 12]
        })
    });

    marker.bindPopup(row[2]);
    marker.bindTooltip("Click me");

    return marker;
}
"""
for cat, marker_data in marker_clusters_data.items():
    color = mapper_color_type[cat]

    icon_create_function = f"""
    function(cluster) {{
        return L.divIcon({{
            html: '<div style="background-color:{color};'
                + 'color:white;'
                + 'border-radius:50%;'
                + 'width:40px;height:40px;'
                + 'display:flex;'
                + 'align-items:center;'
                + 'justify-content:center;'
                + 'font-weight:bold;'
                + 'border:2px solid white;'
                + 'box-shadow:0 1px 4px #555;">'
                + cluster.getChildCount()
                + '</div>',
            className: 'custom-marker-cluster',
            iconSize: new L.Point(44, 44)
        }});
    }}
    """

    FastMarkerCluster(
        data=marker_data,
        callback=callback,
        icon_create_function=icon_create_function,
        options={
            "disableClusteringAtZoom": 10,
            "spiderfyOnMaxZoom": True,
        },
        name=layer_names[cat],
        overlay=True,
        control=True,
    ).add_to(map)

folium.LayerControl(collapsed=False).add_to(map)

st_folium(map, use_container_width=True, 
          returned_objects=[] ### this or it reruns the map at each click
          )
