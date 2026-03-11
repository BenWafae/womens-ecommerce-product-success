# Prédiction du succès d’un produit e-commerce

## Description générale
Ce projet a pour objectif de prédire si un produit e-commerce sera populaire ou non à partir du dataset **Women's E-Commerce Clothing Reviews**.  
Le projet est conçu comme un **système de prédiction intelligent**, combinant l’exploration des données, le prétraitement, l’entraînement de modèles de machine learning et une interface interactive avec **Streamlit**.

Le projet permet de :  
- Analyser les caractéristiques des produits et des avis clients  
- Construire un modèle de classification binaire : produit populaire (1) ou produit faible (0)  
- Mettre en place une application interactive pour tester les prédictions  

---

## Problème traité
Dans le e-commerce, savoir à l’avance si un produit va être populaire permet de :  
- Optimiser le stock et la logistique  
- Cibler les campagnes marketing  
- Proposer des recommandations personnalisées aux clients  

Le problème se formalise comme une **classification binaire**, où l’objectif est de prédire la popularité d’un produit à partir de ses caractéristiques et des avis clients.

---

## Dataset utilisé
- **Nom :** Women's E-Commerce Clothing Reviews  
- **Source :** [Kaggle](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)  
- **Taille :** 23 486 lignes, 10 colonnes  
- **Colonnes principales :**  
  - `Clothing ID` : identifiant du produit  
  - `Age` : âge du client  
  - `Rating` : note du produit (1–5)  
  - `Review Text` : texte du commentaire  
  - `Recommended IND` : indicateur si le produit est recommandé (target)  
  - `Positive Feedback Count` : nombre de feedbacks positifs  
  - `Division Name`, `Department Name`, `Class Name` : catégories du produit  

Ce dataset est **réel et exploitable pour un projet étudiant**, avec des colonnes numériques, catégorielles et textuelles, permettant de tester différentes techniques de machine learning et de NLP.

---

## Structure actuelle du projet
- `data/` → contient le dataset CSV  
- `notebook/` → notebook unique pour l’exploration, le prétraitement et la modélisation (sera rempli progressivement)  
- `app/` → dossier pour l’application Streamlit (vide pour l’instant)  

---

## Objectifs futurs du projet
- Prétraitement des données et création de nouvelles features (ex : longueur de l’avis, sentiment)  
- Entraînement de modèles de classification (Logistic Regression, Decision Tree, Random Forest)  
- Évaluation des modèles avec des métriques adaptées (accuracy, precision, recall, F1)  
- Mise en place d’une interface interactive Streamlit pour tester les prédictions  
- Ajout de fonctionnalités intelligentes : explication des prédictions via SHAP ou LIME  

---

## Remarques
Ce README présente uniquement la **vision globale du projet** et sera mis à jour au fur et à mesure de l’avancement avec :  
- les résultats des modèles  
- les hyperparamètres optimaux  
- les métriques détaillées et les analyses  
