"""
Projekt: Log-Analyzer CLI
Du baust ein kleines Kommandozeilen-Tool, das eine Logdatei 
auswertet und einen JSON-Report schreibt. Lege dafür einen neuen Ordner 
an, z.B. ~/Desktop/Python/loganalyzer/, mit drei Dateien: generator.py, analyzer.py, config.py.
Teil 1 — Testdaten erzeugen (Aufwärmen, ~15 Min)
Schreib generator.py: Es erzeugt eine Datei app.log mit 200 Zeilen in diesem Format:
2026-06-12 14:32:01 INFO Login erfolgreich user=max
2026-06-12 14:32:05 ERROR Datenbank nicht erreichbar user=laura
2026-06-12 14:32:09 WARNING Langsame Antwort user=max
Level (INFO, WARNING, ERROR, CRITICAL) und User (4–5 Namen) wählst du mit random.choice, den Zeitstempel baust du mit datetime (jede Zeile ein paar Sekunden später als die vorige). Pfad zur Logdatei:
 über BASE_DIR in der config.py — wie heute gelernt.




Teil 2 — Analyse (Kern, ~40 Min)
analyzer.py liest app.log Zeile für Zeile und baut ein Ergebnis-Dictionary mit dieser Struktur:
json{
  "gesamt": 200,
  "nach_level": {"INFO": 120, "ERROR": 35, "WARNING": 40, "CRITICAL": 5},
  "nach_user": {"max": 52, "laura": 48},
  "erster_critical": "2026-06-12 14:35:12 CRITICAL ..."
}
Dabei gelten drei harte Regeln — die sind der eigentliche Drill:

Keine Zwischenvariablen für Zählwerte. Du schreibst direkt ins Dictionary: report["nach_level"][level] = report["nach_level"].get(level, 0) + 1. Kein counter = 0 … counter += 1 … report[...] = counter.
json.dump steht exakt einmal im Code — nach der Schleife. Wenn du fertig bist, prüfe das bewusst nach.
erster_critical: Sobald die erste CRITICAL-Zeile gefunden ist, soll für dieses Feld nicht weitergesucht werden. Überleg dir, wie du das löst, ohne die Hauptschleife abzubrechen (die muss ja weiterzählen) — das ist die Denksportaufgabe des Tages. Es gibt mindestens zwei saubere Wege.




Der Report landet als report.json neben dem Skript (wieder BASE_DIR).


Teil 3 — Das neue Konzept: argparse (~30 Min)
Jetzt machst du aus analyzer.py ein richtiges CLI-Tool. Lies dir die ersten zwei Abschnitte der offiziellen Doku an (python -m pydoc argparse oder docs.python.org → argparse Tutorial), dann baue ein:

--level ERROR → es werden nur Zeilen mit diesem Level gezählt
--user max → nur Zeilen dieses Users
--output pfad/zur/datei.json → überschreibt den Default-Ausgabepfad
Ohne Argumente → alles wie in Teil 2

Das Grundgerüst, mehr bekommst du nicht:
pythonimport argparse

parser = argparse.ArgumentParser(description="Analysiert app.log")
parser.add_argument("--level", help="Nur dieses Log-Level zählen")
args = parser.parse_args()


# args.level ist dann entweder der String oder None
Erfolgs-Check am Ende — alle vier Aufrufe müssen funktionieren:
bashpython analyzer.py
python analyzer.py --level ERROR
python analyzer.py --user max --output /tmp/max_report.json
python analyzer.py --help   # ← bekommst du von argparse geschenkt
Bonus, falls noch Energie da ist: Bau einen --strict-Flag (action="store_true") ein, der das Skript mit sys.exit(1) beenden lässt, wenn mehr als 10 CRITICAL-Einträge gefunden wurden. Exit-Codes ≠ 0 sind die Sprache, in der CI/CD-Pipelines „Fehler" verstehen — damit wäre dein Tool theoretisch schon pipelinetauglich.
Zeitbudget insgesamt: ~90 Minuten. Schreib alles selbst, auch wenn's länger dauert — und wenn du fertig bist, zeig mir deinen Code, dann gehen wir ihn wie immer durch. Bei Teil 2, Regel 3 bin ich gespannt, welchen der Wege du findest.

"""


