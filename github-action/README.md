Orchestrated GitHub Actions pipeline task within established learning formatOrchestrated GitHub Actions pipeline task within established learning formatGut. Das neue Konzept heute ist CI/CD mit GitHub Actions – dein Health-Checker läuft dann automatisch bei jedem Push, und der Exit-Code entscheidet ob die Pipeline durchläuft oder fehlschlägt. Ich erkläre es ausführlich, weil es komplett neu ist.
Was eine Pipeline überhaupt ist
GitHub Actions ist ein Automatisierungssystem das direkt in GitHub eingebaut ist. Du legst eine Konfigurationsdatei in deinem Repo ab, die beschreibt: "Wenn dieses Ereignis passiert (z.B. ein Push), dann führe diese Schritte aus." GitHub startet dann automatisch einen frischen Linux-Rechner in der Cloud, holt deinen Code, und führt deine Schritte aus. Wenn ein Schritt mit Exit-Code ungleich 0 endet, gilt die Pipeline als fehlgeschlagen und wird rot markiert.
Das ist der Moment wo dein --strict-Flag plötzlich Sinn ergibt. Dein Health-Checker beendet sich mit sys.exit(1) wenn zu viele Services ungesund sind. In einer Pipeline bedeutet das: Die Pipeline schlägt fehl. Genau so funktioniert echtes Monitoring in CI/CD.
Die Aufgabe
Du baust eine GitHub-Actions-Pipeline für deinen Health-Checker. Die Pipeline soll bei jedem Push den Generator laufen lassen, dann den Checker im Strict-Modus, und fehlschlagen wenn zu viele Services ungesund sind.
Schritt 1 – Ordnerstruktur anlegen
GitHub Actions erwartet seine Konfigurationsdateien an einem festen Ort: im Ordner .github/workflows/ im Wurzelverzeichnis deines Repos. Lege diese Struktur an. Der Punkt am Anfang von .github ist wichtig – es ist ein versteckter Ordner.
dein-repo/
├── .github/
│   └── workflows/
│       └── health-check.yml
├── config.py
├── generator.py
└── checker.py
Schritt 2 – Die Workflow-Datei verstehen und schreiben
Erstelle die Datei .github/workflows/health-check.yml. YAML ist das Format das du schon von docker-compose kennst – Einrückung mit Leerzeichen ist bedeutungstragend, keine Tabs.
Hier das Grundgerüst, das du verstehen und anpassen sollst:
yamlname: Health Check

on:
  push:
    branches:
      - main

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - name: Code auschecken
        uses: actions/checkout@v4

      - name: Python einrichten
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Services generieren
        run: python generator.py

      - name: Health Check ausführen
        run: python checker.py --strict
Schritt 3 – Jede Zeile verstehen
Geh die Datei durch und mach dir klar was jeder Block tut:
name ist der Anzeigename der Pipeline in der GitHub-Oberfläche.
on definiert wann die Pipeline läuft. Hier bei jedem Push auf den main-Branch. Es gibt auch andere Auslöser – pull_request, zeitgesteuert mit schedule, oder manuell.
jobs enthält die Aufgaben. Ein Job läuft auf einem eigenen frischen Rechner.
runs-on: ubuntu-latest sagt GitHub, einen frischen Ubuntu-Rechner zu starten. Genau das Linux das du kennst.
steps sind die einzelnen Schritte nacheinander. uses greift auf fertige Action-Bausteine zurück (Code auschecken, Python installieren), run führt einen Shell-Befehl aus – genau die Befehle die du lokal auch tippst.
Schritt 4 – Die Pipeline testen
Committe und pushe die Datei zu GitHub:
bashgit add .github/workflows/health-check.yml
git commit -m "Add health check pipeline"
git push origin main
Geh dann auf GitHub in dein Repo, klick oben auf den Tab "Actions". Dort siehst du deine Pipeline laufen – live, Schritt für Schritt. Wenn der Generator zufällig viele ungesunde Services erzeugt, schlägt checker.py --strict mit Exit-Code 1 fehl, und die Pipeline wird rot. Wenn nicht, wird sie grün.
Schritt 5 – Den Effekt beobachten
Lass die Pipeline ein paar Mal laufen (jeder Push triggert sie neu, oder du nutzt im Actions-Tab "Re-run jobs"). Weil dein Generator zufällige Status-Codes erzeugt, wird die Pipeline mal grün, mal rot sein – je nachdem wie viele Services ungesund sind. Das demonstriert genau wozu Pipelines da sind: Sie fangen Probleme automatisch ab, ohne dass jemand manuell prüfen muss.
Worauf ich beim Review achten werde
Ob die YAML-Einrückung sauber ist (häufigster Fehler bei Anfängern). Ob du verstehst warum die Schritte in dieser Reihenfolge stehen (erst Code holen, dann Python, dann erst deine Scripts). Und ob dir auffällt, dass dein requirements.txt hier eventuell noch installiert werden müsste, falls dein Checker externe Packages braucht – schau dir an ob deine drei Dateien (config, generator, checker) überhaupt externe Imports haben oder nur die Standardbibliothek.
Wenn die Pipeline läuft, hast du zum ersten Mal etwas das echte DevOps-Engineers täglich bauen: eine automatisierte Pipeline die bei jeder Änderung Code ausführt und über Erfolg oder Fehler entscheidet. Das ist ein Meilenstein.
Zeig mir deine health-check.yml und einen Screenshot oder die Ausgabe aus dem Actions-Tab, wenn du durch bist. Bei der YAML-Einrückung bin ich gespannt – das ist erfahrungsgemäß der Teil wo es beim ersten Mal hakt.