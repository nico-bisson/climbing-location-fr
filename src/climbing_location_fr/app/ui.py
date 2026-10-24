import plotly.express as px

natural = ["Site d'escalade en falaise", "Site de blocs d'escalade",
            "Cascade de glace", "Via ferrata / Via corda"]

mapper_color_type = {
    "Site d'escalade en falaise": "green",
    "Site de blocs d'escalade": "orange",
    "Cascade de glace": "lightblue",
    "Via ferrata / Via corda": "red",

    "Blocs artificiels d'escalade": "darkorange",
    "Salle de blocs artificiels d'escalade": "gold",
    "Structure Artificielle d'Escalade": "purple",
}

mapper_color_nature = {
    "Naturel": "forestgreen",
    "Naturel aménagé": "lightgreen",
    "Intérieur": "royalblue",
    "Extérieur": "goldenrod",
    "Extérieur couvert": "darkorange",
    "Artificiel": "slategray",
}

mapper_color_is_artificial = {
    'artificiel' :'purple',
    'naturel': 'green',
}

mapper_color_libre = {
    "libre": "seagreen",
    "non libre": "indianred",
}

mapper_color_saison = {
    "saisonnier": "darkorange",
    "non saisonnier": "steelblue",
}

order_date = ['Avant 1945', '1945-1964', '1965-1974', '1975-1984', '1985-1994',
               '1995-2004', 'A partir de 2005']

def create_color_mapper(data, column, palette=px.colors.qualitative.Safe):
    categories = sorted(data[column].dropna().unique(), key=str)

    return {
        category: palette[i % len(palette)]
        for i, category in enumerate(categories)
    }