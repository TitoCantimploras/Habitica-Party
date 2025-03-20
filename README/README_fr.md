<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Système de gestion de Party automatisé 📈

Bienvenue dans le projet **Système de gestion de Party automatisé** ! Notre objectif est de fournir aux utilisateurs de Habitica des outils de gestion de Party efficaces et pratiques. Que vous soyez un leader passionné par la gestion ou un membre souhaitant participer activement, vous trouverez ici tous les outils et documents nécessaires ! ✨

## 🚀 Structure du projet

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # Fichier de workflow GitHub Actions
├── LICENSE                                    # Licence du projet
├── documents                                  # Dossier de documentation du projet
│   ├── brief_description.md                   # Document de brève description
│   ├── new_members.md                         # Document sur la liste des nouveaux membres
│   ├── party_description.md                   # Document de description de la Party
│   ├── remove_PM.md                           # Modèle de notification de suppression de membre
│   └── remove_members.md                      # Modèle d'enregistrement des membres supprimés
├── logs                                        # Dossier des journaux
│   ├── manage_members.log                     # Journal de gestion des membres
│   └── update_description.log                 # Journal de mise à jour de description
├── requirements.txt                           # Fichier des dépendances
└── scripts                                     # Dossier de scripts
    ├── manage_members.py                      # Script de gestion des membres
    └── update_description.py                  # Script de mise à jour de la description de la Party
```

## 📄 Introduction aux fichiers

| Nom de fichier                             | Description                                                     |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | Fichier de workflow GitHub Actions exécuté automatiquement toutes les 10 minutes, responsable de la gestion des tâches de l'équipe. En configurant l'environnement Python, en installant des dépendances et en exécutant des scripts de gestion des membres et de mise à jour de la description, ce fichier garantit que votre Party reste toujours active ! 🎯 |
| **brief_description.md**              | Fournit une citation quotidienne et sa traduction, favorisant l'apprentissage linguistique et la participation communautaire. Ce document sera également mis à jour automatiquement avec les informations des nouveaux membres, garantissant la fraîcheur du contenu. 🌱 |
| **new_members.md**                    | Enregistre les invitations de nouveaux membres, soulignant la participation active de la communauté. Ce document est mis à jour par un processus programmé, vous assurant de ne manquer aucun nouveau partenaire ! 👥 |
| **party_description.md**              | Expose la mission et les règles de la Party, encourageant les membres à partager leurs expériences personnelles et à participer activement aux tâches. De plus, le contenu comprend des discussions sur l'existentialisme et le nihilisme, vous aidant à explorer des significations plus profondes dans la vie. 📚 |
| **remove_PM.md**                      | Un modèle de notification amical pour informer les membres supprimés en raison d'une inactivité, tout en offrant la possibilité de récupérer leur place, renforçant la convivialité et l'efficacité de la communication. 🤝 |
| **remove_members.md**                 | Enregistre les raisons de la suppression des membres et les liens associés, garantissant la transparence du processus de gestion, et est mis à jour régulièrement pour l'audit et l'enregistrement. 🔍 |
| **requirements.txt**                  | Liste les dépendances Python nécessaires, garantissant que votre environnement est configuré de manière cohérente pour une installation facile des bibliothèques requises. ⚙️ |
| **manage_members.py**                 | Script pour gérer les membres de la Party, comprenant des fonctionnalités comme la suppression des membres inactifs, l'envoi d'invitations et l'enregistrement des journaux, simplifiant ainsi le processus de gestion. ⚡️ |
| **update_description.py**             | Script pour mettre à jour automatiquement la description de la Party, garantissant que vous avez toujours du contenu à partager avec les membres, renforçant ainsi le sentiment d'appartenance. 🌟 |

## Comment utiliser

1. **Forkez ce projet** : Cliquez sur le bouton "**Fork**" en haut à droite.
2. **Configurez le token API** : Configurez votre token API Habitica et votre ID dans les secrets des Actions de votre projet cloné.
3. **Personnalisez les modèles** : Modifiez les modèles dans le dossier `documents` selon vos besoins, en veillant à ne pas altérer les espaces réservés.
4. **Profitez de la gestion automatisée** : Une fois les étapes ci-dessus terminées, vous pourrez bénéficier de la gestion automatisée souhaitée ! 🚀

## 🌟 Comment contribuer

Si vous pensez que ce projet vous est utile, ou si vous souhaitez y participer, n'hésitez pas à donner une ⭐️ à notre projet ! Votre soutien est notre plus grande motivation ! Nous attendons vos suggestions, vos signalements de problèmes ou vos contributions de code avec impatience ! 💪

## 📧 Contactez-nous

Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter via les Issues, et nous vous répondrons dans les plus brefs délais ! 😉

Merci de votre intérêt pour le Système de gestion de Party automatisé, et nous vous souhaitons une bonne utilisation ! 🎉