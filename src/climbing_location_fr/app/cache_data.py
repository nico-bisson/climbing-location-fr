import streamlit as st
import pandas as pd
from climbing_location_fr.data import cleaner_data
from climbing_location_fr.paths import get_data_path
from climbing_location_fr.app.ui import natural
## resource partagée entre les pages

@st.cache_resource
def load_data():
    data = cleaner_data(pd.read_csv(get_data_path()))

    bool_matcher = {
    True: {"equip_acc_libre": "libre", "equip_saison": "saisonnier"},
    False: {"equip_acc_libre": "non libre", "equip_saison": "non saisonnier"},}
    data["equip_acc_libre"] = data["equip_acc_libre"].map(
    lambda value: bool_matcher[value]["equip_acc_libre"]) # pyright: ignore[reportArgumentType])
    data["equip_saison"] = data["equip_saison"].map(
    lambda value: bool_matcher[value]["equip_saison"]) # pyright: ignore[reportArgumentType])

    print(list(data['equip_service_periode'].value_counts().index))
    data_natural = data.query('equip_type_name in @natural')
    data_artificial = data.query('equip_type_name not in @natural')
    data["is_natural"] = data["equip_type_name"].isin(natural).replace({True:'naturel', False: 'artificiel'}) # pyright: ignore[reportArgumentType]

    return data, data_natural, data_artificial
