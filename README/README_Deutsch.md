- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Projektübersicht 📚

Willkommen beim **Habitica Team-Automatisierungsmanagement-Projekt**! 🎉 Dieses Projekt hat sich zum Ziel gesetzt, das Management der Teammitglieder durch Automatisierungstools und Skripte zu optimieren, um Ihr Erlebnis auf der Habitica-Plattform zu verbessern. Egal, ob Sie Teil des Spiels sind oder einfach Ihr Team bequem verwalten möchten, unsere Tools können Ihnen eine große Hilfe sein!

## Projektstruktur 📂

Hier ist die Struktur des Projekts, damit Sie die benötigten Dateien leicht finden können:

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

## Dateiübersicht 🔍

### Automatisiertes Team-Management (`.github/workflows/automated_party_management.yml`)
Diese Datei definiert einen GitHub Actions-Workflow mit dem Namen „Team-Automatisierungsmanagement“. Er wird alle 10 Minuten automatisch ausgeführt oder kann manuell ausgelöst werden und erfüllt folgende Funktionen:
- Überprüfung des Code-Repositories
- Einrichtung einer Python 3.8-Umgebung
- Installation der erforderlichen Abhängigkeiten (z. B. `requests`)
- Ausführung der Verwaltungsskripte (`manage_members.py` und `update_description.py`) im Austausch mit der Habitica API
- Verzögerung zwischen den Skriptaufrufen, um die API-Rate-Limitierung nicht zu überschreiten
- Einreichung und Push von Protokolländerungen, um die Aktualisierungen des Verwaltungsskripts festzuhalten

### Lizenz (`LICENSE`)
Dieses Projekt folgt der Apache-Lizenz 2.0, um die Open-Source-Zusammenarbeit zu fördern und die Rechte von Schöpfern und Nutzern zu schützen. Die Lizenz beschreibt die Bedingungen für die Nutzung, Kopie und Verteilung der Software und anderer Werke.

### Abhängigkeitsdatei (`requirements.txt`)
Diese Datei listet die externen Bibliotheken und Abhängigkeiten auf, die für das Projekt erforderlich sind. Hier ist nur die „requests“-Bibliothek enthalten, die eine einfache Möglichkeit bietet, HTTP-Anfragen zu senden und Antworten zu verarbeiten.

### Mitgliedsverwaltungsskript (`scripts/manage_members.py`)
Dieses Skript wird zur Verwaltung der Mitglieder auf der Habitica-Plattform verwendet und automatisiert folgende Aufgaben:
- Entfernen inaktiver Mitglieder und Versenden von Benachrichtigungen
- Einladen neuer Benutzer, die dem Team beitreten möchten

### Beschreibung Aktualisierungsskript (`scripts/update_description.py`)
Dieses Skript ist dafür verantwortlich, die Beschreibung des Habitica-Teams zu aktualisieren, indem es den Inhalt dynamisch abrufen und aktualisieren kann. Zu den wichtigen Funktionen gehören:
- Tägliche Inspirationen von einer externen API abrufen
- Automatische Aktualisierung der Team-Beschreibung, um sicherzustellen, dass die Informationen stets aktuell sind!

## Protokolldateien 📜
Alle durchgeführten Aktionen werden in der `logs`-Ordner aufgezeichnet, damit Sie die Ausführungshistorie einsehen und potenzielle Probleme überprüfen können.

## Erste Schritte 🚀

1. Klonen Sie das Projekt-Repository
2. Installieren Sie die Abhängigkeiten: `pip install -r requirements.txt`
3. Nutzen Sie die GitHub Actions-Automatisierungs-Workflows und genießen Sie ein nahtloses Mitgliederverwaltungserlebnis!

## Mitwirken 💡
Wenn Sie zu diesem Projekt beitragen möchten, freuen wir uns über PRs oder Fragen! Lassen Sie uns gemeinsam Habitica noch besser machen! ⭐️

Vielen Dank, dass Sie die README-Datei dieses Projekts gelesen haben! Wir freuen uns auf Ihr Engagement und Ihre Unterstützung, und kommen Sie vorbei und ⭐️ dieses Projekt!