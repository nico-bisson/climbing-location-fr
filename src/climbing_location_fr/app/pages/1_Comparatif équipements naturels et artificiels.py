import streamlit as st
import plotly.express as px
from climbing_location_fr.app.ui import mapper_color_type, mapper_color_nature, \
order_date, mapper_color_is_artificial, mapper_color_libre, mapper_color_saison, create_color_mapper
from climbing_location_fr.app.cache_data import load_data

st.set_page_config(
    page_title='home-page-installations',
    layout='wide'   
)

data, data_natural, data_artificial = load_data()

mapper_color_prop_type = create_color_mapper(
    data, "equip_prop_type"
)
mapper_color_gest_type = create_color_mapper(
    data, "equip_gest_type"
)
mapper_color_equip_nature_grouped = create_color_mapper(
    data, "equip_nature_grouped"
)

st.title('Comparatif escalade naturelle et escalade artificielle')
st.divider()


left, right = st.columns([1, 1], gap='large')

with left:
    st.subheader(f'Escalade naturelle : {len(data_natural)} installations')
    fig1 = px.pie(data_natural, names="equip_type_name", hole=0.33,
                  title="Type de l'équipement", 
                  color="equip_type_name", color_discrete_map=mapper_color_type)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})
    
    fig2 = px.pie(data_natural, names="equip_saison", hole=0.33,
                      title="Equipement saisonnier",
                      color="equip_saison", color_discrete_map=mapper_color_saison)
    fig2.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig2, config = {'scrollZoom': False})

    fig3 = px.pie(data_natural, names="equip_acc_libre", hole=0.33,
                          title="Equipement en accès libre ou non",
                          color="equip_acc_libre", color_discrete_map=mapper_color_libre)
    fig3.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig3, config = {'scrollZoom': False})

   
    fig4 = px.pie(data_natural, names="equip_nature_grouped", hole=0.33,
                      title="Nature de l'équipement",
                      color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig4.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig4, config = {'scrollZoom': False})

    fig5 = px.pie(data_natural, names="equip_prop_type", hole=0.33,
                          title="Propriétaire de l'équipement",
                          color="equip_prop_type", color_discrete_map=mapper_color_prop_type)
    fig5.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig5, config = {'scrollZoom': False})

    fig6 = px.pie(data_natural, names="equip_gest_type", hole=0.33,
                              title="Gestionnaire de l'équipement",
                              color="equip_gest_type", color_discrete_map=mapper_color_gest_type)
    fig6.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig6, config = {'scrollZoom': False})


with right:
    st.subheader(f'Escalade naturelle : {len(data_artificial)} installations')
    fig1 = px.pie(data_artificial, names="equip_type_name", hole=0.33,
                  title="Type de l'équipement", 
                  color="equip_type_name", color_discrete_map=mapper_color_type)
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig1, config = {'scrollZoom': False})

    fig2 = px.pie(data_artificial, names="equip_saison", hole=0.33,
                      title="Equipement saisonnier",
                      color="equip_saison", color_discrete_map=mapper_color_saison)
    fig2.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig2, config = {'scrollZoom': False})

    fig3 = px.pie(data_artificial, names="equip_acc_libre", hole=0.33,
                          title="Equipement en accès libre ou non",
                          color="equip_acc_libre", color_discrete_map=mapper_color_libre)
    fig3.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig3, config = {'scrollZoom': False})

   
    fig4 = px.pie(data_artificial, names="equip_nature_grouped", hole=0.33,
                        title="Nature de l'équipement",
                        color="equip_nature_grouped", color_discrete_map=mapper_color_nature)
    fig4.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig4, config = {'scrollZoom': False})

    fig5 = px.pie(data_artificial, names="equip_prop_type", hole=0.33,
                            title="Propriétaire de l'équipement",
                            color="equip_prop_type", color_discrete_map=mapper_color_prop_type)
    fig5.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig5, config = {'scrollZoom': False})

    fig6 = px.pie(data_artificial, names="equip_gest_type", hole=0.33,
                                title="Gestionnaire de l'équipement",
                                color="equip_gest_type", color_discrete_map=mapper_color_gest_type)
    fig6.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    st.plotly_chart(fig6, config = {'scrollZoom': False})


fig1 = px.bar(data.groupby(['equip_service_periode','is_natural']).size().reset_index(name="counts"), 
               x='equip_service_periode', y='counts', color='is_natural', barmode='group',
               title="Période en années de mise en service des équipements",
               color_discrete_map=mapper_color_is_artificial)
fig1.update_xaxes(categoryorder='array', categoryarray= order_date)
st.plotly_chart(fig1, config = {'scrollZoom': False})

fig1 = px.bar(data.groupby(['reg_nom', 'is_natural']).size().reset_index(name="counts").
              sort_values(by='counts', ascending=False),
               x='reg_nom', y='counts', color='is_natural', barmode='group',
               title="Réparition par région des équipements", 
               color_discrete_map=mapper_color_is_artificial)
fig1.update_xaxes(categoryorder='array', categoryarray= order_date)
st.plotly_chart(fig1, config = {'scrollZoom': False})
