# ScrapJob — Dashboard d'offres d'emploi Data

Application de veille sur les offres d'emploi dans le domaine de la Data au Maroc : un scraper collecte automatiquement les annonces publiées sur [rekrute.com](https://www.rekrute.com), les stocke dans MongoDB, et un dashboard Streamlit permet de les explorer visuellement.

## Fonctionnalités

- **Scraping automatisé** : récupération des offres (poste, ville, lien) toutes les heures via `requests` + `BeautifulSoup`
- **Stockage MongoDB** avec déduplication (mise à jour des offres existantes plutôt que doublons)
- **Dashboard interactif** (Streamlit) :
  - Filtrage des offres par ville
  - Statistiques en temps réel (nombre d'offres, nombre de villes)
  - Graphique des postes les plus demandés par ville
  - Tableau interactif avec liens cliquables vers les annonces
    
## Stack technique

| Composant | Technologie |
|---|---|
| Scraping | Python, `requests`, `BeautifulSoup4` |
| Planification | `schedule` |
| Base de données | MongoDB |
| Dashboard | `Streamlit`, `pandas`, `plotly` |
| Configuration | `python-dotenv` |

## Structure du projet

```
JobScrapper/
├── ScrapJob.py           # Scraper : collecte et stockage des offres
├── dashboard.py          # Dashboard Streamlit
├── .streamlit/
│   └── config.toml       # Thème visuel du dashboard
├── .env                  # Variables d'environnement (non versionné)
├── .gitignore
└── requirements.txt
```

## Installation

1. Cloner le dépôt puis se placer dans le dossier du projet

2. Créer et activer un environnement virtuel
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows (PowerShell)
```

3. Installer les dépendances
```bash
pip install pymongo streamlit pandas plotly beautifulsoup4 requests schedule python-dotenv
```

4. Configurer les variables d'environnement — créer un fichier `.env` à la racine :
```
MONGO_URI=mongodb://localhost:27017/
```

## Utilisation

**Lancer le scraper** (collecte les offres et les stocke en base) :
```bash
python ScrapJob.py
```

**Lancer le dashboard** :
```bash
streamlit run dashboard.py
```

Le dashboard est ensuite accessible sur `http://localhost:8501`.

