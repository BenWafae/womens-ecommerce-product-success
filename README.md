<div align="center">
<img src="https://img.shields.io/badge/Python-3.10+-7B68EE?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML-534AB7?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/NLP-TextBlob-1B7F3E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SHAP-Explicabilité_IA-A0522D?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Complet-success?style=for-the-badge"/>
<br/><br/>
🛍️ Prédiction du Succès des Produits E-Commerce
Women's Clothing Reviews — Classification Binaire avec Explicabilité IA
<br/>
👩‍💻 BEN ZHIR Wafa👩‍💻 IKSOD Salma👨‍🏫 Encadré par : AIT BAHA TarekBSDSIBSDSIAnnée 2025-2026
<br/>
Prédire si un produit sera recommandé ou non, à partir des avis clients et de leurs caractéristiques — du prétraitement jusqu'à l'explicabilité IA.
<br/>
</div>

📌 Table des Matières

✨ Points clés du projet
🎯 Problème traité et Dataset
📁 Structure du projet
⚙️ Installation et Exécution
🔬 Pipeline complet
🤖 Modèles testés et Résultats
🧠 Explicabilité SHAP
✅ Conclusion


✨ Points clés du projet

Un pipeline Machine Learning complet et professionnel — de l'exploration des données jusqu'à l'explicabilité IA.

<br/>
🔍   Exploration approfondie des données avec visualisations et corrélations
🧹   Prétraitement rigoureux — valeurs manquantes, outliers IQR, encodage, normalisation
⚙️   Feature Engineering NLP — polarité, subjectivité et longueur des avis via TextBlob
🤖   3 modèles ML comparés — Logistic Regression, Decision Tree, Random Forest
⚖️   Gestion du déséquilibre — stratify=y + class_weight='balanced'
🔁   Cross-Validation cv=3 — fiabilité et stabilité confirmées
🔧   Optimisation GridSearchCV / RandomizedSearchCV — hyperparamètres affinés
🧠   Explicabilité SHAP — Summary Plot, Beeswarm Plot, Waterfall Plot
<br/>

🎯 Problème traité et Dataset
Le problème

Objectif : Prédire si un produit sera recommandé ou non (Recommended IND) à partir des avis et caractéristiques des produits.

<br/>
ÉlémentDétailType de problèmeClassification binaireVariable cibleRecommended INDClasse 1✅ Produit recommandéClasse 0❌ Produit non recommandéDéséquilibre82% recommandés · 18% non recommandés
<br/>
Le dataset

🔗 Source : Women's E-Commerce Clothing Reviews — Kaggle

23 486 avis clients sur des vêtements vendus sur une plateforme e-commerce.
<br/>
ColonneTypeDescriptionClothing IDNumériqueIdentifiant unique du produitAgeNumériqueÂge de la clienteTitleTexteTitre de l'avisReview TextTexteContenu complet de l'avisRatingNumériqueNote du produit ⭐ (1 à 5)Recommended INDBinaire⚡ Variable cible (0 ou 1)Positive Feedback CountNumériqueNombre de feedbacks positifsDivision NameCatégorielleDivision du magasinDepartment NameCatégorielleDépartement du produitClass NameCatégorielleCatégorie spécifique
<br/>

📁 Structure du projet
ecommerce_project/
│
├── 📂 data/
│   └── Womens Clothing E-Commerce Reviews.csv
│
├── 📓 notebook.ipynb       ← Notebook principal (tout le projet)
│
├── 📄 README.md            ← Ce fichier
│
└── 📋 requirements.txt     ← Dépendances Python

⚙️ Installation et Exécution
1️⃣ Cloner le repository
bashgit clone https://github.com/votre-username/ecommerce-prediction.git
cd ecommerce-prediction
<br/>
2️⃣ Créer un environnement virtuel
bash# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
<br/>
3️⃣ Installer les dépendances
bashpip install -r requirements.txt
Contenu de requirements.txt :
pandas
numpy
matplotlib
seaborn
scikit-learn
textblob
wordcloud
shap
lime
scipy
joblib
<br/>
4️⃣ Lancer le notebook
bash# Avec VS Code (recommandé)
code .
# → Ouvrir notebook.ipynb
# → Cliquer Run All ▶️

# Ou avec Jupyter
jupyter notebook notebook.ipynb

⚠️ Important : Adaptez le chemin du fichier CSV dans la cellule de chargement selon votre machine.

<br/>

🔬 Pipeline complet
📥  Chargement des données
         23 486 lignes × 11 colonnes
              ↓
🔍  Exploration & Visualisation
         • Statistiques descriptives
         • Distributions (Age, Rating, Feedback)
         • Nuages de points & corrélations
         • Détection outliers — méthode IQR
              ↓
🧹  Prétraitement
         • Suppression lignes sans Review Text
         • Remplacement NaN : Title → "No Title"
         • Suppression outliers Age & Feedback Count
         • Suppression colonne index inutile
              ↓
