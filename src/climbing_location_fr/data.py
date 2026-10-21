import pandas as pd

def cleaner_data(data: pd.DataFrame) -> pd.DataFrame :
    data = data.copy()
    counts = data["equip_type_name"].value_counts()
    cols_to_filter = counts[counts > 20].index
    # remove equip not exalty for the climbing practice
    cols_to_filter = cols_to_filter[
        ~cols_to_filter.isin(
            [
                "Refuge de montagne",
                "Parcours Acrobatique en Hauteur/Site d'accrobranche",
                "Salle multisports (gymnase)",
            ]
        )
    ]
    data = data.query("equip_type_name in @cols_to_filter")
    # only two découvrable for the same center seems a typo
    # data['equip_nature'] = data['equip_nature'].replace({'Découvrable' : 'Découvert'})

    # transform row text to list of str
    for col in ["equip_utilisateur_filter", "aps_name"]:
        data[col] = (
            data[col].str.replace({"[": "", "]": "", "'": ""}).str.split(", ")
        )

    return data
