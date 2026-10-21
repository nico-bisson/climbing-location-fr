import argparse
from requests import RequestException, Session
from tqdm import tqdm
import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Scraper les équipements sportifs par activité."
    )
    parser.add_argument(
        "--activity",
        default="escalade",
        help="Activité sportive à scraper (défaut : escalade).",
    )
    activity = parser.parse_args().activity

    url = "https://equipements.sports.gouv.fr/api/explore/v2.1/catalog/datasets/data-es/records"

    params = {
        "select": (
            "equip_numero, equip_nom, inst_numero, inst_nom,"
            "inst_adresse, inst_cp, new_name, dep_nom, reg_nom, equip_x, equip_y,"
            "equip_type_name, equip_nature, equip_acc_libre, equip_saison, equip_surf,"
            "equip_prop_type, equip_gest_type,"
            "equip_service_date, equip_service_periode,"
            "equip_utilisateur_filter, aps_name"
        ),
        "where": f'aps_name LIKE "%{activity}%"',
        "limit": 100,
        "offset": 0,
    }

    data = []

    with Session() as session:
        with tqdm(desc="Récupération des équipements", unit="équipement") as pbar:
            while True:
                try:
                    response = session.get(url, params=params, timeout=60)
                    response.raise_for_status()
                    response = response.json()

                    results = response["results"]
                    total_count = response["total_count"]

                    if not results:
                        break

                    data.extend(results)

                    pbar.total = total_count
                    pbar.update(len(results))

                    params["offset"] += len(results)
                    if params["offset"] >= total_count:
                        break

                except (RequestException, ValueError, KeyError) as e:
                    print(f"Erreur lors de la récupération : {e}")
                    break

    df = pd.DataFrame(data)
    print("Nombre total de résultats :", len(df))

    if not df.empty:
        output_path = f"data/equipements_{activity}.csv"
        df.to_csv(output_path, index=False)
        print(f"Données enregistrées dans {output_path}")
    else:
        print("Aucun résultat à enregistrer.")


if __name__ == "__main__":
    main()