⚙️  Feature Engineering NLP — TextBlob
         • review_length  → nombre de mots
         • polarity       → sentiment (-1 négatif → +1 positif)
         • subjectivity   → opinion (0 objectif → 1 subjectif)
              ↓
🔄  Encodage & Normalisation
         • One-Hot Encoding (Division · Department · Class)
         • StandardScaler sur variables numériques
              ↓
✂️  Train / Test Split
         80% entraînement · 20% test · stratify=y
              ↓
🤖  Modélisation — 3 modèles
         • Logistic Regression  (baseline)
         • Decision Tree
         • Random Forest
              ↓
⚖️  class_weight='balanced'
         Test correction du déséquilibre des classes
              ↓
🔁  Cross-Validation cv=3
         Vérification fiabilité et stabilité
              ↓
🔧  Optimisation hyperparamètres
         GridSearchCV (LR · DT) · RandomizedSearchCV (RF)
              ↓
🧠  Explicabilité SHAP
         Summary Plot · Beeswarm Plot · Waterfall Plot
              ↓
✅  Modèle final
         Random Forest optimisé — F1 = 0.9616

🤖 Modèles testés et Résultats
📊 Résultats initiaux
ModèleAccuracyPrecisionRecallF1-ScoreF1 Classe 0🔵 Logistic Regression0.93460.97030.94980.96000.82🟢 Decision Tree0.92180.95520.94980.95250.78 ⚠️🟠 Random Forest0.93210.97190.94510.95830.82
<br/>
🔁 Cross-Validation (cv=3)
ModèleF1 MoyenÉcart-typeVerdict🔵 Logistic Regression0.95970.0005🥇 Ultra stable🟠 Random Forest0.96010.0017🥈 Stable🟢 Decision Tree0.94900.0012🥉 Acceptable
<br/>
🔧 Après optimisation GridSearch / RandomizedSearch
ModèleMeilleurs ParamètresF1 AvantF1 AprèsGain🔵 Logistic RegressionC=10, solver='lbfgs'0.96000.9604+0.0004🟢 Decision Treecriterion='entropy', max_depth=50.95250.9597+0.0072 ✅🟠 Random Forestn_estimators=100, max_depth=10, max_features='log2'0.95830.9616+0.0033 🏆
<br/>
<div align="center">
🏆 Modèle Final : Random Forest Optimisé
✅ F1-Score✅ Accuracy✅ F1 Classe 0✅ F1 CV Moyen0.96160.93750.820.9609
</div>
<br/>

🧠 Explicabilité SHAP

SHAP (SHapley Additive exPlanations) explique pourquoi le modèle prédit chaque valeur — variable par variable.

<br/>
3 visualisations produites :
📊   Summary Plot (bar) — importance globale de chaque variable
🐝   Beeswarm Plot (dot) — distribution de l'impact sur toutes les prédictions
💧   Waterfall Plot — explication détaillée d'une prédiction individuelle
<br/>
🔝 Top variables — Scores SHAP
RangVariableScore SHAPInterprétation🥇 1Rating0.1907Domine massivement — 6× plus important que le suivant🥈 2polarity0.0309Feature Engineering NLP validé ✅🥉 3subjectivity0.0090Contribue légèrement4Positive Feedback Count0.0056Faible mais réel5review_length0.0048Faible mais réel6Age0.0047Quasi nul7–10Class · Division · Dept< 0.003Négligeable
<br/>

💡 Insight clé : La corrélation détectée en exploration (Rating = 0.79) est confirmée scientifiquement par SHAP (score = 0.1907). Les features NLP polarity et subjectivity se révèlent utiles — notre Feature Engineering est validé !

<br/>

✅ Conclusion

Ce projet a permis de construire un pipeline Machine Learning complet pour prédire la recommandation de produits e-commerce avec une accuracy finale de 93.75%.

<br/>
📊   Rating = variable dominante confirmée par SHAP (score = 0.1907, corrélation = 0.79)
🧪   Feature Engineering NLP validé — polarity en 2ème position SHAP
🌳   Random Forest optimisé = meilleur modèle final (F1 = 0.9616)
🔁   Cross-validation confirme la fiabilité (écart-type < 0.002)
⚖️   Déséquilibre 82%/18% bien géré grâce à stratify=y
🔧   GridSearchCV améliore significativement le Decision Tree (+0.0072)
<br/>

🏪 Application métier : ce modèle permet à une entreprise e-commerce d'anticiper la popularité d'un produit avant même d'analyser manuellement les avis clients.

<br/>

<div align="center">
Mini-projet réalisé dans le cadre du cours de Machine Learning — BSDSI 2025-2026
<br/>
BEN ZHIR Wafa   ·   IKSOD Salma   ·   Encadré par AIT BAHA Tarek
<br/>
⭐ N'hésitez pas à laisser une étoile si ce projet vous a été utile !
</div>