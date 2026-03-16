<div align="center">
<img src="https://img.shields.io/badge/Python-3.10+-7B68EE?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML-534AB7?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/NLP-TextBlob-1B7F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SHAP-Explicabilité_IA-A0522D?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Complet-success?style=for-the-badge"/>
</div>

<div align="center">
<h1>🛍️ Prédiction du Succès des Produits E-Commerce</h1>
<p><i>Women's Clothing Reviews — Classification Binaire avec Explicabilité IA</i></p>

<br>
<b>👩‍💻 BEN ZHIR Wafa & IKSOD Salma</b><br>
<b>👨‍🏫 Encadré par : AIT BAHA Tarek</b><br>
<b>BSDSI - Année 2025-2026</b>
<br><br>

<p>Prédire si un produit sera recommandé ou non, à partir des avis clients et de leurs caractéristiques — du prétraitement jusqu'à l'explicabilité IA.</p>
</div>

---

## 📌 Table des Matières
- [✨ Points clés du projet](#-points-clés-du-projet)
- [🎯 Problème traité et Dataset](#-problème-traité-et-dataset)
- [📁 Structure du projet](#-structure-du-projet)
- [⚙️ Installation et Exécution](#️-installation-et-exécution)
- [🔬 Pipeline complet](#-pipeline-complet)
- [🤖 Modèles testés et Résultats](#-modèles-testés-et-résultats)
- [🧠 Explicabilité SHAP](#-explicabilité-shap)
- [✅ Conclusion](#-conclusion)

---

## ✨ Points clés du projet

Un pipeline Machine Learning complet et professionnel — de l'exploration des données jusqu'à l'explicabilité IA.

| Étape | Description |
|-------|-------------|
| 🔍 **Exploration** | Analyse approfondie avec visualisations et corrélations |
| 🧹 **Prétraitement** | Gestion des valeurs manquantes, outliers IQR, encodage, normalisation |
| ⚙️ **Feature Engineering NLP** | Polarité, subjectivité et longueur des avis via TextBlob |
| 🤖 **3 modèles ML** | Logistic Regression, Decision Tree, Random Forest |
| ⚖️ **Gestion du déséquilibre** | `stratify=y` + `class_weight='balanced'` |
| 🔁 **Cross-Validation** | cv=3 pour fiabilité et stabilité |
| 🔧 **Optimisation** | GridSearchCV / RandomizedSearchCV |
| 🧠 **Explicabilité SHAP** | Summary Plot, Beeswarm Plot, Waterfall Plot |

---

## 🎯 Problème traité et Dataset

### Le problème

**Objectif :** Prédire si un produit sera recommandé ou non (`Recommended IND`) à partir des avis et caractéristiques des produits.

| Élément | Détail |
|---------|--------|
| **Type de problème** | Classification binaire |
| **Variable cible** | `Recommended IND` |
| **Classe 1** | ✅ Produit recommandé |
| **Classe 0** | ❌ Produit non recommandé |
| **Déséquilibre** | 82% recommandés · 18% non recommandés |

### Le dataset

🔗 **Source :** [Women's E-Commerce Clothing Reviews — Kaggle](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)

23 486 avis clients sur des vêtements vendus sur une plateforme e-commerce.

| Colonne | Type | Description |
|---------|------|-------------|
| `Clothing ID` | Numérique | Identifiant unique du produit |
| `Age` | Numérique | Âge de la cliente |
| `Title` | Texte | Titre de l'avis |
| `Review Text` | Texte | Contenu complet de l'avis |
| `Rating` | Numérique | Note du produit ⭐ (1 à 5) |
| `Recommended IND` | Binaire | ⚡ **Variable cible** (0 ou 1) |
| `Positive Feedback Count` | Numérique | Nombre de feedbacks positifs |
| `Division Name` | Catégorielle | Division du magasin |
| `Department Name` | Catégorielle | Département du produit |
| `Class Name` | Catégorielle | Catégorie spécifique |

---

## 📁 Structure du projet
ecommerce_project/
│
├── 📂 data/
│ └── Womens Clothing E-Commerce Reviews.csv
│
├── 📓 notebook.ipynb # Notebook principal (tout le projet)
│
├── 📄 README.md # Ce fichier
│
└── 📋 requirements.txt # Dépendances Python
## ⚙️ Installation et Exécution

### 1️⃣ Cloner le repository

```bash
git clone https://github.com/votre-username/ecommerce-prediction.git
cd ecommerce-prediction
Lancer le notebook
# Avec VS Code (recommandé)
code .
# → Ouvrir notebook.ipynb
# → Cliquer Run All 

# Ou avec Jupyter
jupyter notebook notebook.ipynb
Important : Adaptez le chemin du fichier CSV dans la cellule de chargement selon votre machine.
Pipeline complet
📥 Chargement des données
        23 486 lignes × 11 colonnes
              ↓
🔍 Exploration & Visualisation
    • Statistiques descriptives
    • Distributions (Age, Rating, Feedback)
    • Nuages de points & corrélations
    • Détection outliers — méthode IQR
              ↓
🧹 Prétraitement
    • Suppression lignes sans Review Text
    • Remplacement NaN : Title → "No Title"
    • Suppression outliers Age & Feedback Count
    • Suppression colonne index inutile
              ↓
⚙️ Feature Engineering NLP — TextBlob
    • review_length  → nombre de mots
    • polarity       → sentiment (-1 négatif → +1 positif)
    • subjectivity   → opinion (0 objectif → 1 subjectif)
              ↓
🔄 Encodage & Normalisation
    • One-Hot Encoding (Division · Department · Class)
    • StandardScaler sur variables numériques
              ↓
✂️ Train / Test Split
    80% entraînement · 20% test · stratify=y
              ↓
🤖 Modélisation — 3 modèles
    • Logistic Regression  (baseline)
    • Decision Tree
    • Random Forest
              ↓
⚖️ class_weight='balanced'
    Test correction du déséquilibre des classes
              ↓
🔁 Cross-Validation cv=3
    Vérification fiabilité et stabilité
              ↓
🔧 Optimisation hyperparamètres
    GridSearchCV (LR · DT) · RandomizedSearchCV (RF)
              ↓
🧠 Explicabilité SHAP
    Summary Plot · Beeswarm Plot · Waterfall Plot
              ↓
✅ Modèle final
    Random Forest optimisé — F1 = 0.9616
    Modèles testés et Résultats
    Résultats initiaux
    
Modèle	Accuracy	Precision	Recall	F1-Score	F1 Classe 0
🔵 Logistic Regression	0.9346	0.9703	0.9498	0.9600	0.82
🟢 Decision Tree	0.9218	0.9552	0.9498	0.9525	0.78 ⚠️
🟠 Random Forest	0.9321	0.9719	0.9451	0.9583	0.82
Cross-Validation (cv=3)
Modèle	F1 Moyen	Écart-type	Verdict
🔵 Logistic Regression	0.9597	0.0005	🥇 Ultra stable
🟠 Random Forest	0.9601	0.0017	🥈 Stable
🟢 Decision Tree	0.9490	0.0012	🥉 Acceptable
Après optimisation GridSearch / RandomizedSearch
Modèle	Meilleurs Paramètres	F1 Avant	F1 Après	Gain
🔵 Logistic Regression	C=10, solver='lbfgs'	0.9600	0.9604	+0.0004
🟢 Decision Tree	criterion='entropy', max_depth=5	0.9525	0.9597	+0.0072 ✅
🟠 Random Forest	n_estimators=100, max_depth=10, max_features='log2'	0.9583	0.9616	+0.0033 
<div align="center">
 Modèle Final : Random Forest Optimisé
✅ F1-Score	✅ Accuracy	✅ F1 Classe 0	✅ F1 CV Moyen
0.9616	0.9375	0.82	0.9609
</div>
Explicabilité SHAP
SHAP (SHapley Additive exPlanations) explique pourquoi le modèle prédit chaque valeur — variable par variable.

Visualisations produites :
📊 Summary Plot (bar) — importance globale de chaque variable

🐝 Beeswarm Plot (dot) — distribution de l'impact sur toutes les prédictions

💧 Waterfall Plot — explication détaillée d'une prédiction individuelle

🔝 Top variables — Scores SHAP
Rang	Variable	Score SHAP	Interprétation
🥇 1	Rating	0.1907	Domine massivement — 6× plus important que le suivant
🥈 2	polarity	0.0309	✅ Feature Engineering NLP validé
🥉 3	subjectivity	0.0090	Contribue légèrement
4	Positive Feedback Count	0.0056	Faible mais réel
5	review_length	0.0048	Faible mais réel
6	Age	0.0047	Quasi nul
7–10	Class · Division · Dept	< 0.003	Négligeable
💡 Insight clé : La corrélation détectée en exploration (Rating = 0.79) est confirmée scientifiquement par SHAP (score = 0.1907). Les features NLP polarity et subjectivity se révèlent utiles — notre Feature Engineering est validé !

✅ Conclusion
Ce projet a permis de construire un pipeline Machine Learning complet pour prédire la recommandation de produits e-commerce avec une accuracy finale de 93.75%.

Points clés à retenir :
📊 Rating = variable dominante confirmée par SHAP (score = 0.1907, corrélation = 0.79)

🧪 Feature Engineering NLP validé — polarity en 2ème position SHAP

🌳 Random Forest optimisé = meilleur modèle final (F1 = 0.9616)

🔁 Cross-validation confirme la fiabilité (écart-type < 0.002)

⚖️ Déséquilibre 82%/18% bien géré grâce à stratify=y

🔧 GridSearchCV améliore significativement le Decision Tree (+0.0072)
Application métier :
Ce modèle permet à une entreprise e-commerce d'anticiper la popularité d'un produit avant même d'analyser manuellement les avis clients.

<div align="center"> <hr>
Mini-projet réalisé dans le cadre du cours de Machine Learning — BSDSI 2025-2026


BEN ZHIR Wafa · IKSOD Salma
Encadré par AIT BAHA Tarek

</div> ```

