"""
10 Drills – Fokus auf deine wiederkehrenden Fehler
List Comprehensions (ohne append!)
Drill 1: Gegeben: names = ["Anna", "Bo", "Christina", "Ed", "Maximilian"]. Erstelle per List Comprehension eine Liste mit nur den Namen die länger als 3 Buchstaben sind.


"""
names = ["Anna", "Bo", "Christina", "Ed", "Maximilian"]
list_long = [x for x in names if len(x) > 3]
print(list_long)

"""


Drill 2: Gegeben: prices = [150, 420, 80, 300, 50, 600]. Erstelle per List Comprehension eine neue Liste wo jeder Preis um 10% erhöht ist. Nur eine Zeile.

"""
import math
prices = [150, 420, 80, 300, 50, 600] 

list_long = [math.floor((x * 1.1)) for x in prices]
print(list_long)


"""
Drill 3: Gegeben: stocks = [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}, {"ticker": "TSLA", "price": 180}]. Erstelle per List Comprehension eine Liste mit nur den Dictionaries wo der Preis über 200 liegt.
json.dump korrekt (Modul.Funktion, nicht data.dump)

"""

stocks = [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}, {"ticker": "TSLA", "price": 180}]

list_long = [x for x in stocks if x["price"] > 200]
print(list_long)

"""


Drill 4: Schreibe den kompletten Read-Modify-Write-Zyklus aus dem Kopf. Datei heißt "portfolio.json", du willst den Key "status" auf "updated" setzen:
python# 1. Einlesen
# 2. Ändern
# 3. Zurückschreiben

"""
import json


with open("portfolio.json", "r") as data:
    data = json.load(data)

for i in data: 
    if isinstance(i["monthly_change"], float):
        if i["monthly_change"] > 2:
            i["status"] = "updatet"
    

with open("portfolio.json", "w") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

"""
Drill 5: Schreibe eine Funktion save_report(data, filepath) die ein Dictionary als JSON speichert. Drei Zeilen: Funktionsdefinition, open, dump.
f-String Formatierung (Doppelpunkt innerhalb der Klammern)

"""

def save_report(data,filepath):
    with open(filepath, "w") as f: 
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    



"""



Drill 6: Gegeben: price = 1234.5678. Printe den Preis auf 2 Dezimalstellen: 1234.57.

"""
price = 1234.5678

print(f"{price:.2f}")


"""
Drill 7: Gegeben: ticker = "AAPL", price = 300.5, change = -3.275. Erstelle exakt diese Ausgabe:
AAPL       300.50€    -3.28%
Direkt ins Dictionary schreiben (kein Umweg)


"""
ticker = "AAPL"
price = 300.5
change = -3.275
change = round(change,2)


print(f"{ticker:>10} {price:.2f}€ {change}")

"""




Drill 8: Gegeben ist eine Liste von Stocks. Füge jedem ein neues Feld "total" hinzu (price * shares):
pythonstocks = [
    {"ticker": "AAPL", "price": 300, "shares": 10},
    {"ticker": "MSFT", "price": 420, "shares": 5},
]
Dictionary-Merge über gemeinsamen Key


"""
pythonstocks = [
    {"ticker": "AAPL", "price": 300, "shares": 10},
    {"ticker": "MSFT", "price": 420, "shares": 5},
]

#total = prices * shares

for i in pythonstocks:
    i["total"] = i["price"] * i["shares"]

print(pythonstocks)



"""



Drill 9: Merge diese zwei Dictionaries ohne zweiten Loop:
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}, "TSLA": {"shares": 8}}
sectors = {"AAPL": "Tech", "MSFT": "Tech", "TSLA": "Auto"}
# Ergebnis: jedes Portfolio-Dict bekommt den Key "sector"
Kombination: Loop + Bedingung + break


"""
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}, "TSLA": {"shares": 8}}
sectors = {"AAPL": "Tech", "MSFT": "Tech", "TSLA": "Auto"}


for key, value in pythonportfolio.items():
    for i, test in sectors.items():
        if key is i:
            pythonportfolio[key]["sector"] = test
            break


print(pythonportfolio)







"""





Drill 10: Finde den ersten Stock mit negativem Profit, printe ihn, und stoppe:
pythonstocks = [
    {"ticker": "AAPL", "buy": 150, "current": 300},
    {"ticker": "MSFT", "buy": 420, "current": 400},
    {"ticker": "TSLA", "buy": 200, "current": 180},
]
# Berechne profit = current - buy
# Printe den ersten mit negativem Profit
# break
Timer: 20 Minuten für alle 10. Poste deine Lösungen.


"""

pythonstocks_2 = [
    {"ticker": "AAPL", "buy": 150, "current": 300},
    {"ticker": "MSFT", "buy": 420, "current": 400},
    {"ticker": "TSLA", "buy": 200, "current": 180},
]


#profit = current - buy

for stock in pythonstocks_2:
    if stock["current"] - stock["buy"] < 0:
        print(stock["ticker"])



"""




"""