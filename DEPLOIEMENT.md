# 🚀 Guide de Déploiement Rapide

## Option 1 : Déploiement sur Streamlit Cloud (Gratuit - RECOMMANDÉ)

### Étape 1 : Préparer les fichiers
Vous avez déjà tous les fichiers nécessaires :
- `app.py` - L'application principale
- `requirements.txt` - Les dépendances
- `.streamlit/config.toml` - Configuration

### Étape 2 : Créer un compte GitHub
1. Allez sur [github.com](https://github.com)
2. Créez un compte gratuit si vous n'en avez pas

### Étape 3 : Créer un nouveau dépôt
1. Cliquez sur le bouton vert "+" → "New repository"
2. Nommez-le : `profil-investisseur`
3. Rendez-le public
4. Cliquez sur "Create repository"

### Étape 4 : Uploader les fichiers
**Méthode simple (interface web) :**
1. Sur la page de votre nouveau dépôt, cliquez sur "uploading an existing file"
2. Glissez-déposez TOUS les fichiers (app.py, requirements.txt, et le dossier .streamlit)
3. Cliquez sur "Commit changes"

**Méthode Git (ligne de commande) :**
```bash
cd profil_investisseur
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/profil-investisseur.git
git push -u origin main
```

### Étape 5 : Déployer sur Streamlit Cloud
1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez-vous avec votre compte GitHub
3. Cliquez sur "Create app" ou "New app"
4. Sélectionnez :
   - **Repository** : `VOTRE_USERNAME/profil-investisseur`
   - **Branch** : `main`
   - **Main file path** : `app.py`
5. Cliquez sur "Deploy"

### Étape 6 : Votre site est en ligne ! 🎉
- L'URL sera : `https://votre-nom-de-app.streamlit.app`
- Vous pouvez la partager immédiatement

---

## Option 2 : Déploiement Local

### Prérequis
- Python 3.8 ou supérieur installé

### Installation
```bash
# 1. Naviguer vers le dossier
cd profil_investisseur

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur Mac/Linux:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

---

## 📁 Structure des fichiers

```
profil-investisseur/
├── app.py                  ← Application principale (REQUIS)
├── requirements.txt        ← Dépendances (REQUIS)
├── README.md              ← Documentation
├── DEPLOIEMENT.md         ← Ce fichier
├── .gitignore             ← Fichiers à ignorer par Git
└── .streamlit/
    └── config.toml        ← Configuration Streamlit
```

---

## 🛠️ Personnalisation

### Modifier les couleurs
Éditez le fichier `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#2d5a87"      # Couleur principale
backgroundColor = "#ffffff"    # Fond
secondaryBackgroundColor = "#f0f2f6"  # Fond secondaire
textColor = "#1e3a5f"         # Couleur du texte
```

### Modifier le contenu
Éditez `app.py` pour changer :
- Les questions
- Les profils
- Les descriptions
- Les recommandations

---

## ❓ Dépannage

### Problème : L'application ne se lance pas
**Solution :** Vérifiez que toutes les dépendances sont installées :
```bash
pip install streamlit plotly
```

### Problème : Erreur sur Streamlit Cloud
**Solution :** Vérifiez que `requirements.txt` contient bien :
```
streamlit>=1.28.0
plotly>=5.15.0
```

### Problème : Les modifications ne s'affichent pas
**Solution :** Sur Streamlit Cloud, cliquez sur "Reboot" ou attendez quelques minutes pour le redéploiement automatique.

---

## 📞 Support

Pour toute question ou problème :
1. Consultez la [documentation Streamlit](https://docs.streamlit.io)
2. Vérifiez les logs sur Streamlit Cloud (bouton "Manage app")
3. Testez localement avant de déployer

---

**Bon déploiement ! 🚀**
