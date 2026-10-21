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


