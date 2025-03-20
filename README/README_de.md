<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Automatisiertes Parteienmanagementsystem 📈

Willkommen beim **Automatisierten Parteienmanagementsystem** Projekt! Unser Ziel ist es, Habitica-Nutzern effiziente und benutzerfreundliche Werkzeuge für das Parteienmanagement zur Verfügung zu stellen. Egal ob Sie ein leidenschaftlicher Manager sind oder ein aktives Mitglied, hier finden Sie die Werkzeuge und Dokumente, die Sie benötigen!✨

## 🚀 Projektstruktur

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # GitHub Actions Workflow-Datei
├── LICENSE                                    # Projektlizenz
├── documents                                  # Dokumentenordner des Projekts
│   ├── brief_description.md                   # Kurzdokumentation 
│   ├── new_members.md                         # Dokument für neue Mitglieder 
│   ├── party_description.md                   # Parteibeschreibung 
│   ├── remove_PM.md                           # Vorlage für die Benachrichtigung über Mitgliedsentfernung 
│   └── remove_members.md                      # Vorlage für Aufzeichnungen über entfernte Mitglieder 
├── logs                                        # Log-Ordner
│   ├── manage_members.log                     # Protokoll für Mitgliederverwaltung
│   └── update_description.log                 # Protokoll für Beschreibungsaktualisierungen
├── requirements.txt                           # Abhängigkeitsdatei 
└── scripts                                     # Skriptverzeichnis
    ├── manage_members.py                      # Skript zur Verwaltung von Mitgliedern 
    └── update_description.py                  # Skript zur Aktualisierung der Parteibeschreibung 
```

## 📄 Dateibeschreibung

| Dateiname                                 | Beschreibung                                                 |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | GitHub Actions Workflow-Datei, die alle 10 Minuten automatisch läuft und für die Verwaltung von Teamaufgaben zuständig ist. Durch das Einrichten der Python-Umgebung, Installation der Abhängigkeiten und Ausführung von Mitgliedermanagement- und Beschreibungsaktualisierungsskripten bleibt Ihre Partei immer aktiv! 🎯 |
| **brief_description.md**              | Bietet täglich ein Zitat und dessen Übersetzung, um das Sprachenlernen und die Gemeinschaftsaktivitäten zu fördern. Dieses Dokument aktualisiert automatisch die Informationen zu neuen Mitgliedern, um frische Inhalte zu gewährleisten. 🌱 |
| **new_members.md**                    | Dokumentiert die Einladungen neuer Mitglieder und betont die aktive Teilnahme an der Gemeinschaft. Dieses Dokument aktualisiert sich regelmäßig, damit Sie keine neuen Partner verpassen! 👥 |
| **party_description.md**              | Erläutert die Ziele und Regeln der Partei und ermutigt die Mitglieder, persönliche Erfahrungen zu teilen und aktiv an Aufgaben teilzunehmen. Der Inhalt diskutiert auch existenzialistische und nihilistische Themen, die Ihnen helfen, tiefere Bedeutungen im Leben zu erkunden. 📚 |
| **remove_PM.md**                      | Eine freundliche Benachrichtigungsvorlage, um Mitglieder, die aufgrund von Inaktivität entfernt wurden, zu informieren und ihnen die Möglichkeit zur Wiederaufnahme zu geben, um die Kommunikation freundlicher und effizienter zu gestalten. 🤝 |
| **remove_members.md**                 | Dokumentiert die Gründe für die Entfernung von Mitgliedern sowie relevante Links, um den Managementprozess transparent zu gestalten und regelmäßig aktualisiert zu werden für Audits und Aufzeichnungen. 🔍 |
| **requirements.txt**                  | Listet die erforderlichen Python-Abhängigkeiten auf, um sicherzustellen, dass Ihre Umgebung konsistent eingerichtet ist und die benötigten Bibliotheken einfach installiert werden können. ⚙️ |
| **manage_members.py**                 | Skript zur Verwaltung von Parteimitgliedern, einschließlich der Entfernung inaktiver Mitglieder, dem Versenden von Einladungen und Protokollierung, um den Verwaltungsprozess zu vereinfachen. ⚡️ |
| **update_description.py**             | Skript zur automatischen Aktualisierung der Parteibeschreibung, damit Sie täglich aktualisierte Inhalte mit den Mitgliedern teilen können, um das Engagement zu steigern. 🌟 |

## So verwenden Sie es

1. **Forken Sie dieses Projekt**: Klicken Sie auf die Schaltfläche "**Fork**" oben rechts.
2. **Konfigurieren Sie das API-Token**: Richten Sie in den Action-Geheimnissen Ihres geklonten Projekts Ihr Habitica API-Token und Ihre ID ein.
3. **Passen Sie die Vorlagen an**: Ändern Sie nach Bedarf die Vorlagen im `documents`-Ordner, um sicherzustellen, dass die Platzhalter nicht kaputtgehen.
4. **Genießen Sie die automatisierte Verwaltung**: Nach Abschluss der obigen Schritte können Sie die gewünschte automatisierte Verwaltung genießen! 🚀

## 🌟 Wie man beiträgt

Wenn Sie denken, dass dieses Projekt Ihnen hilfreich ist oder Sie daran teilnehmen möchten, freuen wir uns über einen ⭐️ für unser Projekt! Ihre Unterstützung ist unsere größte Motivation! Wir freuen uns auf Ihre Vorschläge, Fehlermeldungen oder Codebeiträge – Ihre Teilnahme ist herzlich willkommen!💪

## 📧 Kontaktieren Sie uns

Wenn Sie Fragen oder Anregungen haben, zögern Sie nicht, uns über Issues zu kontaktieren, wir werden Ihnen so schnell wie möglich antworten!😉

Vielen Dank für Ihr Interesse am Automatisierten Parteienmanagementsystem, und viel Spaß bei der Nutzung!🎉