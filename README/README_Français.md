[Back to main language README](README.md)

切换语言: 简体中文
切換語言: 繁體中文
Switch Language: English
Cambiar idioma: Español
Sprache wechseln: Deutsch
言語を切り替える: 日本語

# Système de Gestion de Projets README 🌟

Bienvenue dans notre système de gestion de projets ! 🎉 Ce projet est conçu pour la gestion d'équipe sur la plateforme Habitica, automatisant la gestion des membres de l'équipe et la mise à jour de la description de l'équipe pour garantir que chaque équipe fonctionne en bonne condition. 👏

## Structure du Projet 🗂️

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

## Présentation des Fichiers du Projet 📁

### Fichiers de Workflow 🔄
- **Workflow de gestion automatisée** : Ce fichier se trouve dans `.github/workflows/automated_party_management.yml`, il gère régulièrement l'équipe via GitHub Actions. Il s'exécute toutes les 10 minutes, garantissant que l'état de l'équipe reste toujours à jour ! 💼

### Licence 📜
- **LICENSE** : Ce projet est sous la licence Apache 2.0, qui précise en détail les conditions d'utilisation, de reproduction et de distribution des logiciels et autres œuvres, afin que tout le monde soit clairement informé ! ✨

### Fichiers de Dépendances 📦
- **requirements.txt** : Ce fichier liste les bibliothèques nécessaires au projet, contenant seulement une bibliothèque essentielle : `requests`, qui nous aide à envoyer facilement des requêtes HTTP et simplifie l'écriture de code ! 🚀

### Fichiers de Scripts 🖥️
- **Script de gestion des membres (manage_members.py)** : Ce script est responsable de la surveillance de l'activité des membres, de l'élimination automatique des membres inactifs, de l'invitation de nouveaux membres, etc., garantissant que nos coéquipiers restent toujours dynamiques ! 💪

- **Script de mise à jour de description (update_description.py)** : La tâche de ce script est de mettre à jour la description de l'équipe, incluant des citations motivantes, des informations sur les membres, l'heure actuelle, etc., pour que notre équipe soit toujours pleine d'énergie positive ! 🌈

## Guide de Contribution 🤝

Nous accueillons toute personne intéressée par ce projet pour apporter sa contribution ! Veuillez vous assurer de respecter notre licence et d'interagir amicalement avec les autres contributeurs. 🌍

## Instructions d'Utilisation 🛠️

1. **Cloner le projet** : Utilisez la commande suivante pour cloner le projet sur votre machine locale :
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **Installer les dépendances** : Utilisez pip pour installer les bibliothèques Python nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les Secrets GitHub** : Configurez les ID d'utilisateur et les clés API nécessaires pour le script de gestion, afin de garantir votre accès à l'API Habitica.

4. **Démarrer le Workflow** : Déclenchez le workflow manuellement ou attendez son exécution automatique toutes les 10 minutes, et profitez de la gestion automatisée ! 🥳

## Journalisation 📊

Dans le dossier `logs`, vous pouvez trouver les fichiers journaux générés au cours de la gestion de l'équipe et de la mise à jour de la description, qui nous aident à suivre chaque opération ! 🪄

## Contactez-Nous 📧

Si vous rencontrez des problèmes en utilisant le projet, ou si vous souhaitez faire des suggestions, n'hésitez pas à nous contacter par e-mail ! 😊

Merci de votre intérêt et de votre utilisation du projet ! Ensemble, construisons une équipe plus active et efficace ! 🎊

---

Nous espérons que cette introduction vous passionnera pour le projet, alors venez vite découvrir le plaisir de la gestion automatisée ! 🚀✨