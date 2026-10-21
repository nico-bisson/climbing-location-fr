import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import seaborn as sns

    return mo, pd, px, sns


@app.cell
def _(pd):
    data = pd.read_csv("data/equipements_escalade.csv")
    return (data,)


@app.cell
def _(data):
    data.head()
    return


@app.cell
def _(data):
    data["aps_name"].value_counts()
    return


@app.cell
def _(data):
    data.isna().sum()
    return


@app.cell
def _(data):
    (
        data["equip_acc_libre"].value_counts(),
        data["equip_nature"].value_counts(),
        data["equip_type_name"].value_counts(),
    )
    return


@app.cell
def _(data):
    near_climbing = ["Site de spéléologie sportive et/ou éducative", "Canyon"]
    query = ["Salle multisports (gymnase)"]
    data.query("equip_type_name in @query")
    return


@app.cell
def _(data):
    def cleaner_data(data=data):
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

    return (cleaner_data,)


@app.cell
def _(cleaner_data):
    clean_data = cleaner_data()
    clean_data.head()
    clean_data.columns
    return (clean_data,)


@app.cell
def _(clean_data):
    clean_data.sort_values(by="equip_surf", ascending=False)["equip_surf"]
    return


@app.cell
def _(clean_data, pd, sns):
    sns.heatmap(
        pd.crosstab(clean_data["equip_type_name"], clean_data["equip_nature"]),
        cmap="Oranges",
        annot=True,
        fmt="1d",
    )
    return


@app.cell
def _(clean_data):
    tmp = ["Structure Artificielle d'Escalade", "Blocs artificiels d'Escalade"]
    filtered_data = clean_data.query("equip_nom in @tmp")
    return (filtered_data,)


@app.cell
def _(clean_data, pd, sns):
    sns.heatmap(
        pd.crosstab(clean_data["equip_type_name"], clean_data["equip_nature"]),
        cmap="Oranges",
        annot=True,
        fmt="1d",
    )
    return


@app.cell
def _(clean_data):
    clean_data.groupby("equip_type_name")
    return


@app.cell
def _(clean_data, px):
    fig1 = px.pie(
        clean_data,
        names="equip_type_name",
        hole=0.33,
        title="Types d'équipements d'escalade en France",
    )
    fig1.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    fig1.show()

    fig2 = px.pie(
        clean_data, names="equip_nature", hole=0.3, title="Exterieur interieur"
    )
    fig2.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    fig2.show()

    fig3 = px.pie(
        clean_data, names="equip_nature", hole=0.3, title="Exterieur interieur"
    )
    fig3.update_traces(hoverinfo="label+percent", textinfo="value+percent")
    fig3.show()
    return


@app.cell
def _(clean_data):
    clean_data.query('equip_nature == "Site artificiel"')
    return


@app.cell
def _(clean_data):
    counts = clean_data["equip_x"].value_counts()
    clean_data[clean_data["equip_x"].isin(counts[counts > 1].index)]
    return


@app.cell
def _(clean_data):
    clean_data["equip_nom"].value_counts()
    return


@app.cell
def _(clean_data):
    clean_data.groupby(["inst_numero"]).equip_type_name.value_counts().sort_values(
        ascending=False
    ).head(10).plot(kind="bar")
    return


@app.cell
def _(clean_data):
    clean_data[
    clean_data["equip_type_name"] == "Site de blocs d'escalade"]
    return


@app.cell
def _(clean_data, mo):
    _df = mo.sql(
        f"""
        SELECT inst_numero, inst_nom, count(*) as total FROM clean_data
        GROUP BY inst_numero, inst_nom
        ORDER BY total DESC
        limit 10
        """
    )
    return


@app.cell
def _(clean_data, mo):
    _df = mo.sql(
        f"""
        SELECT inst_numero, inst_nom, equip_type_name, count(*) as total FROM clean_data
        where equip_type_name = 'Parcours Acrobatique en Hauteur/Site d''accrobranche'
        GROUP BY inst_numero, inst_nom, equip_type_name
        ORDER BY total DESC
        limit 10
        """
    )
    return


@app.cell
def _(clean_data, mo):
    _df = mo.sql(
        f"""
        SELECT equip_type_name, inst_nom, equip_nom, count(*) FROM clean_data
        where equip_type_name = 'Parcours Acrobatique en Hauteur/Site d''accrobranche' 
        AND inst_nom = 'BISC''AVENTURE'
        group by equip_type_name, inst_nom, equip_nom
        """
    )
    return


@app.cell
def _(clean_data):
    clean_data["aps_name"].str.replace({"[": "", "]": "", "'": ""}).str.split(
        ", "
    ).value_counts()
    return


@app.cell
def _(clean_data):
    clean_data["aps_name"][0]
    return


if __name__ == "__main__":
    app.run()
