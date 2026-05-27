"""
10 Drills – Tag 4
Fokus: Tuple Unpacking, Format-Specs, Dict Comprehension, enumerate(), 
Variable im Loop korrekt aktualisieren, zip() festigen
"""

# ============================================================
# Drill 1 – Tuple Unpacking statt Index-Zugriff
# ============================================================
"""
Gegeben ist eine Liste von Tuples. Printe jede Zeile mit Unpacking 
(NICHT mit i[0], i[1], i[2]):

data = [
    ("Max", 28, "Erfurt"),
    ("Laura", 26, "Berlin"),
    ("Tom", 35, "München"),
]

Ausgabe:
Max ist 28 Jahre alt und lebt in Erfurt.
Laura ist 26 Jahre alt und lebt in Berlin.
Tom ist 35 Jahre alt und lebt in München.
"""

# Dein Code hier:

data = [
    ("Max", 28, "Erfurt"),
    ("Laura", 26, "Berlin"),
    ("Tom", 35, "München"),
]

for  name, alter, ort in data:
    print(f"{name} ist {alter} Jahre alt und lebt in {ort}")



# ============================================================
# Drill 2 – Format-Specs: Breite, Dezimalen, Vorzeichen
# ============================================================
"""
Formatiere diese Daten als Tabelle. 
Name linksbündig 12 Zeichen, Saldo rechtsbündig 10 Zeichen 
mit 2 Dezimalstellen und IMMER Vorzeichen (+/-):

accounts = [
    ("Girokonto", 1523.4),
    ("Sparkonto", -87.123),
    ("Depot", 45000.5),
    ("Kreditkarte", -1200.0),
]

Ausgabe:
Girokonto      +1523.40€
Sparkonto        -87.12€
Depot         +45000.50€
Kreditkarte    -1200.00€
"""

# Dein Code hier:
accounts = [
    ("Girokonto", 1523.4),
    ("Sparkonto", -87.123),
    ("Depot", 45000.5),
    ("Kreditkarte", -1200.0),
]

print("Ausgabe:")
for konto, betrag in accounts:
    print(f"{konto:<10}{betrag:>10}€")


# ============================================================
# Drill 3 – Dict Comprehension: neues Dict aus Liste bauen
# ============================================================
"""
Baue aus dieser Liste ein Dictionary {ticker: price} 
mit einer EINZIGEN Dict Comprehension:

stocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]

Ergebnis: {"AAPL": 300, "MSFT": 420, "TSLA": 180}
"""

# Dein Code hier:
stocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]

#Ergebnis: {"AAPL": 300, "MSFT": 420, "TSLA": 180}
#result = {KEY: VALUE for x in data}

result = {x["ticker"]: x["price"] for x in stocks}
print(result)


# ============================================================
# Drill 4 – Dict Comprehension mit Filter
# ============================================================
"""
Wie Drill 3, aber NUR Stocks mit Preis über 200:

stocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
    {"ticker": "NVDA", "price": 150},
]

Ergebnis: {"AAPL": 300, "MSFT": 420}
"""

# Dein Code hier:

result_2 = {x["ticker"]: x["price"] for x in stocks if x["price"] > 200}
print(result_2)

# ============================================================
# Drill 5 – enumerate(): Index + Wert gleichzeitig
# ============================================================
"""
Printe eine nummerierte Liste (startend bei 1) dieser Tickers.
Nutze enumerate(), NICHT range(len(...)):

tickers = ["AAPL", "MSFT", "TSLA", "NVDA", "CRWD"]

Ausgabe:
1. AAPL
2. MSFT
3. TSLA
4. NVDA
5. CRWD
"""

# Dein Code hier:

tickers = ["AAPL", "MSFT", "TSLA", "NVDA", "CRWD"]

for i, s in enumerate(tickers, 1):
    print(f"{i}. {s}")

# ============================================================
# Drill 6 – zip() + Dict bauen (Drill 8 von gestern nochmal)
# ============================================================
"""
Baue aus drei Listen ein verschachteltes Dict. 
Achte auf die Loop-Variablen-Namen (NICHT gleich wie die Listen!):

tickers = ["AAPL", "MSFT", "TSLA"]
prices = [300, 420, 180]
changes = [2.5, -1.3, 8.7]

Ergebnis: {
    "AAPL": {"price": 300, "change": 2.5},
    "MSFT": {"price": 420, "change": -1.3},
    "TSLA": {"price": 180, "change": 8.7},
}
"""

# Dein Code hier:
tickers = ["AAPL", "MSFT", "TSLA"]
prices = [300, 420, 180]
changes = [2.5, -1.3, 8.7]



result = {
    ticker: {
        "price": price,
        "change": change
    }
    for ticker, price, change in zip(tickers, prices, changes)
}

print(result)


# Habe ich durch Chat gpt gemacht - wäre nicht alleine auf den Syntax gekommen 

# ============================================================
# Drill 7 – Ganzes Objekt im Loop aktualisieren (nicht nur einen Wert)
# ============================================================
"""
Finde den Stock mit dem HÖCHSTEN absoluten Change (egal ob + oder -).
Speichere das GESAMTE Dict in einer Variable, nicht nur den Wert.

stocks = [
    {"ticker": "AAPL", "change": 2.5},
    {"ticker": "MSFT", "change": -7.3},
    {"ticker": "TSLA", "change": 4.1},
    {"ticker": "NVDA", "change": -1.8},
]

Ergebnis: best = {"ticker": "MSFT", "change": -7.3}
Tipp: abs() gibt den Absolutwert.
"""

