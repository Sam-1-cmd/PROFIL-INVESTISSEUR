# 📊 Questionnaire de Profil Investisseur

Application Streamlit interactive basée sur le questionnaire de profil investisseur de **L'École de la Bourse d'Abidjan**.

## 🎯 Description

Cette application permet aux utilisateurs de déterminer leur profil d'investisseur à travers un questionnaire complet de 9 questions réparties en 3 parties :

1. **Situation personnelle et financière** (Questions 1-3)
2. **Objectifs de placement et tolérance au risque** (Questions 4-8)
3. **Connaissances et expériences en matière de placement** (Question 9)

## 🚀 Déploiement sur Streamlit Cloud

### Méthode 1 : Déploiement via GitHub (Recommandé)

1. **Créer un dépôt GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/profil-investisseur.git
   git push -u origin main
   ```

2. **Se connecter à Streamlit Cloud**
   - Allez sur [share.streamlit.io](https://share.streamlit.io)
   - Connectez-vous avec votre compte GitHub
   - Cliquez sur "New app"
   - Sélectionnez votre dépôt
   - Le fichier principal est `app.py`
   - Cliquez sur "Deploy"

### Méthode 2 : Déploiement local

1. **Cloner le projet**
   ```bash
   git clone https://github.com/VOTRE_USERNAME/profil-investisseur.git
   cd profil-investisseur
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

## 📁 Structure du projet

```
profil-investisseur/
├── app.py              # Application Streamlit principale
├── requirements.txt    # Dépendances Python
└── README.md          # Documentation
```

## 📋 Profils d'investisseur

| Profil | Score | Revenu fixe | Actions |
|--------|-------|-------------|---------|
| **Prudent** | 0-9 points | 80% | 20% |
| **Modéré** | 10-27 points | 67% | 33% |
| **Équilibré** | 28-44 points | 50% | 50% |
| **Croissance** | 45-62 points | 33% | 67% |
| **Audacieux** | 63-72 points | 20% | 80% |

## ✨ Fonctionnalités

- ✅ Interface utilisateur moderne et responsive
- ✅ Navigation intuitive (Précédent/Suivant)
- ✅ Barre de progression en temps réel
- ✅ Calcul automatique du score
- ✅ Graphique de répartition du portefeuille
- ✅ Recommandations personnalisées
- ✅ Possibilité de recommencer le questionnaire

## 🛠️ Technologies utilisées

- **Streamlit** - Framework web pour applications de data science
- **Plotly** - Bibliothèque de visualisation interactive
- **Python** - Langage de programmation

## 📞 Contact

**L'École de la Bourse d'Abidjan**
- Plateforme d'éducation financière et de formation à l'investissement en bourse
- Version 001 du 03 avril 2016
- KOUAO BRICE ARNAUD

---

*Document confidentiel*
