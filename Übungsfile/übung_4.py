

"""
10 Drills – Tag 3
Dictionary-Zugriff ohne zweiten Loop (muss sitzen)
Drill 1: Gegeben sind zwei Datensätze. Füge jedem Stock den Sektor hinzu, ohne zweiten Loop:
pythonstocks = {"AAPL": {"price": 300}, "NVDA": {"price": 220}, "TSLA": {"price": 410}}
sectors = {"AAPL": "Technology", "NVDA": "Technology", "TSLA": "Consumer Cyclical"}
Drill 2: Gegeben sind Portfoliodaten und aktuelle Kurse. Berechne für jedes Asset den Profit direkt ins Dictionary, ohne zweiten Loop:
pythonportfolio = {"AAPL": {"buy": 150, "shares": 10}, "MSFT": {"buy": 300, "shares": 5}}
current = {"AAPL": 300, "MSFT": 420}
# Ergebnis: jedes Dict bekommt "current_price", "profit", "total_profit"
List Comprehension + Funktion kombiniert
Drill 3: Schreibe eine Funktion get_losers(stocks) die in einer Zeile alle Stocks mit negativem Profit zurückgibt:
pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": -100},
    {"ticker": "TSLA", "profit": 800},
    {"ticker": "CRWD", "profit": -250},
]
Drill 4: Schreibe eine Funktion extract_tickers(stocks) die per List Comprehension nur die Ticker-Strings extrahiert und als Liste zurückgibt. Dann schreibe eine zweite Funktion format_tickers(tickers) die sie per ", ".join() als einen String zurückgibt: "AAPL, MSFT, TSLA".
f-String Formatierung mit Vorzeichen und Ausrichtung
Drill 5: Erstelle eine formatierte Tabelle aus dem Kopf. Ticker linksbündig 8 Zeichen, Preis rechtsbündig 10 Zeichen mit 2 Dezimalstellen, Change mit Vorzeichen:
pythondata = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
    ("NVDA", 222.32, -8.123),
]
# Ausgabe:
# AAPL        300.50€   +12.80%
# MSFT        420.12€    -3.28%
# TSLA        180.90€   +45.67%
# NVDA        222.32€    -8.12%
try/except im Praxiskontext
Drill 6: Schreibe eine Funktion safe_load(filepath) die eine JSON-Datei einliest. Wenn die Datei nicht existiert, gib ein leeres Dictionary zurück. Wenn die Datei kaputtes JSON enthält, printe eine Fehlermeldung und gib ein leeres Dictionary zurück. Drei Exceptions: FileNotFoundError, json.JSONDecodeError, und Exception als Fallback.
Loop mit break und Ergebnis speichern
Drill 7: Finde den teuersten Stock unter 500€ und speichere ihn in einer Variable. Nicht printen, speichern:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "NVDA", "price": 222},
    {"ticker": "CRWD", "price": 618},
    {"ticker": "TSLA", "price": 410},
]
# Ergebnis: best = {"ticker": "MSFT", "price": 420}
Tipp: Kein break hier, aber eine Variable die sich im Loop aktualisiert.
Verschachtelte Dictionaries bauen
Drill 8: Baue aus diesen drei Listen ein verschachteltes Dictionary:
pythontickers = ["AAPL", "MSFT", "TSLA"]
prices = [300, 420, 180]
shares = [10, 5, 8]
# Ergebnis: {"AAPL": {"price": 300, "shares": 10}, "MSFT": ...}
Nutze zip() im Loop.
Komplette Mini-Pipeline
Drill 9: Schreibe drei Funktionen und eine Main-Funktion die alles zusammensteckt:
pythondef load_data(filepath):
    # JSON einlesen und zurückgeben

def enrich_data(stocks, sectors):
    # jedem Stock den Sektor hinzufügen (ohne zweiten Loop)
    # return stocks

def save_data(data, filepath):
    # data als JSON speichern

def main():
    # 1. load_data
    # 2. enrich_data
    # 3. save_data

if __name__ == "__main__":
    main()
dict.get() mit Default-Wert
Drill 10: Gegeben ist eine Liste von Log-Einträgen. Zähle die Vorkommen jedes Levels mit dict.get():
pythonlogs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "INFO", "ERROR", "DEBUG", "INFO"]
# Ergebnis: {"ERROR": 3, "INFO": 4, "WARNING": 1, "DEBUG": 1}
Vier Zeilen: leeres Dict, Loop, get mit Default 0, increment.
"""