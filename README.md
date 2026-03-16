Prédiction du succès des produits e-commerce

Pipeline ML complet de classification binaire sur les avis clients — du prétraitement NLP jusqu'à l'explicabilité SHAP.

Show Image Show Image Show Image Show Image
BSDSI · 2025–2026 | BEN ZHIR Wafa & IKSOD Salma | Encadré par AIT BAHA Tarek

Problème traité
Prédire si un produit sera recommandé ou non (Recommended IND) à partir des avis et caractéristiques clients.
ÉlémentDétailTypeClassification binaireVariable cibleRecommended IND (0 ou 1)Déséquilibre82% recommandés · 18% non recommandésDatasetWomen's E-Commerce Clothing Reviews — KaggleTaille23 486 avis · 11 colonnes

Structure du projet
ecommerce_project/
├── data/
│   └── Womens Clothing E-Commerce Reviews.csv
├── notebook.ipynb       # Notebook principal — tout le projet
├── requirements.txt     # Dépendances Python
└── README.md

Utilisation
Ouvrir le notebook
bash# Avec VS Code (recommandé)
code notebook.ipynb
# → Run All
Dépendances
Les bibliothèques standard (pandas, numpy, scikit-learn, matplotlib, seaborn) sont incluses dans toute installation Anaconda. Seules trois librairies supplémentaires sont nécessaires — elles sont déjà installées via des cellules dans le notebook :
python!pip install textblob wordcloud shap

Aucun environnement virtuel requis. Aucune configuration supplémentaire.

Adapter le chemin du CSV
Dans la cellule de chargement, ajustez le chemin selon votre machine :
pythondf = pd.read_csv("data/Womens Clothing E-Commerce Reviews.csv")

Pipeline complet
01 · Exploration & visualisation
     Statistiques descriptives, distributions, nuages de points,
     matrice de corrélation, détection outliers (méthode IQR)
     ↓
02 · Prétraitement
     Suppression lignes sans Review Text
     NaN Title → "No Title"
     Suppression outliers Age & Positive Feedback Count
     Suppression colonne index inutile
     ↓
03 · Feature Engineering NLP (TextBlob)
     review_length  → nombre de mots
     polarity       → sentiment (-1 négatif → +1 positif)
     subjectivity   → opinion (0 objectif → 1 subjectif)
     ↓
04 · Encodage & normalisation
     One-Hot Encoding (Division · Department · Class Name)
     StandardScaler sur variables numériques
     ↓
05 · Train / Test split
     80% entraînement · 20% test · stratify=y
     ↓
06 · Modélisation — 3 modèles
     Logistic Regression (baseline)
     Decision Tree
     Random Forest
     + class_weight='balanced' + Cross-validation cv=3
     ↓
07 · Optimisation hyperparamètres
     GridSearchCV (LR · DT) · RandomizedSearchCV (RF)
     ↓
08 · Explicabilité SHAP
     Summary Plot · Beeswarm Plot · Waterfall Plot · Top-10 variables

Résultats
Après optimisation
ModèleAccuracyF1F1 Classe 0F1 CV (cv=3)Logistic Regression0.93530.96040.820.9597 ±0.0005Decision Tree0.93430.9597—0.9490 ±0.0012Random Forest ★0.93750.96160.820.9609 ±0.0017
★ Modèle final : Random Forest optimisé — n_estimators=100, max_depth=10, max_features='log2'
Top variables SHAP
RangVariableScore SHAPNote1Rating0.19076× plus important que le suivant2polarity0.0309Feature Engineering NLP validé3subjectivity0.0090Contribution légère4Positive Feedback Count0.0056—5review_length0.0048—

Branches Git
bash# Initialiser le repo
git init && git add . && git commit -m "initial commit"

# Créer les branches de chaque collaboratrice
git branch benzhirWafa
git branch iksodsalma

# Travailler sur sa branche
git checkout benzhirWafa     # ou iksodsalma
git push origin benzhirWafa  # pousser vers GitHub
Chaque membre travaille sur sa propre branche, puis fusionne vers main via une pull request.

Conclusion
Ce projet construit un pipeline ML complet atteignant une accuracy de 93.75% sur la prédiction de recommandation produit.

Rating est la variable dominante (SHAP = 0.1907, corrélation = 0.79)
Le Feature Engineering NLP (polarity) est validé en 2e position SHAP
La cross-validation confirme la fiabilité du modèle (écart-type < 0.002)
Le déséquilibre 82/18 est bien géré grâce à stratify=y


Mini-projet réalisé dans le cadre du cours de Machine Learning — BSDSI 2025–2026
BEN ZHIR Wafa · IKSOD Salma · Encadré par AIT BAHA Tarek
