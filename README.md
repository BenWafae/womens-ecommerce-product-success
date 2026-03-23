<div align="center">

<img src="https://img.shields.io/badge/Python-3.13.9-7B68EE?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML-534AB7?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/NLP-TextBlob-1B7F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SHAP-Explicabilité_IA-A0522D?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
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
- Appliquer des méthodes de **clustering non supervisé** pour segmenter les clientes
- Mettre en place une **application Streamlit interactive** pour tester les prédictions en temps réel

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
├── app/
│   └── (ressources de l'application Streamlit)
├── data/
│   └── Womens Clothing E-Commerce Reviews.csv
├── model/
│   ├── models.pkl              ← 3 modèles optimisés (LR, DT, RF)
│   ├── scaler.pkl              ← StandardScaler fitté sur les données
│   ├── feature_columns.pkl     ← Liste des 36 colonnes dans le bon ordre
│   └── scaled_columns.pkl      ← Colonnes numériques à normaliser
├── notebooks/
│   ├── ecommerce_project.ipynb ← Notebook supervisé (EDA + ML + SHAP)
│   └── nonSupervise.ipynb      ← Notebook non supervisé (K-Means, DBSCAN, HC)
├── app.py                      ← Application Streamlit interactive
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
pip install pandas numpy matplotlib seaborn scikit-learn textblob wordcloud shap lime joblib streamlit plotly
```

### Lancer le notebook supervisé

1. Forker le dépôt depuis GitHub
2. Cloner votre fork en local :
```bash
git clone https://github.com/<votre-username>/ecommerce-prediction.git
cd ecommerce-prediction
```
3. Ouvrir `notebooks/ecommerce_project.ipynb` dans VS Code
4. Exécuter chaque cellule avec **Run** (▶) ou `Shift + Enter`

### Lancer le notebook non supervisé

```bash
# Ouvrir dans VS Code
notebooks/nonSupervise.ipynb
```

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
    ↓
Non Supervisé           — K-Means · DBSCAN · Clustering Hiérarchique · PCA
    ↓
Application Streamlit   — Interface interactive de prédiction en temps réel
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

##  Apprentissage Non Supervisé

> En complément du modèle supervisé, nous avons appliqué des techniques de **clustering non supervisé** pour explorer les comportements cachés des clientes — sans variable cible.

### Variables utilisées

```python
X = df[['Age', 'Rating', 'Positive Feedback Count']]
```

Après normalisation avec `StandardScaler` et réduction de dimension avec `PCA (2 composantes)`.

### K-Means — Segmentation en 4 clusters

Le nombre optimal de clusters (K=4) a été déterminé par la **méthode du coude**.

| Cluster | Taille | Âge moyen | Rating moyen | Feedback moyen | Profil |
|---|---|---|---|---|---|
| **Cluster 0** | 8 350 | ~35 ans | ⭐ 4.72 | ~0.5 | 🔵 Satisfaites passives |
| **Cluster 1** | 2 918 | ~43 ans | ⭐ 4.32 | ~4.7 | 🟢 Engagées actives (ambassadrices) |
| **Cluster 2** | 5 399 | ~57 ans | ⭐ 4.63 | ~0.7 | 🟡 Âgées satisfaites |
| **Cluster 3** | 3 732 | ~40 ans | ⭐ 2.32 | ~0.9 | 🔴 Insatisfaites (à surveiller) |

```python
kmeans = KMeans(n_clusters=4, random_state=42)
labels_kmeans = kmeans.fit_predict(X_scaled)
```

### DBSCAN — Détection d'anomalies

```python
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels_dbscan = dbscan.fit_predict(X_scaled)
```

> Identifie automatiquement les **outliers** (label `-1`) : avis incohérents, ratings atypiques.

### Clustering Hiérarchique

```python
hc = AgglomerativeClustering(n_clusters=3)
labels_hc = hc.fit_predict(X_scaled)
```

> Construit une hiérarchie de groupes — utile pour visualiser les relations entre clusters.

### Insights business tirés du clustering

| Action | Cluster ciblé | Objectif |
|---|---|---|
| Programme fidélité / VIP | Cluster 1 (Engagées) | Valoriser les ambassadrices |
| Amélioration produit | Cluster 3 (Insatisfaites) | Réduire le churn |
| Encourager les avis | Cluster 0 & 2 (Passives) | Augmenter l'engagement |

---

##  Application Streamlit — ShopSense AI

> L'application interactive **ShopSense AI** constitue l'aboutissement du projet. Elle permet de tester les prédictions en temps réel, d'explorer les résultats ML et de visualiser les explications SHAP — le tout dans une interface moderne en 8 pages.

### Lancer l'application

```bash
streamlit run app.py
```

### Pages disponibles

| Page | Contenu |
|---|---|
| **01 · Accueil** | Présentation du projet, technologies, dataset |
| **02 · Exploration des Données** | Distributions, corrélations, visualisations EDA |
| **03 · Modélisation ML** | Résultats, cross-validation, optimisation, feature importances |
| **04 · Non Supervisé** | PCA, K-Means, DBSCAN, Clustering Hiérarchique, profils clients |
| **05 · Prédiction** | Interface de prédiction interactive en temps réel |
| **06 · Explication IA** | SHAP global + Waterfall Plot individuel + Beeswarm Plot |
| **07 · Valeur Ajoutée** | Insights business et recommandations stratégiques |
| **08 · Conclusion** | Bilan, limites et perspectives |

### Pipeline de prédiction réelle

Quand l'utilisateur soumet un avis, l'application exécute exactement le même pipeline que le notebook :

```
Texte saisi
    ↓
TextBlob → polarity + subjectivity
    ↓
Reconstruction des 36 colonnes (One-Hot Encoding inclus)
    ↓
StandardScaler (vrai scaler fitté sur les données)
    ↓
Modèle ML (Random Forest / Decision Tree / Logistic Regression)
    ↓
predict() + predict_proba() → résultat + probabilité
```

### Fichiers pkl nécessaires

| Fichier | Contenu |
|---|---|
| `model/models.pkl` | 3 modèles optimisés sauvegardés |
| `model/scaler.pkl` | StandardScaler fitté sur le dataset |
| `model/feature_columns.pkl` | 36 colonnes dans le bon ordre |
| `model/scaled_columns.pkl` | 6 colonnes numériques à normaliser |

> ⚠️ Ces fichiers sont générés en exécutant le bloc de sauvegarde à la fin du notebook `ecommerce_project.ipynb`.

### Exemples de prédiction testés

| Rating | Avis | Feedback | Résultat | Probabilité |
|---|---|---|---|---|
| 3 | "i really found it so bad it was not comfortable at all" | 6 | ❌ Non Recommandé | 37% |
| 4 | "i reelly love it it was impressive so goood so comfortable" | 39 | ✅ Recommandé | 100% |
| 4 | "neutre" | 0 | ✅ Recommandé | 87% |

> Le modèle reflète fidèlement les données réelles : 85.3% des produits avec Rating 4 sont recommandés dans le dataset.

---

##  Limites & pistes d'amélioration

| Limite identifiée | Piste d'amélioration |
|---|---|
| Déséquilibre des classes (82% / 18%) | Appliquer SMOTE ou `class_weight='balanced'` |
| Analyse textuelle basique (TextBlob) | Utiliser un modèle BERT ou TF-IDF avancé |
| Texte en anglais seulement | Extension multilingue avec mBERT ou XLM-RoBERTa |
| Données statiques | Pipeline MLOps avec re-entraînement automatique |
| Déploiement local uniquement | Déploiement cloud AWS / GCP |

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
| `scikit-learn` | Modélisation ML + clustering |
| `textblob` | Analyse de sentiment NLP |
| `wordcloud` | Visualisation textuelle |
| `shap` | Explicabilité IA |
| `joblib` / `pickle` | Sauvegarde des modèles |
| `streamlit` | Application interactive |
| `plotly` | Visualisations interactives dans Streamlit |

---

<div align="center">

*Projet réalisé dans le cadre du cours Systèmes Intelligents — BSDSI 2025-2026*

**BEN ZHIR Wafa · IKSOD Salma · Enc. AIT BAHA Tarek**

</div>