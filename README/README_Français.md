- [简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Introduction au Projet 📚

Bienvenue dans le **projet d’automatisation de gestion des équipes Habitica** ! 🎉 Ce projet vise à optimiser la gestion des membres de l’équipe grâce à des outils et des scripts automatiques, afin d'améliorer votre expérience sur la plateforme Habitica. Que vous fassiez partie du jeu ou que vous souhaitiez simplement faciliter la gestion de votre équipe, nos outils sont là pour vous aider !

## Structure du Projet 📂

Voici la structure du projet, pour garantir que vous puissiez facilement trouver les fichiers nécessaires :

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml
├── LICENSE
├── README.md
├── README
│   ├── README_Deutsch.md
│   ├── README_English.md
│   ├── README_Español.md
│   ├── README_Français.md
│   ├── README_日本語.md
│   └── README_繁体中文.md
├── documents
│   ├── brief_description.md
│   ├── new_members.md
│   ├── party_description.md
│   ├── remove_PM.md
│   └── remove_members.md
├── logs
│   ├── manage_members.log
│   └── update_description.log
├── requirements.txt
└── scripts
    ├── manage_members.py
    └── update_description.py
```

## Description des Fichiers 🔍

### Gestion Automatisée des Équipes (`.github/workflows/automated_party_management.yml`)
Ce fichier définit un flux de travail GitHub Actions nommé "Gestion automatisée des équipes". Il s'exécute automatiquement toutes les 10 minutes ou peut être déclenché manuellement, et réalise les fonctions suivantes :
- Récupère le dépôt de code
- Configure l'environnement Python 3.8
- Installe les bibliothèques nécessaires (comme `requests`)
- Exécute les scripts de gestion (`manage_members.py` et `update_description.py`), interagissant avec l'API Habitica
- Met en place des délais entre les exécutions des scripts pour éviter de dépasser les limites de taux de l'API
- Soumet et pousse les modifications des journaux pour enregistrer les mises à jour des scripts de gestion

### Licence (`LICENSE`)
Ce projet est soumis à la licence Apache 2.0, visant à promouvoir la collaboration open source et à protéger les droits des créateurs et des utilisateurs. La licence détaille les termes et conditions d'utilisation, de reproduction et de distribution du logiciel et d'autres œuvres.

### Fichier de Dépendances (`requirements.txt`)
Ce fichier liste les bibliothèques externes et les dépendances nécessaires au projet, se limitant uniquement à la bibliothèque "requests", qui facilite l'envoi de requêtes HTTP et le traitement des réponses.

### Script de Gestion des Membres (`scripts/manage_members.py`)
Ce script est utilisé pour gérer les membres sur la plateforme Habitica, automatisant les tâches suivantes :
- Suppression des membres inactifs et envoi de notifications
- Invitation de nouveaux utilisateurs souhaitant rejoindre l'équipe

### Script de Mise à Jour de la Description (`scripts/update_description.py`)
Ce script est responsable de la mise à jour de la description de l'équipe Habitica, récupérant dynamiquement le contenu et réalisant les mises à jour. Ses fonctionnalités clés incluent :
- Obtenir quotidiennement des phrases d'inspiration d'une API externe
- Mettre à jour automatiquement la description de l'équipe, garantissant une information toujours fraîche !

## Fichiers de Journal 📜
Tous les logs des opérations exécutées sont enregistrés dans le dossier `logs`, facilitant la consultation de l'historique des exécutions et le diagnostic des problèmes potentiels.

## Commencer à Utiliser 🚀

1. Clonez le dépôt du projet
2. Installez les dépendances : `pip install -r requirements.txt`
3. Profitez de l'expérience de gestion des membres sans couture grâce à GitHub Actions !

## Contribuer 💡
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre des PR ou à poser des questions ! Ensemble, rendons Habitica encore plus génial ! ⭐️

Merci d'avoir lu le fichier README de ce projet ! Nous attendons votre participation et votre soutien avec impatience, alors n'hésitez pas à ⭐️ ce projet !