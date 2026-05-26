

"""
10 Drills – Tag 3
Dictionary-Zugriff ohne zweiten Loop (muss sitzen)
Drill 1: Gegeben sind zwei Datensätze. Füge jedem Stock den Sektor hinzu, ohne zweiten Loop:
pythonstocks = {"AAPL": {"price": 300}, "NVDA": {"price": 220}, "TSLA": {"price": 410}}
sectors = {"AAPL": "Technology", "NVDA": "Technology", "TSLA": "Consumer Cyclical"}
"""

pythonstocks = {"AAPL": {"price": 300}, "NVDA": {"price": 220}, "TSLA": {"price": 410}}
sectors = {"AAPL": "Technology", "NVDA": "Technology", "TSLA": "Consumer Cyclical"}

for k, v in sectors.items():
    pythonstocks[k]["sector"] = v

print(pythonstocks)
# Hier habe ich nachgeschaut - Ich wusste nicht, dass man durch sectory loopen muss und auf den key loopt


"""
Drill 2: Gegeben sind Portfoliodaten und aktuelle Kurse. Berechne für jedes Asset den Profit direkt ins Dictionary, ohne zweiten Loop:
pythonportfolio = {"AAPL": {"buy": 150, "shares": 10}, "MSFT": {"buy": 300, "shares": 5}}
current = {"AAPL": 300, "MSFT": 420}
# Ergebnis: jedes Dict bekommt "current_price", "profit", "total_profit"
List Comprehension + Funktion kombiniert
"""

pythonportfolio = {"AAPL": {"buy": 150, "shares": 10}, "MSFT": {"buy": 300, "shares": 5}}
current = {"AAPL": 300, "MSFT": 420}


#list_comp = [ k,v for k,v in pythonportfolio.items()]


for k, v in current.items():
    pythonportfolio[k]["profit"] = pythonportfolio[k]["shares"] * v
    pythonportfolio[k]["current_price"] = v
    zwischenvariable = pythonportfolio[k]["profit"] - pythonportfolio[k]["buy"] * pythonportfolio[k]["shares"]
    pythonportfolio[k]["total_profit"] = zwischenvariable
    

print(pythonportfolio)

#print(pythonportfolio)
# weiß nicht wie man hier eine listcomprehension mit einfügt 


"""
Drill 3: Schreibe eine Funktion get_losers(stocks) die in einer Zeile alle Stocks mit negativem Profit zurückgibt:
pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": -100},
    {"ticker": "TSLA", "profit": 800},
    {"ticker": "CRWD", "profit": -250},
]
"""

pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": -100},
    {"ticker": "TSLA", "profit": 800},
    {"ticker": "CRWD", "profit": -250},]


def get_losers(stocks):
    vals = []
    for k in stocks:
        if k["profit"] < 0:
            vals.append(k)
    return vals


lister = [stocks for stocks in pythonstocks if stocks["profit"] < 0]


def alt_loser(stocks):
    return [x for x in stocks if x["profit"] < 0]
    


print(lister)

    #list_comp = [value for value in stocks if value < 0]  
    #return list_comp
    # In einer Listcomprehension wird zuerst angegeben was in den Listenausdruck hineinsoll , hier also "x" danach für welche Argumente in der Liste wieder "x" so entsteht x for x 
    # ich will eine Liste von Ergebnissen
    # result = [EXPRESSION for x in data]
    # Ich will eine Zuordnung Mapping 
    #result = {KEY: VALUE for x in data}


print(get_losers(pythonstocks))
print(alt_loser(pythonstocks))



"""
Drill 4: Schreibe eine Funktion extract_tickers(stocks) 
die per List Comprehension nur die Ticker-Strings extrahiert und als Liste zurückgibt. 
Dann schreibe eine zweite Funktion format_tickers(tickers) die sie per ", ".join() als einen String zurückgibt: "AAPL, MSFT, TSLA".
f-String Formatierung mit Vorzeichen und Ausrichtung
"""

def extract_tickers(stocks):
    return [x["ticker"] for x in stocks]

def format_tickers(ticker): 
    return f"{",".join(ticker)}"


print(extract_tickers(pythonstocks))
print(format_tickers(extract_tickers(pythonstocks)))

# Fstringformatierung musste ich googeln weiß auch nicht was mit vorzeichen gemeint ist strigs haben doch keines ???




"""
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
"""


pythondata = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
    ("NVDA", 222.32, -8.123),
]

print("# Ausgabe:")
for i in pythondata: 
    
    print(f"# {i[0]} {i[1]:10}€ {i[2]:10}%")




"""
Drill 6: Schreibe eine Funktion safe_load(filepath) die eine JSON-Datei einliest. 
Wenn die Datei nicht existiert, gib ein leeres Dictionary zurück. 
Wenn die Datei kaputtes JSON enthält, 
printe eine Fehlermeldung und gib ein leeres Dictionary zurück. Drei Exceptions: FileNotFoundError, json.JSONDecodeError, und Exception als Fallback.
Loop mit break und Ergebnis speichern

"""
import json

def safe_load(filepath):
    empty_dic = {}
    try:
        with open(filepath, "r") as f:
          data = json.load(f)
          return data 
    except FileNotFoundError:
         return empty_dic
    except json.JSONDecodeError:
        return print("Json ist kaputt"), empty_dic
        

print(safe_load("testfile.json"))



"""
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

"""
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "NVDA", "price": 222},
    {"ticker": "CRWD", "price": 618},
    {"ticker": "TSLA", "price": 410},
]

var = 0
for i in pythonstocks: 
    if i["price"] > var and i["price"] < 500:
        var = i["price"]
    

print(var)



"""

Drill 8: Baue aus diesen drei Listen ein verschachteltes Dictionary:
pythontickers = ["AAPL", "MSFT", "TSLA"]
prices = [300, 420, 180]
shares = [10, 5, 8]
# Ergebnis: {"AAPL": {"price": 300, "shares": 10}, "MSFT": ...}
Nutze zip() im Loop.
Komplette Mini-Pipeline
"""

"""
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
"""



"""

Drill 10: Gegeben ist eine Liste von Log-Einträgen. Zähle die Vorkommen jedes Levels mit dict.get():
pythonlogs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "INFO", "ERROR", "DEBUG", "INFO"]
# Ergebnis: {"ERROR": 3, "INFO": 4, "WARNING": 1, "DEBUG": 1}
Vier Zeilen: leeres Dict, Loop, get mit Default 0, increment.
"""