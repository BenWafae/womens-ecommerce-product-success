<div align="center">

<img src="https://img.shields.io/badge/Python-3.13.9-7B68EE?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML-534AB7?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/NLP-TextBlob-1B7F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SHAP-Explicabilité_IA-A0522D?style=for-the-badge"/>
<img src="https://img.shields.io/badge/VS_Code-Notebook-0078D4?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Complet-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/>

#  Prédiction du succès des produits e-commerce

**Mini-projet Machine Learning — Filière BSDSI | Année universitaire 2025-2026**

Réalisé par : **BEN ZHIR Wafa** ([BenWafae](https://github.com/BenWafae)) · **IKSOD Salma** ([salmaIKSOD](https://github.com/salmaIKSOD))  
Encadré par : **AIT BAHA Tarek**

</div>

---

##  Description générale

Ce projet a pour objectif de **prédire si un produit e-commerce sera populaire ou non** à partir du dataset *Women's E-Commerce Clothing Reviews*. Il est conçu comme un **système de prédiction intelligent**, combinant l'exploration des données, le prétraitement, l'entraînement de modèles de machine learning et une interface interactive.

Le projet permet de :

- Analyser les caractéristiques des produits et des avis clients
- Construire un modèle de **classification binaire** : produit recommandé `1` ou non recommandé `0`
- Mettre en place une application interactive pour tester les prédictions

### Pourquoi ce problème ?

Dans le e-commerce, anticiper la popularité d'un produit permet de :

| Cas d'usage | Bénéfice |
|---|---|
| Gestion de stock & logistique | Éviter les ruptures ou le surstockage |
| Campagnes marketing | Cibler les produits à fort potentiel |
| Recommandations clients | Personnaliser l'expérience d'achat |

> Le problème se formalise comme une **classification binaire** : prédire la popularité d'un produit à partir de ses caractéristiques et des avis clients.

---

##  Présentation du projet

Prédire si un produit vestimentaire sera **recommandé ou non** par les clientes, à partir de leurs avis et des caractéristiques du produit.

| Élément | Détail |
|---|---|
| **Dataset** | Women's E-Commerce Clothing Reviews |
| **Source** | [Kaggle — nicapotato](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews) |
| **Taille** | 23 486 avis · 11 colonnes |
| **Type de problème** | Classification binaire |
| **Variable cible** | `Recommended IND` — 1 = recommandé · 0 = non recommandé |

---

## 🗂️ Structure du dépôt

```
ecommerce-prediction/
├── data/
│   └── Womens Clothing E-Commerce Reviews.csv
├── notebooks/
│   └── ecommerce_project.ipynb
├── models/
│   └── (modèles sauvegardés via joblib)
└── README.md
```

---

##  Environnement & exécution

> Aucun environnement virtuel requis. Le projet tourne directement dans **VS Code** avec l'extension **Jupyter**.

### Prérequis

| Outil | Version / Usage |
|---|---|
| Python | 3.13.9 |
| VS Code | Éditeur utilisé |
| Extension Jupyter (VS Code) | Exécution cellule par cellule |

### Installation des dépendances

```bash
pip install pandas numpy matplotlib seaborn scikit-learn textblob wordcloud shap lime joblib
```

### Lancer le notebook

1. Forker le dépôt depuis GitHub
2. Cloner votre fork en local :
```bash
git clone https://github.com/<votre-username>/ecommerce-prediction.git
cd ecommerce-prediction
```
3. Ouvrir `notebooks/ecommerce_project.ipynb` dans VS Code
4. Exécuter chaque cellule avec **Run** (▶) ou `Shift + Enter`

---

## Pipeline du projet

```
Dataset brut
    ↓
Exploration (EDA)       — distributions, corrélations, valeurs manquantes
    ↓
Prétraitement           — nettoyage, outliers IQR, encodage, normalisation
    ↓
Feature Engineering     — longueur avis, polarité, subjectivité (TextBlob)
    ↓
Modélisation            — Logistic Regression · Decision Tree · Random Forest
    ↓
Évaluation              — accuracy, F1, matrice de confusion, cross-validation
    ↓
Optimisation            — GridSearchCV · RandomizedSearchCV
    ↓
Explicabilité           — SHAP (importance globale + prédiction individuelle)
```

---

##  Résultats des modèles

### Avant optimisation

| Modèle | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.9346 | 0.9703 | 0.9498 | 0.9600 |
| Decision Tree | 0.9218 | 0.9552 | 0.9498 | 0.9525 |
| Random Forest | 0.9321 | 0.9719 | 0.9451 | 0.9583 |

### Après optimisation (GridSearchCV / RandomizedSearchCV)

| Modèle | Accuracy | F1-Score | Meilleurs paramètres |
|---|---|---|---|
| Logistic Regression | 0.9353 | 0.9604 | `C=10, solver=lbfgs` |
| Decision Tree | 0.9343 | 0.9597 | `max_depth=5, criterion=entropy` |
| **Random Forest**  | **0.9375** | **0.9616** | `n_estimators=100, max_depth=10` |

### Cross-validation (cv = 3)

| Modèle | F1 moyen | Écart-type |
|---|---|---|
| Logistic Regression | 0.9597 | ±0.0005 |
| Decision Tree | 0.9490 | ±0.0012 |
| Random Forest | 0.9601 | ±0.0017 |

> **Modèle retenu : Random Forest optimisé** — meilleur F1 global (0.9616) et meilleure Accuracy (0.9375).

---

##  Feature Engineering NLP

| Feature créée | Description | Outil |
|---|---|---|
| `review_length` | Nombre de mots dans l'avis | Python `.split()` |
| `polarity` | Sentiment du texte (−1 négatif → +1 positif) | TextBlob |
| `subjectivity` | Opinion vs fait (0 objectif → 1 subjectif) | TextBlob |

> SHAP confirme que `polarity` et `subjectivity` sont les 2ᵉ et 3ᵉ variables les plus influentes après `Rating`.

---

##  Explicabilité — SHAP

> Au-delà de la performance brute, SHAP permet de **comprendre pourquoi** le modèle prédit une recommandation — variable par variable, prédiction par prédiction.

| Rang | Variable | Score SHAP moyen | Interprétation |
|---|---|---|---|
| 1 | `Rating` | 0.1907 | Variable dominante (×6 vs le suivant) |
| 2 | `polarity` | 0.0309 | Feature Engineering utile |
| 3 | `subjectivity` | 0.0090 | Contribution légère |
| 4 | `Positive Feedback Count` | 0.0056 | Faible mais réel |
| 5 | `review_length` | 0.0048 | Faible mais réel |

---

##  Optimisation des hyperparamètres

> Les modèles par défaut ne sont pas toujours optimaux. GridSearchCV et RandomizedSearchCV testent automatiquement plusieurs combinaisons de paramètres pour trouver la meilleure configuration.

| Modèle | Méthode | Paramètres testés |
|---|---|---|
| Logistic Regression | GridSearchCV | `C`, `solver` |
| Decision Tree | GridSearchCV | `max_depth`, `criterion`, `min_samples_split` |
| Random Forest | RandomizedSearchCV | `n_estimators`, `max_depth`, `max_features` |

---

##  Limites & pistes d'amélioration

| Limite identifiée | Piste d'amélioration |
|---|---|
| Déséquilibre des classes (82% / 18%) | Appliquer SMOTE ou `class_weight='balanced'` |
| Analyse textuelle basique (TextBlob) | Utiliser un modèle BERT ou TF-IDF avancé |
| Partie non supervisée absente | Ajouter un clustering k-means par segment client |
| Pas d'interface utilisateur | Développer une mini-app Streamlit ou Gradio |

---

##  Organisation Git

| Branche | Contributrice | Profil |
|---|---|---|
| `main` | Dépôt principal partagé | — |
| `benzhirWafa` | BEN ZHIR Wafa | [github.com/BenWafae](https://github.com/BenWafae) |
| `iksodsalma` | IKSOD Salma | [github.com/salmaIKSOD](https://github.com/salmaIKSOD) |

### Workflow utilisé

Chaque contributrice travaille sur sa branche, puis intègre les modifications via les commandes suivantes :

```bash
# Récupérer les dernières modifications du dépôt distant
git fetch origin

# Intégrer la branche de l'autre contributrice
git merge origin/iksodsalma
# ou
git merge origin/benzhirWafa
```

---

##  Bibliothèques utilisées

| Bibliothèque | Usage |
|---|---|
| `pandas` / `numpy` | Manipulation des données |
| `matplotlib` / `seaborn` | Visualisation |
| `scikit-learn` | Modélisation ML |
| `textblob` | Analyse de sentiment NLP |
| `wordcloud` | Visualisation textuelle |
| `shap` | Explicabilité IA |
| `joblib` | Sauvegarde des modèles |

---

<div align="center">

*Projet réalisé dans le cadre du cours Systèmes Intelligents — BSDSI 2025-2026*

</div>