stocks = [
    {"ticker": "AAPL", "change": 2.5},
    {"ticker": "MSFT", "change": -7.3},
    {"ticker": "TSLA", "change": 4.1},
    {"ticker": "NVDA", "change": -1.8},
]


# Dein Code hier:
test = {}
ph = 0

for i in stocks:
     i["change"] = abs(i["change"])
     x = i["change"]
     if ph < x:
         test = {"ticker": i["ticker"], "change": i["change"]}
                 

print(test)
print(ph)


# ============================================================
# Drill 8 – return vs print (Anti-Pattern erkennen)
# ============================================================
"""
Diese Funktion hat einen Bug. Finde ihn und fixe ihn:

def get_summary(stocks):
    total = sum(s["price"] for s in stocks)
    avg = total / len(stocks)
    return print(f"Total: {total}, Avg: {avg:.2f}")

stocks = [{"price": 300}, {"price": 420}, {"price": 180}]
result = get_summary(stocks)
print(f"Gespeichertes Ergebnis: {result}")

Was printed die letzte Zeile? Warum? Fixe die Funktion so, 
dass result den String enthält (nicht None).
"""

# Dein Code hier:

def get_summary(stocks):
    total = sum(s["price"] for s in stocks)
    print(total)
    avg = total / len(stocks)
    print(avg)
    return total, avg

stocks = [{"price": 300}, {"price": 420}, {"price": 180}]
result = get_summary(stocks)
print(get_summary(stocks))
print(f"Gespeichertes Ergebnis: {result}")
#print(f"Total: {total}, Avg: {avg:.2f}")

# ============================================================
# Drill 9 – try/except mit mehreren Exceptions (sauber)
# ============================================================
"""
Schreibe eine Funktion safe_divide(a, b) die:
- a / b zurückgibt
- Bei Division durch 0: printe "Division durch 0!" und gib None zurück
- Bei TypeError (z.B. "hello" / 2): printe "Falscher Typ!" und gib None zurück
- Bei jedem anderen Fehler: printe den Fehler und gib None zurück

Wichtig: print und return GETRENNT (nicht return print(...))!

Teste mit: safe_divide(10, 2), safe_divide(10, 0), safe_divide("hello", 2)
"""

# Dein Code hier:

def safe_divide(a,b):
    try:
        #return a / b
    
        if b or a == 0: 
            print("Division durch 0!")
            return None
    except TypeError:
        print("Falscher Typ!")
        return None
    else: 
        print("Fehler")
        return None
    
test = safe_divide(0, 5)



print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("hello", 2))


# ============================================================
# Drill 10 – Mini-Pipeline: alles kombiniert
# ============================================================
"""
Gegeben:

raw_data = [
    ("AAPL", "300.5", "12.8"),
    ("MSFT", "420.1", "-3.2"),
    ("TSLA", "ERROR", "45.6"),
    ("NVDA", "222.3", "-8.1"),
]

Aufgabe:
1. Schreibe eine Funktion parse_stock(ticker, price_str, change_str) die:
   - price und change zu float konvertiert
   - Bei ValueError ein Dict mit "error": True zurückgibt
   - Sonst ein Dict {"ticker": ..., "price": ..., "change": ..., "error": False}

2. Nutze eine List Comprehension um parse_stock auf jedes Tuple anzuwenden
   (Tuple Unpacking im Comprehension-Ausdruck: parse_stock(*row) )

3. Filtere per List Comprehension nur die fehlerfreien Einträge

4. Printe eine formatierte Tabelle der fehlerfreien Einträge:
   Ticker linksbündig 8, Preis rechtsbündig 10 mit 2 Dezimalen, 
   Change mit Vorzeichen

Erwartete Ausgabe:
AAPL        300.50   +12.80%
MSFT        420.10    -3.20%
NVDA        222.30    -8.10%
"""

# Dein Code hier:

raw_data = [
    ("AAPL", "300.5", "12.8"),
    ("MSFT", "420.1", "-3.2"),
    ("TSLA", "ERROR", "45.6"),
    ("NVDA", "222.3", "-8.1"),
]



def parse_stock(ticker, price_str, change_str):
    try:
        price_str = float(price_str)
        change_str = float(change_str)
        return {"ticker": ticker, "price":price_str, "change": change_str, "error": False}
    except ValueError:
        return {"ticker": ticker, "price":price_str, "change": change_str, "error": True}
    
    

    

listcomp = [parse_stock(x,i,c) for x,i,c in raw_data]
#print(listcomp)

fehlerfrei = [x for x in listcomp if x["error"] is not True ]
print(fehlerfrei)



for x in fehlerfrei:
    print(f"{x["ticker"]:>10} {x["price"]:>10,.2f} {x["change"]:+}%")

"""Aufgabe:
1. Schreibe eine Funktion parse_stock(ticker, price_str, change_str) die:
   - price und change zu float konvertiert
   - Bei ValueEsrror ein Dict mit "error": True zurückgibt
   - Sonst ein Dict {"ticker": ..., "price": ..., "change": ..., "error": False}

2. Nutze eine List Comprehension um parse_stock auf jedes Tuple anzuwenden
   (Tuple Unpacking im Comprehension-Ausdruck: parse_stock(*row) )

3. Filtere per List Comprehension nur die fehlerfreien Einträge

4. Printe eine formatierte Tabelle der fehlerfreien Einträge:
   Ticker linksbündig 8, Preis rechtsbündig 10 mit 2 Dezimalen, 
   Change mit Vorzeichen

Erwartete Ausgabe:
AAPL        300.50   +12.80%
MSFT        420.10    -3.20%
NVDA        222.30    -8.10%
"""