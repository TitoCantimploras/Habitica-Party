<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Automatisiertes Party-Management-System 📈

Willkommen beim **Automatisierten Party-Management-System** Projekt! Unser Ziel ist es, Habitica-Nutzern effiziente und benutzerfreundliche Party-Management-Tools anzubieten. Egal, ob Sie ein leidenschaftlicher Leiter oder ein engagiertes Mitglied sind, hier finden Sie die Werkzeuge und Dokumente, die Sie benötigen! ✨

## 🚀 Projektstruktur

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # GitHub Actions Workflow-Datei
├── LICENSE                                    # Projektlizenz
├── documents                                  # Projekt-Dokumentenordner
│   ├── brief_description.md                   # Dokument mit kurzer Beschreibung 
│   ├── new_members.md                         # Dokument mit neuer Mitgliederliste 
│   ├── party_description.md                   # Dokument mit Party-Beschreibung 
│   ├── remove_PM.md                           # Benachrichtigungsvorlage für Mitgliedsentfernungen 
│   └── remove_members.md                      # Vorlage für Aufzeichnungen über entfernte Mitglieder 
├── logs                                        # Protokollordner
│   ├── manage_members.log                     # Mitgliederverwaltungsprotokoll
│   └── update_description.log                 # Protokoll für Beschreibungsaktualisierungen
├── requirements.txt                           # Abhängigkeitsdatei 
└── scripts                                     # Skriptverzeichnis
    ├── manage_members.py                      # Skript zur Verwaltung von Mitgliedern 
    └── update_description.py                  # Skript zur Aktualisierung der Party-Beschreibung 
```

## 📄 Dateiübersicht

| Dateiname                                | Beschreibung                                                  |
|------------------------------------------|-------------------------------------------------------------|
| **automated_party_management.yml**       | GitHub Actions Workflow-Datei, die alle 10 Minuten automatisch ausgeführt wird und für das Management von Teamaufgaben verantwortlich ist. Mit Python-Umgebung, Installation von Abhängigkeiten und Ausführung der Skripte zur Mitgliederverwaltung und Beschreibungsaktualisierung sorgt sie dafür, dass Ihre Party immer aktiv bleibt! 🎯 |
| **brief_description.md**                 | Bietet täglich ein Zitat und seine Übersetzung, um das Sprachenlernen und die Gemeinschaftsbeteiligung zu fördern. Dieses Dokument wird auch automatisch mit den neuesten Mitgliederdaten aktualisiert und sorgt für frische Inhalte. 🌱 |
| **new_members.md**                       | Dokumentiert Einladungen neuer Mitglieder und betont die aktive Beteiligung der Gemeinschaft. Dieses Dokument wird regelmäßig aktualisiert, damit Sie keinen neuen Freund verpassen! 👥 |
| **party_description.md**                 | Erläutert die Mission und Regeln der Party, ermutigt Mitglieder, persönliche Erfahrungen zu teilen und aktiv an Aufgaben teilzunehmen. Außerdem diskutiert es existenzialistische und nihilistische Themen, um Ihnen zu helfen, tiefere Bedeutungen im Leben zu erkunden. 📚 |
| **remove_PM.md**                         | Eine freundliche Benachrichtigungsvorlage, um Mitglieder, die aufgrund von Inaktivität entfernt wurden, zu informieren und ihnen eine Möglichkeit zur Wiederbeitrag zu bieten, wodurch die Kommunikation freundlicher und effizienter wird. 🤝 |
| **remove_members.md**                    | Dokumentiert die Gründe für die Entfernung von Mitgliedern und relevante Links, um den Verwaltungsprozess transparent zu gestalten und regelmäßig aktualisiert zu werden, um Audits und Aufzeichnungen zu erleichtern. 🔍 |
| **requirements.txt**                     | Listet die erforderlichen Python-Abhängigkeiten auf, um sicherzustellen, dass Ihre Umgebungsinstallation konsistent und die Installation der erforderlichen Bibliotheken einfach ist. ⚙️ |
| **manage_members.py**                    | Skript zur Verwaltung von Party-Mitgliedern, das Funktionen wie das Entfernen inaktiver Mitglieder, das Versenden von Einladungen und das Führen von Protokollen umfasst und den Verwaltungsprozess vereinfacht. ⚡️ |
| **update_description.py**                | Skript zur automatischen Aktualisierung der Party-Beschreibung, um sicherzustellen, dass Sie täglich aktualisierte Inhalte mit den Mitgliedern teilen können und das Engagement erhöhen. 🌟 |

## Wie man es benutzt

1. **Forken Sie dieses Projekt**: Klicken Sie auf die Schaltfläche „**Fork**“ in der oberen rechten Ecke.
2. **API-Token konfigurieren**: Konfigurieren Sie Ihr Habitica API-Token und Ihre ID in den Actions-Secrets Ihres geklonten Projekts.
3. **Vorlagen anpassen**: Passen Sie die Vorlagen im `documents`-Ordner nach Bedarf an, um sicherzustellen, dass die Platzhalter nicht beschädigt werden.
4. **Genießen Sie die automatisierte Verwaltung**: Nach Abschluss dieser Schritte können Sie die gewünschte automatisierte Verwaltung genießen! 🚀

## 🌟 Wie man beiträgt

Wenn Sie denken, dass dieses Projekt Ihnen hilfreich ist oder Sie daran teilnehmen möchten, freuen wir uns über einen ⭐️ für unser Projekt! Ihre Unterstützung ist unsere größte Motivation! Wir freuen uns auf Anregungen, Problemmeldungen oder Code-Beiträge von Ihnen!💪

## 📧 Kontaktieren Sie uns

Wenn Sie Fragen oder Vorschläge haben, zögern Sie nicht, uns über Issues zu kontaktieren. Wir werden Ihnen so schnell wie möglich antworten! 😉

Danke für Ihr Interesse am automatisierten Party-Management-System. Wir wünschen Ihnen viel Freude bei der Nutzung! 🎉