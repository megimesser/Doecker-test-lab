"""
10 Drills – Tag 5
Drill 1-5: Schwachstellen (Format-Specs, try/except, Mutation vermeiden)
Drill 6-10: Neue Themen (File I/O, verschachtelte Loops, Sets, String-Methoden, Default-Parameter)
"""

# ============================================================
# TEIL A – SCHWACHSTELLEN FESTIGEN
# ============================================================

# ============================================================
# Drill 1 – Format-Spec Reihenfolge auswendig
# ============================================================
"""
Printe jede Zeile EXAKT so wie vorgegeben. Keine Abweichung.
Schreibe den f-String aus dem Kopf — nicht raten, sondern die Reihenfolge anwenden:
    [fill][align][sign][width][.precision][type]

Erwartete Ausgabe (exakt):
Müller     +3850.00€
Schmidt     -120.50€
Weber     +12400.75€
Klein       -45.10€

Hinweis: Name linksbündig 10, Betrag rechtsbündig 10 mit 2 Dezimalen und Vorzeichen.
"""

# Dein Code hier:

employees = [
    ("Müller", 3850.00),
    ("Schmidt", -120.50),
    ("Weber", 12400.75),
    ("Klein", -45.10),
]

#for i,s in employees:
    #print(f"{i:10}{s:+}€")


# ============================================================
# Drill 2 – Format-Spec für gemischte Typen
# ============================================================
"""
Formatiere einen Fortschrittsbalken. Prozent soll IMMER 
mit Vorzeichen, 1 Dezimalstelle und 6 Zeichen breit sein:

tasks = [
    ("LFCS", 100.0),
    ("Python", 15.5),
    ("Docker", 0.0),
    ("AZ-104", -2.3),   # negativer Fortschritt = Rückschritt
]

Erwartete Ausgabe:
LFCS         [##########] +100.0%
Python       [##--------]  +15.5%
Docker       [----------]   +0.0%
AZ-104       [----------]   -2.3%

Hinweis: 
- Name linksbündig 12 Zeichen
- Balken: round(pct/10) '#'-Zeichen, Rest '-', immer 10 breit
- Prozent rechtsbündig 6 Zeichen, 1 Dezimalstelle, Vorzeichen
"""

# Dein Code hier:

import math


tasks = [
    ("LFCS", 100.0),
    ("Python", 15.5),
    ("Docker", 0.0),
    ("AZ-104", -2.3),   # negativer Fortschritt = Rückschritt
]


for i, l in tasks:
    string = ""
    zv = l / 10
    zv = math.ceil(zv)
    #print(zv)
    k = 0
    while k < zv:
        string += "#"
        k +=1
        
    while len(string) < 10:
        string += "-"

    
    string = "[" + string + "]"
    print(f"{i:<10} {string} {l:+}%")
    #print(string)

# Das ist hier meine "super" kreative Lösung den String passend zu formatieren :D 
#sag nix es funktioniert xD

    
        




# ============================================================
# Drill 3 – try/except: Lass Python werfen, fang dann
# ============================================================
"""
Schreibe eine Funktion safe_get(data, key, index) die:
1. data[key] nachschlägt (kann KeyError werfen)
2. Dann auf [index] zugreift (kann IndexError werfen)  
3. Das Ergebnis zurückgibt

Fang jeden Fehler SEPARAT ab und gib eine hilfreiche Meldung + None zurück.
KEINE if-Prüfungen vorher — lass Python werfen.

Teste mit:
  safe_get({"a": [1,2,3]}, "a", 1)      → 2
  safe_get({"a": [1,2,3]}, "b", 0)      → KeyError-Meldung, None
  safe_get({"a": [1,2,3]}, "a", 99)     → IndexError-Meldung, None
  safe_get("not a dict", "a", 0)         → allgemeiner Fehler, None
"""

# Dein Code hier:



# ============================================================
# Drill 4 – Originaldaten NICHT mutieren
# ============================================================
"""
Gegeben ist eine Liste von Stocks. Erstelle eine NEUE Liste 
mit einem zusätzlichen Feld "abs_change", OHNE die Originaldaten zu verändern.

stocks = [
    {"ticker": "AAPL", "change": -5.2},
    {"ticker": "MSFT", "change": 3.8},
    {"ticker": "TSLA", "change": -12.1},
]

Nach deinem Code muss gelten:
- enriched enthält Dicts mit "ticker", "change" UND "abs_change"
- stocks[0] hat KEIN "abs_change" (unverändert)

Tipp: Neues Dict bauen mit {**original, "neuer_key": wert}
"""

# Dein Code hier:



