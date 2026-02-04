# 📁 Liste des fichiers du projet

## Fichiers principaux

| Fichier | Description | Obligatoire |
|---------|-------------|-------------|
| `app.py` | Application Streamlit complète avec les 9 questions et les 5 profils | ✅ OUI |
| `requirements.txt` | Liste des dépendances Python (streamlit, plotly) | ✅ OUI |
| `.streamlit/config.toml` | Configuration du thème et du serveur | ✅ OUI |

## Fichiers de documentation

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation complète du projet |
| `DEPLOIEMENT.md` | Guide de déploiement détaillé étape par étape |
| `FICHIERS.md` | Ce fichier - liste des fichiers |
| `.gitignore` | Fichiers à ignorer par Git |

## Fonctionnalités de l'application

### ✅ Questions interactives (9 questions)
1. **Âge** - 5 options (0-8 points)
2. **Retraite** - 5 options (0-8 points)
3. **Revenus mensuels** - 5 options (0-8 points)
4. **Objectif de placement** - 5 options (0-8 points)
5. **Horizon d'investissement** - 5 options (0-8 points)
6. **Réaction à une baisse de 25%** - 4 options (0-8 points)
7. **Temps de récupération** - 5 options (0-8 points)
8. **Choix de placement** - 5 options avec tableau (0-8 points)
9. **Connaissances** - 5 options (0-8 points)

### ✅ Profils d'investisseur (5 profils)
| Profil | Score | Revenu fixe | Actions |
|--------|-------|-------------|---------|
| **PRUDENT** | 0-9 | 80% | 20% |
| **MODÉRÉ** | 10-27 | 67% | 33% |
| **ÉQUILIBRÉ** | 28-44 | 50% | 50% |
| **CROISSANCE** | 45-62 | 33% | 67% |
| **AUDACIEUX** | 63-72 | 20% | 80% |

### ✅ Fonctionnalités
- Navigation Précédent/Suivant
- Barre de progression
- Calcul automatique du score
- Graphique de répartition (camembert)
- Progress bars visuelles
- Design responsive et moderne
- Possibilité de recommencer

## Déploiement rapide

### Sur Streamlit Cloud (Gratuit)
1. Créez un compte GitHub
2. Uploadez ces fichiers dans un nouveau dépôt
3. Connectez-vous sur [share.streamlit.io](https://share.streamlit.io)
4. Déployez votre application

### En local
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

**Créé par :** L'École de la Bourse d'Abidjan  
**Version :** 001 du 03 avril 2016  
**Auteur :** KOUAO BRICE ARNAUD
