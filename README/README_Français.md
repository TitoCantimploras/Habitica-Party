[Back to main language README](README.md)

# 🥳 Outil de Gestion d'Équipe Automatisé README

Bienvenue dans notre outil de gestion d'équipe automatisé ! Ce projet vise à améliorer l'efficacité et l'engagement dans la gestion d'équipe grâce à l'intégration avec l'API Habitica. 💼✨

## 📁 Aperçu des Fichiers

### 1. Flux de Travail GitHub Actions
- **Chemin**: `.github/workflows/automated_party_management.yml`
- **Fonction**: Ce flux de travail se déclenche toutes les 10 minutes (peut aussi être exécuté manuellement) et contient les étapes clés suivantes :
  - Vérification du code
  - Configuration de l'environnement Python
  - Installation des dépendances
  - Exécution de scripts de gestion pour traiter les membres de l'équipe sur la plateforme Habitica
  - Exécution de scripts de mise à jour pour enregistrer les modifications
- **Caractéristiques**: Inclut une fonctionnalité de pause pour gérer le taux de requêtes, et soumet finalement tous les journaux de modifications dans le dépôt de code. 🔄

### 2. Licence
- **Nom du Fichier**: `LICENSE`
- **Contenu**: Contient la licence Apache, version 2.0, qui résume les termes et conditions d'utilisation, de reproduction et de distribution des logiciels et œuvres associées, y compris les définitions, les droits des utilisateurs, les exigences de redistribution et les clauses de non-responsabilité. 📜

### 3. Script de Gestion des Membres
- **Nom du Fichier**: `manage_members.py`
- **Fonction**: Ce script Python est conçu pour gérer les membres de l'équipe sur la plateforme Habitica. Ses principales fonctions incluent :
  - **Configuration des Journaux**: Initialiser les journaux pour suivre les opérations du script, y compris les erreurs et les informations générales.
  - **Limite de Taux**: Mettre en œuvre un mécanisme pour respecter les limites des requêtes API, en gérant le temps entre les requêtes.
  - **Gestion des Membres**:
    - Identifier et récupérer les membres de l'équipe inactifs basés sur leur dernière connexion.
    - Envoyer des notifications privées avant de retirer des membres.
    - Envoyer des notifications dans le chat d'équipe pour informer du retrait des membres.
  - **Fonction d'Invitation**: Rechercher les utilisateurs à la recherche d'une équipe et leur envoyer des invitations, y compris une liste formatée des membres invités.
  - **Outils**: Inclut des fonctions utilitaires pour traiter les réponses API, envoyer des messages et calculer le temps en fonction de l'activité des utilisateurs.

En résumé, ce script améliore la gestion d'équipe sur Habitica en automatisant le retrait des utilisateurs inactifs et l'invitation de nouveaux utilisateurs, favorisant ainsi un meilleur engagement des utilisateurs. 🎉

### 4. Script de Mise à Jour de la Description
- **Nom du Fichier**: `update_description.py`
- **Fonction**: Ce script Python est destiné à mettre à jour la description de l'équipe Habitica, et inclut les fonctionnalités suivantes :
  - Récupérer quotidiennement une phrase et les détails de dernière connexion des membres de l'équipe.
  - Journalisation et mise en œuvre de la limite de taux des requêtes API.
  - Mise à jour dynamique de la description de l'équipe en fonction des données récupérées.
  - Lecture du format de description à partir d'un fichier modèle, compilation des informations sur les membres et envoi de la requête de mise à jour à l'API Habitica.
  - Enregistrer les réussites et les erreurs au cours des opérations.

## 🛠️ Installation et Utilisation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. Configurez l'environnement Python :
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez le flux de travail GitHub Actions (si nécessaire) et générez une clé valide dans l'API Habitica.

5. Exécutez les scripts :
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 Contributions

Toutes les contributions sont les bienvenues ! Si vous avez des suggestions ou des questions, merci de soumettre un problème ou de faire une demande de tirage. 😊

## 📞 Contact

Si vous avez des questions ou des retours, n'hésitez pas à me contacter :
- Email : your_email@example.com
- GitHub : [votreNomGitHub](https://github.com/yourusername)

Merci d'utiliser notre outil, et je vous souhaite une gestion d'équipe plus fluide sur Habitica ! 🎊