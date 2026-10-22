import streamlit as st
import pandas as pd
from climbing_location_fr.data import cleaner_data
from climbing_location_fr.paths import get_data_path
from climbing_location_fr.app.ui import natural
## resource partagée entre les pages

@st.cache_resource
def load_data():
    data = cleaner_data(pd.read_csv(get_data_path()))
    print(list(data['equip_service_periode'].value_counts().index))
    data_natural = data.query('equip_type_name in @natural')
    data_artificial = data.query('equip_type_name not in @natural')
    data["is_natural"] = data["equip_type_name"].isin(natural).replace({True:'naturel', False: 'artificiel'}) # pyright: ignore[reportArgumentType]

    return data, data_natural, data_artificial
