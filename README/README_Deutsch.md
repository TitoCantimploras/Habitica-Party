[Back to main language README](README.md)

# 🎉 Automatisierung des Teammanagementprojekts

Willkommen zu unserem **Automatisierung des Teammanagementprojekts**! 🚀 Dieses Projekt zielt darauf ab, die Teammitglieder auf der Habitica-Plattform mithilfe von Automatisierungsskripten einfach zu verwalten, das Team aktiv zu halten und die Verwaltungseffizienz zu steigern. Lassen Sie uns die Struktur und die Funktionen dieses Projekts näher betrachten!

## 📁 Projektstruktur

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "Automatisierter Teamverwaltungs-Workflow"
    }
  },
  "LICENSE": "Lizenzdatei",
  "README.md": "Projektbeschreibung",
  "README": {
    "README/README_Deutsch.md": "Deutsch Dokumentation",
    "README/README_English.md": "Englische Dokumentation",
    "README/README_Español.md": "Spanische Dokumentation",
    "README/README_Français.md": "Französische Dokumentation",
    "README/README_日本語.md": "Japanische Dokumentation",
    "README/README_繁体中文.md": "Traditionelle Chinesische Dokumentation"
  },
  "documents": {
    "documents/brief_description.md": "Kurze Projektbeschreibung",
    "documents/new_members.md": "Vorstellung neuer Mitglieder",
    "documents/party_description.md": "Team Beschreibung",
    "documents/remove_PM.md": "Entfernung des Projektleiters Anleitung",
    "documents/remove_members.md": "Entfernung von Mitgliedern Anleitung"
  },
  "logs": {
    "logs/manage_members.log": "Mitgliederverwaltungsprotokoll",
    "logs/update_description.log": "Aktualisierungsprotokoll"
  },
  "requirements.txt": "Abhängigkeiten",
  "scripts": {
    "scripts/manage_members.py": "Mitgliederverwaltungs-Skript",
    "scripts/update_description.py": "Aktualisierungs-Skript"
  }
}
```

## 📜 Projektfunktionen

### 1. Automatisierter Teamverwaltungsworkflow 🤖
Wir haben in `.github/workflows/automated_party_management.yml` einen Workflow namens "Automatisierte Teamverwaltung" definiert. Dieser läuft alle 10 Minuten automatisch und kann auch manuell ausgelöst werden. Das Hauptziel dieses Workflows ist es, Informationen über Teammitglieder mithilfe eines Python-Skripts zu verwalten und zu aktualisieren, das folgende wichtige Schritte umfasst:

- **Code-Checkout**: Holen Sie sich den neuesten Code aus dem Repository.
- **Python-Umgebung einrichten**: Installieren Sie Python 3.8.
- **Abhängigkeiten installieren**: Installieren Sie die erforderliche `requests`-Bibliothek.
- **Verwaltungsskript ausführen**: Führen Sie das Skript `manage_members.py` zur Mitgliederverwaltung aus.
- **Anfragenrate begrenzen**: Verwenden Sie Sleep-Befehle, um eine Überlastung der API zu verhindern.
- **Aktualisierungsskript ausführen**: Führen Sie das Skript `update_description.py` zur Aktualisierung der Beschreibung aus.
- **Änderungen protokollieren**: Protokollieren Sie alle Aktionen und übermitteln Sie die Protokolle an das Repository.

### 2. Lizenz 📝
Das Projekt enthält eine `LICENSE`-Datei, die die Bedingungen und Konditionen für die Nutzung, Kopie und Verteilung dieser Software gemäß der Apache License, Version 2.0 festlegt.

### 3. Abhängigkeiten 📦
Die Datei `requirements.txt` im Projekt listet die externen Bibliotheken auf, die für den Betrieb des Projekts benötigt werden. Die benötigte Bibliothek ist `requests`, eine beliebte HTTP-Bibliothek zur Handhabung von Netzwerk-Anfragen und -Antworten.

### 4. Mitgliederverwaltungs-Skript 🧑‍🤝‍🧑
Das Skript `manage_members.py` ist verantwortlich für die Verwaltung der Teammitglieder auf der Habitica-Plattform. Seine Hauptfunktionen umfassen:
- Protokollierung, Festlegung der Anfragefrequenz, Überwachung inaktiver Mitglieder, Versendung von Einladungen usw., um sicherzustellen, dass das Team aktiv bleibt.

### 5. Aktualisierungsskript 🔄
Das Skript `update_description.py` aktualisiert regelmäßig die Teambeschreibung, kombiniert Informationen über Mitglieder und Inhalte von externen APIs, damit Ihre Teambeschreibung immer frisch und ansprechend bleibt.

## 🛠️ So führen Sie es aus
- Stellen Sie sicher, dass Sie eine Python-Umgebung haben und dass die Bibliotheken in `requirements.txt` installiert sind.
- Führen Sie die Skripte `manage_members.py` und `update_description.py` aus, um die Mitgliederverwaltung und die Beschreibung manuell zu betreiben.
- Sie können auch den automatisierten Workflow nutzen, um regelmäßige Aufgaben einzurichten und die Teaminformationen mühelos zu pflegen. 🎈

## 🌐 Mehrsprachige Unterstützung
Das Projekt enthält Dokumentationen in mehreren Sprachen, darunter Chinesisch, Deutsch, Englisch, Spanisch, Französisch und Japanisch, um sicherzustellen, dass jeder Benutzer den Projektinhalt bequem verstehen kann! 🌍

## 📬 Feedback und Unterstützung
Wir freuen uns über Ihre Fragen oder Vorschläge, um dieses Projekt gemeinsam zu verbessern! 🙏

Vielen Dank für Ihre Aufmerksamkeit! Möge Ihr Team auf Habitica voller Energie sein und immer auf dem Erfolgsweg bleiben! 💪✨