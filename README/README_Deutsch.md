[Back to main language README](README.md)

# 🥳 Automatisierungstool für Teammanagement README

Willkommen bei unserem Automatisierungstool für das Teammanagement! Dieses Projekt zielt darauf ab, die Effizienz und das Engagement im Teammanagement durch die Integration der Habitica API zu steigern.💼✨

## 📁 Dateibeschreibung

### 1. GitHub Actions Workflow
- **Pfad**: `.github/workflows/automated_party_management.yml`
- **Funktion**: Dieser Workflow wird alle 10 Minuten ausgelöst (kann auch manuell ausgeführt werden) und umfasst folgende wichtige Schritte:
  - Code auschecken
  - Python-Umgebung einrichten
  - Abhängigkeiten installieren
  - Verwaltungsskript ausführen, um die Teammitglieder auf der Habitica-Plattform zu verwalten
  - Aktualisierungsskript ausführen, um Änderungen zu protokollieren
- **Merkmale**: Enthält eine Pause-Funktion zur Verwaltung der Anforderungsrate und überträgt schließlich alle Protokolländerungen in das Repository.🔄

### 2. Lizenzvereinbarung
- **Dateiname**: `LICENSE`
- **Inhalt**: Der Inhalt umfasst die Apache-Lizenz, Version 2.0, die die Bedingungen für die Nutzung, Vervielfältigung und Verteilung der Software sowie verwandter Werke umreißt, einschließlich Definitionen, Benutzerrechte, Anforderungen für die Weiterverteilung und Haftungsausschlüsse.📜

### 3. Mitgliedermanagement-Skript
- **Dateiname**: `manage_members.py`
- **Funktion**: Dieses Python-Skript dient der Verwaltung von Teammitgliedern auf der Habitica-Plattform. Die Hauptfunktionen umfassen:
  - **Protokollierung**: Initialisiert Protokolle zur Verfolgung der Skriptaktivitäten, einschließlich Fehlern und allgemeinen Informationen.
  - **Ratenbegrenzung**: Implementiert Mechanismen zur Einhaltung der API-Anforderungsgrenzen, indem die Anforderungszeit gesteuert wird.
  - **Mitgliedermanagement**:
    - Ermittelt und ruft inaktive Teammitglieder basierend auf der letzten Anmeldedatum ab.
    - Sendet private Benachrichtigungen vor der Entfernung von Mitgliedern.
    - Sendet Benachrichtigungen über die Entfernung von Mitgliedern im Team-Chat.
  - **Einladungsfunktion**: Sucht nach Benutzern, die ein Team suchen, und sendet ihnen Einladungen, einschließlich einer formatierten Nachricht mit einer Liste der eingeladenen Mitglieder.
  - **Hilfsfunktionen**: Enthält Hilfsfunktionen zur Verarbeitung von API-Antworten, zum Senden von Nachrichten und zur Berechnung von Zeit basierend auf der Benutzeraktivität.

Zusammenfassend verbessert dieses Skript das Teammanagement in Habitica, indem es die Entfernung inaktiver Benutzer und die Einladung neuer Benutzer automatisiert, was zu besserer Benutzerbeteiligung führt.🎉

### 4. Aktualisierungsskript für Beschreibungen
- **Dateiname**: `update_description.py`
- **Funktion**: Dieses Python-Skript dient der Aktualisierung der Beschreibung von Habitica-Teams. Zu den Funktionen gehören:
  - Tägliche Abruf von Informationen über das Team und die letzten Anmeldedetails der Mitglieder.
  - Protokollierung und Implementierung von Ratenbegrenzung für die API-Anfragen.
  - Dynamische Aktualisierung der Teambeschreibung basierend auf den abgerufenen Daten.
  - Lesen des Beschreibungsformats aus einer Template-Datei, Kompilieren von Mitgliederinformationen und Senden von Aktualisierungsanfragen an die Habitica-API.
  - Protokollierung von Erfolgen und Fehlern während des Vorgangs.

## 🛠️ Installation und Verwendung

1. Klonen Sie dieses Repository:
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. Python-Umgebung einrichten:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. Konfigurieren Sie den GitHub Actions-Workflow (falls erforderlich) und generieren Sie einen gültigen Schlüssel in der Habitica API.

5. Skripte ausführen:
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 Beitrag

Beiträge in jeglicher Form sind willkommen! Bei Vorschlägen oder Fragen reichen Sie bitte ein Issue ein oder erstellen Sie einen Pull Request.😊

## 📞 Kontakt

Wenn Sie Fragen oder Feedback haben, kontaktieren Sie mich bitte über die folgenden Kanäle:
- E-Mail: your_email@example.com
- GitHub: [IhrGitHubBenutzername](https://github.com/yourusername)

Vielen Dank, dass Sie unser Werkzeug verwenden, und viel Erfolg bei der Teamverwaltung in Habitica!🎊