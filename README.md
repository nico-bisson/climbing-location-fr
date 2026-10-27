# Climbing location FR

Projet sur les installations d'escalade en France, les données proviennent de
 [l'API du ministère des Sport.](https://equipements.sports.gouv.fr/)

Pour scrapper la base de données, par défaut on scrappe les équipements qui
ont comme mention l'escalade possibilité de scrapper un autre type d'activité avec
l' argument --activity :
```python
uv run scripts/fetcher_data_gouv_sport.py
uv run scripts/fetcher_data_gouv_sport.py --activity aviron
```

La visualisation des données est disponible via [Streamlit Community Cloud](https://climbing-location-fr-j2mpwechowfztrmsp6xs5t.streamlit.app/).   

Elle propose un comparatif des équipements d’escalade en milieu naturel et artificiel, ainsi qu’une carte interactive des sites d’escalade en milieu naturel en France.

Possibilité de run en local avec:
```python
streamlit  run src/climbing_location_fr/app/home.py
```

