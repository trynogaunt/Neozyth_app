# NeoZyth App - Votre Gestionnaire d'Univers RP

Bienvenue dans **NeoZyth App**, une application conçue pour vous aider à organiser et gérer vos univers de jeu de rôle (RP). Que vous soyez maître de jeu ou joueur, NeoZyth App vous permet de garder une trace de vos personnages, lieux, quêtes et bien plus encore, le tout dans une interface simple et intuitive.

---

## 🎯 **Fonctionnalités Principales**

- **Gestion des Personnages** : Créez et gérez des fiches de personnages avec des informations détaillées.
- **Organisation des Lieux** : Ajoutez des lieux, décrivez-les et connectez-les entre eux.
- **Suivi des Quêtes** : Gardez une trace des quêtes en cours, terminées ou à venir.
- **Interface Intuitive** : Une interface graphique facile à utiliser pour naviguer entre les différentes sections.
- **Sauvegarde Automatique** : Toutes vos données sont stockées localement dans une base de données sécurisée.

---

## 🚀 **Comment Utiliser NeoZyth App**

### 1. **Lancer l'Application**
   - Double-cliquez sur le fichier de lancement ou exécutez la commande suivante dans votre terminal :
     ```bash
     python3 src/app.py
     ```

### 2. **Naviguer dans l'Interface**
   - **Menu Principal** : Accédez aux différentes sections (Personnages, Lieux, Quêtes).
   - **Ajouter des Éléments** : Cliquez sur "Ajouter" pour créer un nouveau personnage, lieu ou quête.
   - **Modifier ou Supprimer** : Sélectionnez un élément existant pour le modifier ou le supprimer.

### 3. **Sauvegarder vos Données**
   - Vos données sont automatiquement sauvegardées dans une base de données locale. Pas besoin de sauvegarder manuellement !

---

## 🛠️ **Configuration Requise**

- **Système d'exploitation** : Windows, macOS ou Linux (avec Python 3.8 ou supérieur).
- **Dépendances** :
  - Python 3
  - Tkinter (installé par défaut sur la plupart des systèmes)
  - SQLite (intégré à Python)

---

## ❓ **FAQ**

### **1. Où sont stockées mes données ?**
Vos données sont stockées localement dans un fichier de base de données SQLite. Vous pouvez le trouver dans le dossier `src/datas/neozyth.db`.

### **2. Puis-je partager mes données avec d'autres ?**
Oui, vous pouvez partager le fichier `neozyth.db` avec d'autres utilisateurs. Ils pourront l'importer dans leur application.

### **3. Que faire si l'application ne se lance pas ?**
- Assurez-vous que Python 3 est installé sur votre système.
- Vérifiez que toutes les dépendances sont installées en exécutant :
  ```bash
  pip install -r requirements.txt
  ```

- Si le problème persiste, contactez le support

### **4. Puis-je transférer mes données sur un autre appareil ?**
Oui, il suffit de copier le fichier `neozyth.db` situé dans le dossier `src/datas/` vers le nouvel appareil. Assurez-vous que l'application est installée sur cet appareil.

## 📬 **Support**
Si vous avez des questions ou des problèmes, n'hésitez pas à ouvrir une issue sur le projet GitHub

[Consultez le projet sur GitHub](https://github.com/votre-utilisateur/neozyth-app)

## 🔮 À venir
- Ajout de captures d'écran pour illustrer l'interface utilisateur.
- Fonctionnalité de recherche avancée pour les personnages et les lieux.
- Exportation des données au format JSON ou CSV.
- Création de fiche personnage à exporter en PDF

## 🤝 Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez signaler un problème ou proposer une amélioration, ouvrez une issue ou soumettez une pull request sur le dépôt GitHub.