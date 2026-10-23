import streamlit as st
import plotly.express as px
from climbing_location_fr.app.ui import mapper_color_type, mapper_color_nature, \
order_date, mapper_color_is_artificial, mapper_color_libre, mapper_color_saison 
from climbing_location_fr.app.cache_data import load_data

st.set_page_config(
    page_title='home-page-installations',
    layout='wide'   
)

data, data_natural, data_artificial = load_data()

st.title('Comparatif escalade naturelle et escalade artificielle')
st.divider()


left, right = st.columns([1, 1], gap='large')

with left:
    st.subheader(f'Escalade naturelle : {len(data_natural)} installations')
    fig1 = px.pie(data_natural, names="equip_type_name", hole=0.33,
                  title="Types d'équipements d'escalade naturelle en France", 
                  color="equip_type_name", color_discrete_map=mapper_color_type)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})
    
    fig1 = px.pie(data_natural, names="equip_saison", hole=0.33,
                      title="Types d'équipements d'escalade naturelle en France")
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

    fig1 = px.pie(data_natural, names="equip_acc_libre", hole=0.33,
                          title="Types d'équipements d'escalade naturelle en France")
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

   
    fig1 = px.pie(data_natural, names="equip_nature_grouped", hole=0.33,
                      title="Nature des équipements d'escalade naturelle en France",
                      color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

    fig1 = px.pie(data_natural, names="equip_prop_type", hole=0.33,
                          title="Nature des équipements d'escalade naturelle en France",
                          color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

    fig1 = px.pie(data_natural, names="equip_gest_type", hole=0.33,
                              title="Nature des équipements d'escalade naturelle en France",
                              color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})


with right:
    st.subheader(f'Escalade artificielle : {len(data_artificial)} installations')
    fig2 = px.pie(data_artificial, names="equip_type_name", hole=0.33,
                      title="Types d'équipements d'escalade artificielle en France",
                      color="equip_type_name", color_discrete_map=mapper_color_type)
    st.plotly_chart(fig2, config = {'scrollZoom': False})

    fig1 = px.pie(data_artificial, names="equip_nature_grouped", hole=0.33,
                  title="Nature des équipements d'escalade artificielle en France",
                  color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

    fig1 = px.pie(data, names="equip_prop_type", hole=0.33,
                              title="Nature des équipements d'escalade naturelle en France",
                              color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})


    
    fig1 = px.pie(data_artificial, names="equip_gest_type", hole=0.33,
                                  title="Nature des équipements d'escalade naturelle en France",
                                  color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

fig1 = px.bar(data.groupby(['equip_service_periode','is_natural']).size().reset_index(name="counts"), 
               x='equip_service_periode', y='counts', color='is_natural', barmode='group',
               color_discrete_map=mapper_color_is_artificial)
fig1.update_xaxes(categoryorder='array', categoryarray= order_date)
st.plotly_chart(fig1, config = {'scrollZoom': False})

fig1 = px.bar(data.groupby(['reg_nom', 'is_natural']).size().reset_index(name="counts").
              sort_values(by='counts', ascending=False),
               x='reg_nom', y='counts', color='is_natural', barmode='group', 
               color_discrete_map=mapper_color_is_artificial)
fig1.update_xaxes(categoryorder='array', categoryarray= order_date)
st.plotly_chart(fig1, config = {'scrollZoom': False})
