[Back to main language README](README.md)

# 🎉 Projet de gestion d'équipe automatisée

Bienvenue dans notre **projet de gestion d'équipe automatisée**! 🚀 Ce projet vise à gérer facilement les membres de l'équipe sur la plateforme Habitica grâce à des scripts d'automatisation, maintenant ainsi l'activité de l'équipe et améliorant l'efficacité de la gestion. Jetons un coup d'œil à la structure et aux fonctionnalités de ce projet !

## 📁 Structure du projet

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "Flux de travail de gestion d'équipe automatisé"
    }
  },
  "LICENSE": "Fichier de licence",
  "README.md": "Documentation du projet",
  "README": {
    "README/README_Deutsch.md": "Documentation en allemand",
    "README/README_English.md": "Documentation en anglais",
    "README/README_Español.md": "Documentation en espagnol",
    "README/README_Français.md": "Documentation en français",
    "README/README_日本語.md": "Documentation en japonais",
    "README/README_繁体中文.md": "Documentation en chinois traditionnel"
  },
  "documents": {
    "documents/brief_description.md": "Brève description du projet",
    "documents/new_members.md": "Présentation des nouveaux membres",
    "documents/party_description.md": "Description de l'équipe",
    "documents/remove_PM.md": "Instructions pour supprimer un chef de projet",
    "documents/remove_members.md": "Instructions pour supprimer des membres"
  },
  "logs": {
    "logs/manage_members.log": "Journal de gestion des membres",
    "logs/update_description.log": "Journal de mise à jour de la description"
  },
  "requirements.txt": "Exigences des paquets dépendants",
  "scripts": {
    "scripts/manage_members.py": "Script de gestion des membres",
    "scripts/update_description.py": "Script de mise à jour de la description"
  }
}
```

## 📜 Fonctionnalités du projet

### 1. Flux de travail de gestion d'équipe automatisé 🤖
Nous avons défini un flux de travail nommé "Gestion automatisée d'équipe" dans le fichier `.github/workflows/automated_party_management.yml`. Il s'exécute automatiquement toutes les 10 minutes et peut également être déclenché manuellement. L'objectif principal de ce flux est de gérer et de mettre à jour les informations des membres de l'équipe via un script Python, comprenant les étapes importantes suivantes :

- **Récupération du code** : obtenir le dernier code du dépôt.
- **Configuration de l'environnement Python** : installation de Python 3.8.
- **Installation des dépendances** : installer la bibliothèque `requests` requise par le script.
- **Exécution du script de gestion** : exécuter le script `manage_members.py` pour la gestion des membres.
- **Limitation de la fréquence des requêtes** : utiliser des commandes de sommeil pour éviter de surcharger l'API.
- **Exécution du script de mise à jour** : exécuter le script `update_description.py` pour mettre à jour la description.
- **Journaliser les modifications** : enregistrer toutes les actions et soumettre les journaux dans le dépôt.

### 2. Licence 📝
Le projet contient un fichier `LICENSE` qui utilise la licence Apache Version 2.0, vous offrant les termes et conditions pour utiliser, copier et distribuer ce logiciel.

### 3. Dépendances 📦
Le fichier `requirements.txt` du projet énumère les bibliothèques externes nécessaires à l'exécution du projet, la principale étant `requests`, une bibliothèque HTTP populaire pour gérer les requêtes et les réponses réseau.

### 4. Script de gestion des membres 🧑‍🤝‍🧑
Le script `manage_members.py` est responsable de la gestion des membres de l'équipe sur la plateforme Habitica. Ses principales fonctionnalités incluent :
- Journalisation, définition de la fréquence des requêtes, détection des membres inactifs, envoi d'invitations, etc., garantissant que l'équipe reste active et ne soit pas laissée pour compte.

### 5. Script de mise à jour de la description 🔄
Le script `update_description.py` met à jour la description de l'équipe à intervalles réguliers, intégrant des informations sur les membres et des contenus provenant d'API externes pour que la description de votre équipe soit toujours fraîche et attrayante.

## 🛠️ Comment exécuter
- Assurez-vous d'avoir un environnement Python et d'installer les bibliothèques requises dans `requirements.txt`.
- Exécutez manuellement les scripts `manage_members.py` et `update_description.py` pour la gestion des membres et la mise à jour des descriptions.
- Vous pouvez également compter sur le flux de travail automatisé pour programmer des tâches et maintenir facilement les informations de l'équipe. 🎈

## 🌐 Support multilingue
Le projet est accompagné de documents d'explication en plusieurs langues, y compris le chinois, l'allemand, l'anglais, l'espagnol, le français et le japonais, garantissant que chaque utilisateur puisse facilement comprendre le contenu du projet ! 🌍

## 📬 Retour d'information et soutien
N'hésitez pas à nous soumettre vos questions ou suggestions, travaillons ensemble pour améliorer ce projet ! 🙏

Merci d'avoir lu ! Que votre équipe sur Habitica soit pleine de vitalité et toujours sur le chemin du succès ! 💪✨