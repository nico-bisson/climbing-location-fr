from pathlib import Path


def find_project_root() -> Path:
    current = Path(__file__).resolve()

    for parent in current.parents:
        if (parent / ".git").exists():
            return parent

    raise FileNotFoundError(
        f"No root git found from {current}"
    )

def get_data_path() -> Path:
    return Path(find_project_root(), 'data', 'equipements_escalade.csv')