# ============================================================
# Drill 5 – try/except + return + Format-Spec kombiniert
# ============================================================
"""
Schreibe eine Funktion format_price(value) die:
- value zu float konvertiert (kann ValueError werfen bei z.B. "N/A")
- Den Float als String formatiert: rechtsbündig 10, 2 Dezimalen, Vorzeichen
- Bei ValueError den String "     ERROR" zurückgibt (10 Zeichen, rechtsbündig)

Teste mit:
  format_price("300.5")   → "   +300.50"
  format_price("-42")     → "    -42.00"
  format_price("N/A")     → "     ERROR"
  format_price(0)         → "     +0.00"
"""

# Dein Code hier:



# ============================================================
# TEIL B – NEUE THEMEN
# ============================================================

# ============================================================
# Drill 6 – File I/O: JSON schreiben und lesen
# ============================================================
"""
1. Erstelle ein Dictionary:
   portfolio = {
       "AAPL": {"shares": 10, "buy": 150},
       "MSFT": {"shares": 5, "buy": 300},
   }

2. Schreibe es in eine Datei "portfolio.json" mit json.dump()
   Wichtig: json.dump() NACH dem Loop / AUSSERHALB des with-Blocks 
   ist falsch — es muss INNERHALB des with-Blocks stehen, 
   aber NICHT in einem Loop.

3. Lies die Datei wieder ein mit json.load() in eine neue Variable.

4. Printe beide und vergleiche ob sie gleich sind (==).
"""

# Dein Code hier:



# ============================================================
# Drill 7 – Verschachtelte Loops (kontrolliert)
# ============================================================
"""
Gegeben sind Portfolios von mehreren Personen. 
Finde ALLE Stocks die in MEHR ALS EINEM Portfolio vorkommen.

portfolios = {
    "Max": ["AAPL", "MSFT", "TSLA"],
    "Laura": ["MSFT", "NVDA", "CRWD"],
    "Tom": ["AAPL", "CRWD", "AMD"],
}

Ergebnis: ["AAPL", "MSFT", "CRWD"]  (Reihenfolge egal)

Tipp: Erst alle Ticker in eine flache Liste sammeln (verschachtelter Loop),
dann zählen welche mehr als 1x vorkommen.
Bonuspunkte: collections.Counter benutzen.
"""

# Dein Code hier:



# ============================================================
# Drill 8 – Sets: Duplikate und Mengenoperationen
# ============================================================
"""
Gegeben sind zwei Listen von Tickers:

watchlist = ["AAPL", "MSFT", "TSLA", "NVDA", "AAPL", "MSFT"]
owned = ["MSFT", "CRWD", "NVDA"]

Berechne mit Set-Operationen:
1. unique_watchlist: alle einzigartigen Ticker der Watchlist
2. already_owned: Ticker die auf der Watchlist UND im Portfolio sind (Schnittmenge)
3. to_research: Ticker die auf der Watchlist aber NICHT im Portfolio sind (Differenz)
4. all_tickers: alle Ticker aus beiden Listen zusammen (Vereinigung)

Nutze set(), &, -, | (keine Loops!)
"""

# Dein Code hier:



# ============================================================
# Drill 9 – String-Methoden: split, strip, replace, join
# ============================================================
"""
Gegeben ist ein schlecht formatierter CSV-String:

raw = "  AAPL ; 300.5 ; +12.8% \n MSFT;420.1 ;-3.2% \n TSLA ; 180.9;+45.7%  "

Aufgabe:
1. Splitte nach Newline ("\n") → Liste von Zeilen
2. Für jede Zeile: splitte nach ";" → Liste von Feldern
3. Für jedes Feld: strip() (Whitespace entfernen)
4. Beim Change-Feld: replace("%", "") und replace("+", "") 
   dann zu float konvertieren
5. Baue eine Liste von Dicts: [{"ticker": ..., "price": ..., "change": ...}, ...]

Kein pandas — alles mit Bordmitteln.
"""

# Dein Code hier:



# ============================================================
# Drill 10 – Default-Parameter und keyword arguments
# ============================================================
"""
Schreibe eine Funktion filter_stocks(stocks, min_price=0, max_price=float("inf"), sector=None):
- Gibt alle Stocks zurück die ZWISCHEN min_price und max_price liegen
- Wenn sector angegeben ist, nur Stocks aus diesem Sektor
- Nutze Default-Parameter damit man die Funktion flexibel aufrufen kann

stocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech"},
    {"ticker": "MSFT", "price": 420, "sector": "Tech"},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare"},
    {"ticker": "JPM", "price": 190, "sector": "Finance"},
    {"ticker": "NVDA", "price": 222, "sector": "Tech"},
]

Teste:
  filter_stocks(stocks)                          → alle 5
  filter_stocks(stocks, min_price=200)           → AAPL, MSFT, NVDA
  filter_stocks(stocks, sector="Tech")           → AAPL, MSFT, NVDA
  filter_stocks(stocks, min_price=200, max_price=400, sector="Tech")  → AAPL, NVDA
"""

# Dein Code hier: