- [{main_language}](README.md)- [切換語言: 繁體中文](README/README_繁体中文.md)
- [Switch Language: English](README/README_English.md)
- [Cambiar idioma: Español](README/README_Español.md)
- [Changer de langue: Français](README/README_Français.md)
- [言語を切り替える: 日本語](README/README_日本語.md)

# 📚 Projektübersicht README

Willkommen zu unserem Projekt! 🎉 Hier widmen wir uns der effizienten und einfachen Verwaltung der Habitica-Community-Mitglieder durch Automatisierungstools. Lassen Sie uns als Nächstes die Struktur und Funktionen dieses Projekts erkunden! ✨

## 📁 Projektstruktur

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "automated_party_management.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "documents": {
    "documents/brief_description.md": "brief_description.md",
    "documents/new_members.md": "new_members.md",
    "documents/party_description.md": "party_description.md",
    "documents/remove_PM.md": "remove_PM.md",
    "documents/remove_members.md": "remove_members.md"
  },
  "logs": {
    "logs/manage_members.log": "manage_members.log",
    "logs/update_description.log": "update_description.log"
  },
  "requirements.txt": "requirements.txt",
  "scripts": {
    "scripts/manage_members.py": "manage_members.py",
    "scripts/update_description.py": "update_description.py"
  }
}
```

## 📝 Dateibeschreibung

### GitHub Actions Automatisierungs-Workflow

Die Datei `.github/workflows/automated_party_management.yml` definiert einen GitHub Actions-Workflow zur automatischen Verwaltung der Teammitglieder. Er wird alle 10 Minuten oder manuell ausgelöst und läuft in einer Ubuntu-Umgebung mit mehreren entscheidenden Schritten:

1. **Code auschecken**: Das Projekt wird heruntergeladen.
2. **Python-Umgebung einrichten**: Python 3.8 wird konfiguriert.
3. **Abhängigkeiten installieren**: Notwendige `requests` Bibliothek wird installiert.
4. **Verwaltungsskript ausführen**: Das Python-Skript zur Verwaltung der Mitglieder (`manage_members.py`) wird ausgeführt, indem Umgebungsvariablen zur Verwaltung der Benutzeranmeldeinformationen verwendet werden.
5. **Ratenlimitierung**: Eine Pause wird eingefügt, um die Anforderungsrate zu steuern.
6. **Aktualisierungsskript ausführen**: Das Skript zur Aktualisierung der Beschreibung (`update_description.py`) wird ebenfalls unter Verwendung von Umgebungsvariablen ausgeführt.
7. **Änderungen protokollieren**: Die von den Skripten generierten Protokolle werden ins Repository eingepflegt.
8. **Änderungen pushen**: Die aktualisierten Protokolle werden zurück ins Remote-Repository gepusht.

Dieser Workflow zielt darauf ab, die Verwaltung der Teammitglieder und die Aktualisierung der Protokolle effizient zu automatisieren – ein wirklich cleverer Assistent! 🤖

### Lizenzdatei

Die Datei `LICENSE` ist die Apache-Lizenz 2.0, die als eine großzügige Open-Source-Software-Lizenz die Bedingungen für die Nutzung, Vervielfältigung und Verbreitung von Software und anderen Werken festlegt. Sie gewährt den Nutzern das Recht, Werke zu reformieren, zu ändern und zu verbreiten und stellt sicher, dass die ursprünglichen Autoren angemessen gewürdigt werden. Außerdem enthält die Datei Bestimmungen zur Nutzung von Marken, Haftungsausschlüssen und Haftungsbeschränkungen. Dieses Dokument soll die Zusammenarbeit zwischen Entwicklern und die Nutzung durch Benutzer fördern, die Freiheit von Software wahren und die Rechte der ursprünglichen Autoren schützen.

### Abhängigkeitsdatei

Die Datei `requirements.txt` listet die externen Pakete und Bibliotheken auf, die das Projekt benötigt. In diesem Projekt wird nur die `requests` Bibliothek aufgeführt, ein beliebtes Python-Modul, das es Entwicklern ermöglicht, HTTP-Anfragen einfach zu senden und mit Webdiensten und APIs zu interagieren. Mit dem einfachen Befehl `pip install -r requirements.txt` können Sie diese Abhängigkeiten problemlos installieren und sofort Ihre magische Reise beginnen! ✨

### Skriptdateien

- **Mitgliederverwaltungsskript `manage_members.py`**

  Dieses Skript dient der Verwaltung der Mitglieder im Habitica-Team und führt folgende Hauptfunktionen aus:

  1. **Protokollierung**: Verwenden des Logging-Moduls zur Protokollierung von Aktionen und Fehlern, die in rotierenden Protokolldateien gespeichert und wichtige Informationen in der Konsole ausgegeben werden.
  2. **API-Anfragen mit Ratenlimit**: Definierung einer Hilfsfunktion, um sicherzustellen, dass Anfragen in den vorgeschriebenen Abständen erfolgen.
  3. **Benutzerverwaltung**: Abrufen der Liste der Teammitglieder, Überprüfung von inaktiven Mitgliedern und deren Entfernung.
  4. **Nachrichten senden**: Möglichkeit, private Nachrichten an Benutzer zu senden und Einladungs- sowie Entfernungsmeldungen in den Teamchat zu veröffentlichen.
  5. **Einladung neuer Benutzer**: Einladungen an neue Benutzer, die nach einem Team suchen, werden gesendet, und das Team wird im Chat benachrichtigt.

  Mit diesen Funktionen vereinfacht dieses Skript die Verwaltung der Habitica-Teammitglieder erheblich und sorgt dafür, dass das Community-Management leichter und angenehmer wird! 🎈

- **Aktualisierungsskript `update_description.py`**

  Dieses Skript aktualisiert automatisch die Teambeschreibung von Habitica, indem es tägliche Sätze und Mitgliederaktivitätsinformationen integriert. Hauptfunktionen umfassen:

  1. **API-Anfragen mit Ratenlimit**: Verwaltung der Abstände zwischen den Anfragen, um Überlastungen der Habitica API zu verhindern.
  2. **Abfrage von täglichen Sätzen**: Abrufen täglicher Sätze von einer externen API, einschließlich der englischen Inhalte und Übersetzungen.
  3. **Mitgliederdaten sammeln**: Abrufen von Informationen über Teammitglieder, einschließlich letzter Anmeldezeit und Dauer der letzten Aktivität.
  4. **Beschreibung formatieren**: Einlesen einer Markdown-Vorlage und Formatierung in den aktuellen Inhalt, Mitgliederinformationen und Zeitstempel.
  5. **Aktualisierte Beschreibung senden**: Die aktualisierte Beschreibung wird an die Habitica API gesendet.

  Mit solchen Automatisierungsmaßnahmen steigert dieses Skript die Attraktivität der Teambeschreibung und die Interaktion der Mitglieder – es ist wirklich ein künstlerischer Freund! 🎨

---

Vielen Dank, dass Sie sich unser Projekt angesehen haben! Wir hoffen, dass die Tools, die wir bereitstellen, die Verwaltung Ihrer Habitica-Community erleichtern und Ihnen Freude bereiten. Bei Fragen stehen wir Ihnen jederzeit zur Verfügung! 🎈👋