
#### 21.05.

"""
20 Drills – zugeschnitten auf deine Schwächen
Block 1 – List Comprehensions (musst du drillen bis es sitzt)
Drill 1: Schreibe die folgende for-Loop als List Comprehension um:
pythonresult = []
for x in [10, 20, 30, 40, 50]:
    if x > 25:
        result.append(x)


"""


list = [10,20,30,40,50]
results = []

listcom = [results.append(x) for x in list if x > 25]

print(results)
"""



Drill 2: Schreibe die folgende for-Loop als List Comprehension um:
pythonresult = []
for x in [1, 2, 3, 4, 5]:
    result.append(x * 10)

"""
pythonresult = []



liste = [ pythonresult.append(x *10) for x in [1, 2, 3, 4, 5]]

print(pythonresult)


"""



Drill 3: Schreibe eine List Comprehension die aus einer Liste von Dictionaries nur die Ticker extrahiert:
pythonstocks = [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}]
# Ergebnis: ["AAPL", "MSFT"]


"""
pythonstocks = [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}]
new_list = []
listcomp = [new_list.append(x["ticker"]) for x in  pythonstocks if x["ticker"]]

print(new_list)

"""

Drill 4: Schreibe eine List Comprehension mit if/else: Gegeben ist numbers = [1, 2, 3, 4, 5, 6]. Erstelle eine Liste die "gerade" oder "ungerade" für jede Zahl enthält.

"""

numbers = [1,2,3,4,5,6]

ger="gerade"
ung="ungerade"

#ListComprehensions bauen listen von selbst
result = [f"{x} gerade" if x % 2 == 0 else f"{x} ungerade" for x in numbers]
print(result)


"""

[f"{x} if x % 2 == 0 else f"{x} ungerade" for x in numbers]
[f"{x} if x % 2 == 0 else f"{x} ungerade" for x in numbers]
[f"{x} if x % 2 == 0 else f"{x} ungerade" for x in numbers]
[f"{x if x % 2 == 0 }]


"""

"""


Drill 5: Schreibe eine Funktion die nur eine Zeile hat – eine List Comprehension im Return:
pythondef get_expensive(stocks, min_price):
 # return alle stocks wo price > min_price
Ergibt kein Sinn ohne die Variablendefiniton von price

[x * 2 if x > 5 else x for x in numbers]


"""
def get_expensive(stocks, min_price):
    return [stock for stock in stocks if stock["price"] > min_price]

stocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]

print(get_expensive(stocks, 250))
# [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}]

"""


Block 2 – Direkt ins Dictionary schreiben (dein Hauptfehler heute)
Drill 6: Gegeben ist ein Dictionary. Ändere den Wert direkt, ohne Zwischenvariable:
pythonstock = {"ticker": "AAPL", "price": 300, "status": "unknown"}
# Setze status auf "UP" – in einer Zeile

"""

pythonstock = {"ticker": "AAPL", "price": 300, "status": "unknown"}
pythonstock["status"] = "UP"


print(pythonstock)
"""


Drill 7: Loope durch eine Liste von Dictionaries und füge jedem einen neuen Key hinzu:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]
# Füge jedem Dict den Key "expensive" hinzu: True wenn price > 250, sonst False


"""
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]



"""
for stock in pythonstocks.items():
    stock["expensive"] = stock["price"] > 250

print(pythonstock)

"""
   #if Else Bedingung innerhalb der festlegung von dictionarys 



"""



Drill 8: Zwei Datensätze mergen über einen gemeinsamen Key, direkt ins Dictionary:
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}}
prices = {"AAPL": 300, "MSFT": 420}
# Ergebnis: {"AAPL": {"shares": 10, "price": 300}, "MSFT": {"shares": 5, "price": 420}}
Block 3 – break und Loop-Kontrolle


"""

pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}}
prices = {"AAPL": 300, "MSFT": 420}

# Loopen durch das Dictionary -> anschließend wird ein neuer Wert definiert
# info ["price"] und auf prices[ticker] gelegt 
for ticker, info in pythonportfolio.items():
    info["price"] = prices[ticker]
print(pythonportfolio)

"""






Drill 9: Finde den ersten Stock mit Preis über 400 und stoppe den Loop:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]
# Printe nur MSFT, dann break

"""




