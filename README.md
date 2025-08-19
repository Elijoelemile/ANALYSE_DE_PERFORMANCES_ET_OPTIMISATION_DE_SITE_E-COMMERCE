# 📊 Analyse de Performances et Optimisation d’un Site E-commerce

## 📌 Contexte  
Ce projet a été réalisé dans le cadre d’un exercice académique visant à analyser les performances d’un site e-commerce et à proposer des solutions d’optimisation.  
En tant que **développeur data**, l’objectif est d’explorer et transformer les données, de produire des visualisations interactives, et de concevoir des tests A/B pour identifier des pistes d’amélioration.  

## 🎯 Objectifs du projet  
- Explorer et analyser les données du site e-commerce.  
- Identifier les tendances, comportements utilisateurs et opportunités d’optimisation.  
- Créer des visualisations et tableaux de bord interactifs avec **Tableau**.  
- Mettre en place des scénarios de tests A/B (simulés).  
- Développer des scripts Python respectant les bonnes pratiques (PEP8, modularité).  
- Fournir une documentation claire et complète.  

## 📂 Structure du projet  

```bash
ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE/
│── ANALYSE/
│   ├── jupyter_notebook/
│   │   └── jupyter.py
│   └── visualisation/        # (Visualisations Tableau à ajouter)
│
│── data/
│   ├── raw/                  # Données brutes
│   ├── loaded/               # Données chargées
│   └── transformed/          # Données transformées
│
│── ETL/
│   ├── extraction/
│   │   └── extract.py
│   ├── transformation/
│   │   └── transform.py
│   └── chargement/
│       └── loaded.py
│
│── LIVRABLE/                 # Rapport, présentation, dashboard final
│
│── requirements.txt          # Dépendances du projet
│── venv/                     # Environnement virtuel Python
│── .gitignore
│── README.md
```

## ⚙️ Installation et utilisation  

### 1. Cloner le dépôt  
```bash
git clone <url-du-depot>
cd ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE
```

### 2. Créer et activer l’environnement virtuel  
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances  
Les dépendances nécessaires sont listées dans le fichier `requirements.txt`.  
Pour les installer :  
```bash
pip install -r requirements.txt
```

#### 📦 Contenu du `requirements.txt` :
```
bleach==6.2.0
certifi==2025.8.3
charset-normalizer==3.4.3
colorama==0.4.6
idna==3.10
kaggle==1.7.4.5
kagglehub==0.3.12
numpy==2.3.2
packaging==25.0
pandas==2.3.1
protobuf==6.32.0
python-dateutil==2.9.0.post0
python-slugify==8.0.4
pytz==2025.2
PyYAML==6.0.2
requests==2.32.4
setuptools==80.9.0
six==1.17.0
text-unidecode==1.3
tqdm==4.67.1
tzdata==2025.2
urllib3==2.5.0
webencodings==0.5.1
```

### 4. Lancer les notebooks  
```bash
jupyter notebook
```

### 5. Visualisations et Dashboard  
- Les visualisations seront créées avec **Tableau** (dossier `ANALYSE/visualisation`).  
- Le tableau de bord final sera livré dans `LIVRABLE/`.  

## 📊 Données  
Les données utilisées proviennent du dataset e-commerce disponible sur Kaggle :  
🔗 [Retail Rocket E-commerce Dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)  

## ✅ Livrables attendus  
- Scripts Python pour ETL et analyse.  
- Tableau de bord interactif (Tableau).  
- Rapport d’analyse et résultats des A/B tests.  
- Présentation finale.  
