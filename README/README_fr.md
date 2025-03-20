<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Système de Gestion Automatisée des Partis 📈

Bienvenue dans le projet **Système de Gestion Automatisée des Partis** ! Notre objectif est de fournir aux utilisateurs de Habitica des outils de gestion des partis efficaces et pratiques. Que vous soyez un leader passionné par la gestion ou un membre désireux de participer activement, vous trouverez ici les outils et la documentation nécessaires ! ✨

## 🚀 Structure du Projet

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # Fichier de workflow GitHub Actions
├── LICENSE                                    # Licence du projet
├── documents                                  # Dossier de documentation du projet
│   ├── brief_description.md                   # Document de description succincte
│   ├── new_members.md                         # Document sur la liste des nouveaux membres
│   ├── party_description.md                   # Document de description du parti
│   ├── remove_PM.md                           # Modèle d'avis pour la suppression de membres
│   └── remove_members.md                      # Modèle d'enregistrement pour la suppression de membres
├── logs                                        # Dossier des journaux
│   ├── manage_members.log                     # Journal de gestion des membres
│   └── update_description.log                 # Journal de mise à jour de la description
├── requirements.txt                           # Fichier de dépendances
└── scripts                                     # Répertoire des scripts
    ├── manage_members.py                      # Script de gestion des membres
    └── update_description.py                  # Script de mise à jour de la description du parti
```

## 📄 Présentation des Fichiers

| Nom du Fichier                            | Description                                                   |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | Fichier de workflow GitHub Actions qui s'exécute toutes les 10 minutes, chargé de la gestion des tâches de l'équipe. En configurant l'environnement Python, en installant les dépendances, et en exécutant les scripts de gestion des membres et de mise à jour de la description, il garantit que votre parti reste toujours actif ! 🎯 |
| **brief_description.md**              | Fournit une citation quotidienne accompagnée de sa traduction, favorisant l'apprentissage des langues et la participation communautaire. Ce document se met automatiquement à jour avec les dernières informations sur les membres, garantissant ainsi la fraîcheur du contenu. 🌱 |
| **new_members.md**                    | Enregistre les invitations des nouveaux membres, mettant en avant la participation active de la communauté. Ce document est mis à jour par des opérations planifiées, vous assurant de ne jamais manquer l'arrivée de nouveaux compagnons ! 👥 |
| **party_description.md**              | Énonce la mission et les règles du parti, encourageant les membres à partager leurs expériences personnelles et à participer activement aux tâches. De plus, le contenu inclut des discussions sur l'existentialisme et le nihilisme, vous aidant à explorer des significations plus profondes dans la vie. 📚 |
| **remove_PM.md**                      | Un modèle d'avis amical, utilisé pour informer les membres qui ont été retirés en raison de leur faible activité, tout en leur offrant la possibilité de revenir, augmentant ainsi la convivialité et l'efficacité de la communication. 🤝 |
| **remove_members.md**                 | Enregistre les raisons de la suppression des membres et les liens associés, garantissant la transparence du processus de gestion, et mis à jour régulièrement pour audit et archives. 🔍 |
| **requirements.txt**                  | Énumère les dépendances Python nécessaires, assurant que votre environnement est configuré de manière cohérente pour une installation facile des bibliothèques requises. ⚙️ |
| **manage_members.py**                 | Script de gestion des membres du parti, incluant la suppression des membres inactifs, l'envoi d'invitations et l'enregistrement des journaux, simplifiant le processus de gestion. ⚡️ |
| **update_description.py**             | Script de mise à jour automatique de la description du parti, garantissant que vous disposez chaque jour de contenu à partager avec les membres et renforçant le sentiment de participation. 🌟 |

## Comment utiliser

1. **Forker ce projet** : Cliquez sur le bouton "**Fork**" en haut à droite.
2. **Configurer le Token API** : Dans les secrets de votre projet cloné, configurez votre token API Habitica et votre ID.
3. **Personnaliser les modèles** : Modifiez les modèles dans le dossier `documents` selon vos besoins, en veillant à ne pas altérer les espaces réservés.
4. **Profitez de la gestion automatisée** : Une fois ces étapes réalisées, vous serez en mesure d'atteindre la gestion automatisée souhaitée ! 🚀

## 🌟 Comment contribuer

Si vous pensez que ce projet vous est utile ou si vous souhaitez y participer, n'hésitez pas à donner ⭐️ à notre projet ! Votre soutien est notre plus grande motivation ! Nous vous attendons avec impatience pour vos suggestions, vos signalements de problèmes ou vos contributions de code. Votre participation est la bienvenue ! 💪

## 📧 Contactez-nous

Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter via les Issues, et nous vous répondrons dans les plus brefs délais ! 😉 

Merci de votre intérêt pour le Système de Gestion Automatisée des Partis, et nous vous souhaitons une excellente utilisation ! 🎉