"""


Drill 10: Verschachtelter Loop mit break: Finde in welchem Portfolio ein bestimmter Ticker steckt:
pythonportfolios = {
    "tech": ["AAPL", "MSFT", "NVDA"],
    "auto": ["TSLA", "BMW", "VW"],
    "crypto": ["BTC", "ETH", "SOL"],
}
# Finde "TSLA" – printe "TSLA gefunden in auto" und brich beide Loops ab

"""




"""

Drill 11: Loop mit continue: Überspringe alle Einträge die None als Price haben:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "EUNL", "price": None},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "SGLD", "price": None},
]
# Printe nur AAPL und MSFT
Block 4 – json.dump Position und File I/O

"""

pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "EUNL", "price": None},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "SGLD", "price": None},
]



for i in pythonstocks:
    if i["price"] != None: 
        print(i["price"])
    else:
        continue

"""

Drill 12: Falsch vs. richtig. Korrigiere diesen Code:
pythonfor stock in stocks:
    stock["profit"] = stock["current"] - stock["buy"]
    with open("output.json", "w") as f:
        json.dump(stock, f, indent=4)

"""
"""
import json 

for stock in stocks:
    stock["profit"] = stock["current"] - stock["buy"]

with open("output.json", "w") as f:
    json.dump(stocks, f, indent=4)

"""




        






"""
Drill 13: Schreibe den kompletten Read-Modify-Write-Zyklus für JSON:
python# 1. JSON einlesen
# 2. Einen Wert im Dictionary ändern
# 3. Gesamte Datei zurückschreiben


"""
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "EUNL", "price": None},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "SGLD", "price": None},
]


with open("input.json", "r") as f:
     data = json.load(f)

for i in data:
    i["test"] = "geändert"

with open("input.json", "w") as b: 
    data.dump(stock, b, indent=4)


"""



Drill 14: Schreibe eine Funktion update_portfolio(filepath, ticker, new_price) die eine JSON-Datei einliest, den Preis eines bestimmten Tickers ändert, und die Datei zurückschreibt.
Block 5 – f-String Formatierung

"""

def update_portfolio(filepath, ticker, new_price):
    with open(filepath, "r") as f:
         data = json.load(f)
    
    for i in data:
        i[ticker] = new_price
        break
    
    with open(filepath, "w") as f:
        data.dump(stock, b, indent=4)


"""


Drill 15: Formatiere diese Ausgabe exakt: "AAPL:    300.23€  (+12.80%)". Nutze nur f-String-Syntax, kein math-Modul:
pythonticker = "AAPL"
price = 300.2345
change = 12.7956
# :.2f für Dezimalstellen, :>10 für Rechtsbündigkeit


"""
pythonticker = "AAPL"
price = 300.2345
change = 12.7956

print(f"{pythonticker}:>10 {price} ")




"""



Drill 16: Erstelle eine formatierte Tabelle per Loop:
pythonstocks = [("AAPL", 300.5, 12.8), ("MSFT", 420.123, -3.2), ("TSLA", 180.9, 45.6)]
# Ausgabe:
# AAPL   300.50€   +12.80%
# MSFT   420.12€    -3.20%
# TSLA   180.90€   +45.60%
Block 6 – Funktionen mit sauberem Return

"""


"""

Drill 17: Korrigiere diese Funktion:
pythondef get_total(price, shares):
    total = price * shares
    return print(total)



"""



"""
Drill 18: Schreibe eine Funktion die ein Dictionary zurückgibt, nicht printet:
pythondef analyze(ticker, buy, current, shares):
    # berechne profit und profit_pct
    # return {"ticker": ticker, "profit": ..., "profit_pct": ..., "status": "GEWINN"/"VERLUST"}
Block 7 – dict.get() mit Default

"""


"""

Drill 19: Nutze dict.get() um sicher auf fehlende Keys zuzugreifen:
pythonstock = {"ticker": "AAPL", "price": 300}
# Greife auf "dividend_yield" zu – soll 0 zurückgeben wenn nicht vorhanden
# Greife auf "sector" zu – soll "Unknown" zurückgeben wenn nicht vorhanden

"""



"""



Drill 20: Zähle mit dict.get() Vorkommen in einer Liste:
pythonlogs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "INFO", "ERROR"]
# Erstelle: {"ERROR": 3, "INFO": 3, "WARNING": 1}
# Nutze: counts[level] = counts.get(level, 0) + 1

"""