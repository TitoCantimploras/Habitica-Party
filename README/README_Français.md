- [{main_language}](README.md)- [切換語言: 繁體中文](README/README_繁体中文.md)
- [Switch Language: English](README/README_English.md)
- [Cambiar idioma: Español](README/README_Español.md)
- [Sprache wechseln: Deutsch](README/README_Deutsch.md)
- [言語を切り替える: 日本語](README/README_日本語.md)

# 📚 Introduction au projet README

Bienvenue dans notre projet ! 🎉 Ici, nous nous engageons à gérer les membres de la communauté Habitica grâce à des outils d'automatisation, rendant ainsi la gestion des équipes plus efficace et facile. Découvrons maintenant la structure et les fonctionnalités de ce projet ! ✨

## 📁 Structure du projet

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "automated_party_management.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "documents": {
    "documents/brief_description.md": "brief_description.md",
    "documents/new_members.md": "new_members.md",
    "documents/party_description.md": "party_description.md",
    "documents/remove_PM.md": "remove_PM.md",
    "documents/remove_members.md": "remove_members.md"
  },
  "logs": {
    "logs/manage_members.log": "manage_members.log",
    "logs/update_description.log": "update_description.log"
  },
  "requirements.txt": "requirements.txt",
  "scripts": {
    "scripts/manage_members.py": "manage_members.py",
    "scripts/update_description.py": "update_description.py"
  }
}
```

## 📝 Description des fichiers

### Flux de travail d'automatisation GitHub Actions

Dans le fichier `.github/workflows/automated_party_management.yml`, un flux de travail GitHub Actions est défini pour gérer automatiquement les membres de l'équipe. Il se déclenche toutes les 10 minutes ou peut être appelé manuellement, fonctionne dans un environnement Ubuntu et comprend plusieurs étapes clés :

1. **Vérification du code** : obtention du code du projet.
2. **Configuration de l'environnement Python** : configuration de Python 3.8.
3. **Installation des dépendances** : installation de la bibliothèque `requests` nécessaire.
4. **Exécution du script de gestion** : exécution d'un script Python pour gérer les membres (`manage_members.py`), en utilisant des variables d'environnement pour gérer les identifiants des utilisateurs.
5. **Limitation du taux** : introduction de pauses pour gérer le taux de demandes.
6. **Exécution du script de mise à jour** : exécution du script de mise à jour de la description (`update_description.py`), également en utilisant des variables d'environnement.
7. **Enregistrement des modifications** : soumission des mises à jour de journal générées par le script au dépôt.
8. **Pousse des modifications** : envoi des journaux mis à jour vers le dépôt distant.

Ce flux de travail est conçu pour automatiser efficacement la gestion des membres de l'équipe et la mise à jour des journaux, c'est vraiment un assistant intelligent ! 🤖

### Fichier de licence

Le fichier `LICENSE` est la licence Apache 2.0, qui est une licence open source permissive, définissant les conditions d'utilisation, de reproduction et de distribution du logiciel et des autres œuvres. Elle accorde aux utilisateurs le droit de modifier et de distribuer des œuvres, tout en s'assurant d'une attribution appropriée aux auteurs originaux. Le document comprend également des clauses sur l'utilisation des marques, la limitation des garanties et des responsabilités. Cette documentation vise à faciliter la collaboration entre développeurs et l'utilisation par les utilisateurs, à promouvoir la liberté du logiciel tout en protégeant les droits des auteurs originaux.

### Fichier de dépendances

Le fichier `requirements.txt` liste les paquets et bibliothèques externes nécessaires à l'exécution du projet. Dans ce projet, il ne cite que la bibliothèque `requests`, un module Python très apprécié qui permet aux développeurs d'envoyer facilement des requêtes HTTP, d'interagir avec les services web et les API. Avec la commande simple `pip install -r requirements.txt`, vous pouvez facilement installer ces dépendances et commencer votre voyage magique ! ✨

### Fichiers de script

- **Script de gestion des membres `manage_members.py`**

  Ce script est utilisé pour gérer les membres de l'équipe Habitica, exécutant les principales fonctions suivantes :

  1. **Journalisation** : utilisation du module de journalisation pour enregistrer les opérations et les erreurs, stockées dans des fichiers journaux tournants, et sortie d'informations importantes dans la console.
  2. **Requêtes API à taux limité** : définition d'une fonction d'assistance pour s'assurer que les demandes respectent les intervalles prévus.
  3. **Gestion des utilisateurs** : obtention de la liste des membres de l'équipe, vérification des membres inactifs et leur suppression.
  4. **Envoi de messages** : possibilité d'envoyer des messages privés aux utilisateurs et de publier des invitations ainsi que des messages de retrait dans le chat d'équipe.
  5. **Invitation de nouveaux utilisateurs** : envoi d'invitations aux nouveaux utilisateurs recherchant une équipe et notifications au groupe dans le chat.

  Grâce à ces fonctionnalités, ce script simplifie considérablement la gestion des membres de l'équipe Habitica, rendant la gestion de la communauté beaucoup plus agréable ! 🎈

- **Script de mise à jour de la description `update_description.py`**

  Ce script met automatiquement à jour la description de l'équipe Habitica en intégrant des phrases quotidiennes et des informations sur l'activité des membres. Ses principales fonctions comprennent :

  1. **Requêtes API à taux limité** : gestion de l'intervalle des requêtes pour éviter de surcharger l'API Habitica.
  2. **Récupération de phrases quotidiennes** : obtention de phrases quotidiennes à partir d'une API externe, en récupérant leur contenu en anglais et leur traduction.
  3. **Collecte de données sur les membres** : collecte des informations des membres de l'équipe, y compris leur dernière connexion et durée d'activité dernière.
  4. **Formatage de la description** : lecture d'un modèle Markdown et formatage avec le contenu actuel, les informations des membres et un horodatage.
  5. **Mise à jour de l'interprétation** : envoi de la description mise à jour à l'API Habitica.

  Grâce à cette automatisation, le script améliore continuellement l'attractivité de la description de l'équipe et l'interaction des membres, un véritable ami au style artistique ! 🎨

---

Merci d'avoir consulté notre projet ! Nous espérons que les outils que nous proposons apporteront commodité et plaisir à la gestion de votre communauté Habitica. Si vous avez des questions, n'hésitez pas à nous contacter ! 🎈👋