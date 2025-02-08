[Back to main language README](README.md)

切换语言: 简体中文
切換語言: 繁體中文
Switch Language: English
Cambiar idioma: Español
Changer de langue: Français
言語を切り替える: 日本語

# Projekt Selbstverwaltungs-System README 🌟

Willkommen zu unserem Projekt Selbstverwaltungs-System! 🎉 Dieses Projekt wurde für das Teammanagement auf der Habitica-Plattform entwickelt. Durch die Automatisierung der Verwaltung von Teammitgliedern und die Aktualisierung der Teambeschreibung wird sichergestellt, dass jedes Team in einem guten Zustand bleibt. 👏

## Projektstruktur 🗂️

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

## Projektdateien Übersicht 📁

### Workflow-Dateien 🔄
- **Automatisierter Verwaltungsworkflow**: Diese Datei befindet sich in `.github/workflows/automated_party_management.yml`, sie verwaltet das Team regelmäßig über GitHub Actions. Alle 10 Minuten wird sie ausgeführt, um sicherzustellen, dass der Teamstatus immer aktuell bleibt! 💼

### Lizenz 📜
- **LICENSE**: Dieses Projekt verwendet die Apache-Lizenz 2.0, die die Bedingungen für die Nutzung, Vervielfältigung und Verbreitung von Software und anderen Arbeiten detailliert festlegt, damit jeder gut informiert ist! ✨

### Abhängigkeitsdatei 📦
- **requirements.txt**: Diese Datei listet die erforderlichen Bibliotheken für das Projekt auf, wobei nur eine wichtige Bibliothek enthalten ist: `requests`, die uns hilft, HTTP-Anfragen einfach zu senden und den Code zu vereinfachen! 🚀

### Skriptdateien 🖥️
- **Mitgliederverwaltungsskript (manage_members.py)**: Dieses Skript überwacht den Aktivitätsstatus der Mitglieder, entfernt inaktive Mitglieder automatisch und lädt neue Mitglieder ein. So bleibt unser Team immer voller Energie! 💪

- **Beschreibung aktualisieren Skript (update_description.py)**: Die Aufgabe dieses Skripts ist es, die Beschreibung des Teams zu aktualisieren, einschließlich motivierender Sprüche, Mitgliedsinformationen, aktueller Zeit usw., damit unser Team immer voller positiver Energie ist! 🌈

## Beitragsrichtlinien 🤝

Wir freuen uns über jeden, der Interesse an diesem Projekt hat, um seinen Beitrag zu leisten! Bitte stellen Sie sicher, dass Sie unsere Lizenz befolgen und freundlich mit anderen Mitwirkenden kommunizieren. 🌍

## Bedienungsanleitung 🛠️

1. **Projekt klonen**: Verwenden Sie den folgenden Befehl, um das Projekt lokal zu klonen:
   ```bash
   git clone https://github.com/dein-repo-url.git
   ```

2. **Abhängigkeiten installieren**: Installieren Sie die erforderlichen Python-Bibliotheken mit pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **GitHub Secrets einrichten**: Konfigurieren Sie die erforderlichen Benutzer-ID und API-Schlüssel für das Verwaltungsskript, um sicherzustellen, dass Sie Zugriff auf die Habitica API haben.

4. **Workflow starten**: Manuell den Workflow auslösen oder alle 10 Minuten auf die automatische Ausführung warten und genießen Sie den Spaß an der automatisierten Verwaltung! 🥳

## Protokollierung 📊

Im `logs` Ordner finden Sie die Protokolldateien, die während der Verwaltung des Teams und der Aktualisierung der Beschreibung generiert werden. Diese helfen uns, jeden Vorgang nachzuvollziehen! 🪄

## Kontaktieren Sie uns 📧

Wenn Sie während der Nutzung des Projekts auf Probleme stoßen oder Vorschläge machen möchten, zögern Sie nicht, uns per E-Mail zu kontaktieren! 😊

Vielen Dank für Ihr Interesse an unserem Projekt! Lassen Sie uns gemeinsam ein aktiveres und effizienteres Team aufbauen! 🎊

---

Wir hoffen, diese Einführung weckt Ihr Interesse am Projekt. Kommen Sie und erleben Sie den Spaß an der automatisierten Verwaltung! 🚀✨