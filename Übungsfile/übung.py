"""
Block 1 – Variablen und Datentypen
Drill 1: Erstelle einen String, einen Integer, einen Float, eine Liste, ein Dictionary und ein Tuple. Prüfe den Typ jeder Variable mit type() und printe das Ergebnis.

"""

string = ""
integer = 1
float = 1.1
liste = []
dictionary = {}
tuple = ()




print(type(string))
print(type(integer))
print(type(float))
print(type(liste))
print(type(dictionary))
print(type(tuple))


"""


Drill 2: Erstelle ein Dictionary mit drei Aktien und ihren Kursen. Füge eine vierte hinzu, ändere den Kurs der ersten, lösche die zweite. Printe das Ergebnis nach jedem Schritt.

"""

kurse = {
    "Aktie_1" : "test_1",
    "Aktie_2" : "test_2",
    "Aktie_3" : "test_3",

}

print(kurse)

kurse["Aktie_4"] = "test_4"

print(kurse)

kurse["Aktie_1"]="geändert"


kurse.update({
    "Aktie_1": "Erfurt",
})

print(kurse)

del kurse["Aktie_2"]

print(kurse)

"""

Drill 3: Erstelle eine Liste mit den Zahlen 1–10. Extrahiere per Slicing: die ersten drei, die letzten zwei, jede zweite, die Liste rückwärts.
"""

liste=[1,2,3,4,5,6,7,8,9,10]

ext = liste[0:3]
print(ext)

ext= liste [-2:]
print(ext)


ext=liste[0::2]
print(ext)

ext = list(reversed(liste))
print(ext)
"""

Block 2 – Strings
Drill 4: Gegeben ist der String "  2026-05-15 ERROR Database connection timeout  ". Entferne Whitespace, prüfe ob "ERROR" enthalten ist, splitte am Leerzeichen, extrahiere nur das Datum, wandle alles in Großbuchstaben.

"""

string = "  2026-05-15 ERROR Database connection timeout  "
print(string)

string = string.strip()
print(string)


ext = string[0:10]
print(ext)


upper = string.upper()
print(upper)
#print(string)

import re
x = re.findall(".*ERROR.*", string)
print(x)



string = string.split()
print(string)

"""



Drill 5: Erstelle einen f-String der folgendes ausgibt: AAPL: 300.23€ (+12.80%). Die Werte kommen aus drei Variablen: ticker = "AAPL", price = 300.234, change = 12.8. Der Preis soll auf 2 Dezimalstellen formatiert sein, die Prozent-Änderung ebenfalls.

"""
ticker = "AAPL"
price = 300.234

import math 

price = math.floor(price * 100) / 100
change = 12.8



fstring = f'{ticker}: {price}€ (+{change}%)'
print(fstring)
"""

Block 3 – Listen und Loops
Drill 6: Erstelle eine Liste von 10 Zahlen. Filtere per List Comprehension alle geraden Zahlen raus. Filtere per List Comprehension alle Zahlen größer als 5. Erstelle eine neue Liste wo jede Zahl verdoppelt ist.

"""

list_numbers = [1,2,5,23,12,53,63,16,1,99]

for i in list_numbers:
    if i % 2 == 0:
        print(f"{i} gerade")

for i in list_numbers:
    if i > 5:
        print(f"{i} ist größer als 5")


new_list = []

for i in list_numbers:
    x = i * 2
    new_list.append(x)

print(new_list)

"""



Drill 7: Gegeben sind zwei Listen: names = ["AAPL", "MSFT", "TSLA"] und prices = [300, 420, 180]. Erstelle daraus per zip() ein Dictionary. Iteriere mit enumerate() über die Namen und printe "1: AAPL", "2: MSFT" usw.

"""
names = ["AAPL", "MSFT", "TSLA"] 
prices = [300, 420, 180]

dictionary = zip(names, prices)

print(list(dictionary))


for index, names in enumerate(names, start=1):
    print(index, names)

"""

Drill 8: Gegeben ist eine verschachtelte Liste: portfolio = [["AAPL", 150, 10], ["MSFT", 300, 5], ["TSLA", 200, 8]]. Berechne für jede Position den Gesamtwert (Preis * Anzahl) und speichere alles in einer neuen Liste von Dictionaries mit den Keys ticker, price, shares, total.

"""

portfolio = [["AAPL", 150, 10], ["MSFT", 300, 5], ["TSLA", 200, 8]]


new_dic = []


for i in portfolio:
    total = i[1] * i[2]
    new_dic = [
        "shares",{
        "ticker": i[0],
        "price": i[1],
        "shares": i[2],
        "total" : total
    }]

    print(total)
    print(new_dic)









"""


Block 4 – Dictionaries
Drill 9: Erstelle ein verschachteltes Dictionary:
python{"AAPL": {"price": 300, "shares": 10}, "MSFT": {"price": 420, "shares": 5}}

"""

dic = {
    "AAPL" : {
        "price" : 300,
        "shares" : 10 
    },
    "MSFT": {
        "price" : 420,
        "shares" : 5
    }
}


print(dic["AAPL"]["price"])
"""

Greife auf den Preis von AAPL zu. 



"""

for i in dic:
    if i == "AAPL":
        print(f"{i}: {dic["AAPL"]["shares"]} shares")

"""

Iteriere über alle Ticker und printe "AAPL: 10 Shares".


 Berechne den Gesamtwert aller Positionen.
Drill 10: Gegeben ist eine Liste von Log-Zeilen. Zähle mit einem Dictionary wie oft jedes Log-Level vorkommt. Nutze dict.get() mit Default-Wert:
pythonlogs = ["INFO ok", "ERROR fail", "INFO ok", "WARNING slow", "ERROR crash", "INFO ok"]

"""

dic["AAPL"]["summe"] = dic["AAPL"]["price"] * dic["AAPL"]["shares"]
dic["MSFT"]["summe"] = dic["MSFT"]["price"] * dic["MSFT"]["shares"]

"""
dic.update({
    "AAPL" : {
        "summe": dic["AAPL"]["price"] * dic["AAPL"]["shares"]
    }
})
"""


print(dic)

"""



"""
"""


Block 5 – Funktionen
Drill 11: Schreibe eine Funktion calculate_profit(buy, current, shares) die den Profit berechnet und zurückgibt. 
Schreibe eine zweite Funktion calculate_percentage(buy, current) die die prozentuale Änderung zurückgibt. Rufe beide auf und printe die Ergebnisse.


"""
def calculate_profit(buy, current, shares):
    if current > buy:
        profit = (current - buy) * shares
    elif current < buy:
        profit = (buy - current) * shares
    elif current == buy:
        profit = current * shares 
    
    return profit

x = calculate_profit(200, 300, 2)
print(x)
    






"""




Drill 12: Schreibe eine Funktion filter_logs(lines, level) die eine Liste von Log-Zeilen und ein Level nimmt und nur die Zeilen mit diesem Level zurückgibt. Nutze eine List Comprehension im Return.



# Kann keine List comprehension 

"""
clocker = ["ilove dicks", "ilove cunts", "ilove dicks"]



import re

def filter_logs(lines, levels):
    levels = str(levels)
    clean_lines = ""
    for i in lines: 
        if re.search(f".*{levels}.*", i) == i: 
            clean_lines.append(i)

    return clean_lines


f = filter_logs(clocker, "dicks")
print(f)

"""


Drill 13: Schreibe eine Funktion mit Default-Parametern: format_price(price, currency="EUR", decimals=2). Sie soll "300.23 EUR" zurückgeben. Rufe sie auf mit und ohne die optionalen Parameter.
Block 6 – File I/O

"""

def format_price(price=300.23, currency="EUR",decimal=2):
        return f"{price} {currency}"


print(format_price())

"""




Drill 14: Schreibe ein Dictionary als JSON in eine Datei. Lies die Datei wieder ein und printe den Inhalt. Nutze json.dump() und json.load().


"""

import json

data={
    "test" : {
        "test" : "test",
        "test" : "test"
    }
}

with open("datei.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("datei.json", "r", encoding="utf-8") as f:
    test = json.load

print(test)


"""



Drill 15: Schreibe eine Funktion die eine Textdatei einliest und die Anzahl Zeilen, Wörter und Zeichen zurückgibt. Rückgabe als Dictionary: {"lines": 10, "words": 50, "chars": 300}.
Block 7 – Exception Handling

"""


test = "file.txt"

def counter(file):
    with open(file, "r") as printer:
        x = printer.readlines()
        lines = 0
        words = 0
        zeichen = 0
        for i in x: 
            lines += 1

        x = str(x)

        f = x.strip()
        for l in f:
            zeichen += 1
    
        x = x.split()
        for k in x:
            words += 1 
        
        dic = {"lines": lines, "words": words, "chars": zeichen}
        




    return dic



x = counter(test)
print(x)





"""

Drill 16: Schreibe einen try/except-Block der eine Datei öffnet die nicht existiert. Fange FileNotFoundError und printe eine saubere Fehlermeldung statt eines Tracebacks.


"""

try:
    with open("test.txt", "r") as file:
        x = file.read()

except FileNotFoundError:
    print("Datei existiert nicht")
"""


Drill 17: Schreibe eine Funktion safe_divide(a, b) die ZeroDivisionError fängt und None zurückgibt. Schreibe eine zweite Version die TypeError fängt falls jemand einen String übergibt.


"""

def safe_divide(a,b): 
    try: 
        f =  a / b 
    except ZeroDivisionError:
        print("Fehler")
    except TypeError:
        print("Fehler")



"""




Block 8 – OOP Basics


Drill 18: Schreibe eine Klasse Stock mit __init__(self, ticker, buy_price, shares). Füge eine Methode total_value(self) hinzu die buy_price * shares zurückgibt. Erstelle zwei Instanzen und printe ihre Werte.


Drill 19: Erweitere die Stock-Klasse um eine Methode profit(self, current_price) die den Gewinn/Verlust berechnet. Füge eine __str__-Methode hinzu die "AAPL: 10 Shares @ 150€" zurückgibt.
Block 9 – Alles zusammen


Drill 20: Baue ein Mini-Script ohne nachzuschauen:

Erstelle eine Liste von 5 Stock-Dictionaries (ticker, buy_price, shares, current_price)
Schreibe eine Funktion die den profitabelsten Stock findet
Schreibe eine Funktion die den Gesamtwert des Portfolios berechnet
Schreibe das Ergebnis als JSON in eine Datei
Lies die Datei wieder ein und printe sie formatiert

Mach jeden Drill einmal, markiere wo du nachschauen musstest, und wiederhole genau diese Drills am nächsten Tag. Dasselbe Prinzip wie dein LFCS-Fehlertracking.




15 Neue Drills
Block 1 – List Comprehensions (deine größte Lücke)






Drill 1: Gegeben ist eine Liste words = ["hello", "world", "python", "docker", "api"]. Erstelle per List Comprehension eine neue Liste die nur Wörter mit mehr als 4 Buchstaben enthält.
Drill 2: Gegeben ist numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Erstelle per List Comprehension eine Liste von Strings: ["1 ist ungerade", "2 ist gerade", "3 ist ungerade", ...]. Tipp: Ternary Operator in der Comprehension: "gerade" if x % 2 == 0 else "ungerade".
Drill 3: Gegeben sind zwei Listen: tickers = ["AAPL", "MSFT", "TSLA"] und prices = [300, 420, 180]. Erstelle per List Comprehension eine Liste von Dictionaries: [{"ticker": "AAPL", "price": 300}, ...]. Nutze zip() innerhalb der Comprehension.
Drill 4: Gegeben ist eine verschachtelte Liste: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Flache sie zu einer einzigen Liste ab per List Comprehension: [1, 2, 3, 4, 5, 6, 7, 8, 9].
Block 2 – Funktionen und Return-Werte
Drill 5: Schreibe eine Funktion analyze_stock(ticker, buy, current, shares) die ein Dictionary zurückgibt mit den Keys ticker, profit, profit_pct, status. Status ist "GEWINN" wenn Profit positiv, "VERLUST" wenn negativ, "NEUTRAL" wenn null.

"""



"""


Drill 6: Schreibe eine Funktion best_performer(stocks) die eine Liste von Dictionaries nimmt (jeweils mit ticker und profit_pct) und den Ticker mit der höchsten prozentualen Performance zurückgibt. Nutze max() mit key-Parameter.
Drill 7: Schreibe eine Funktion format_report(stocks) die eine Liste von Stock-Dictionaries nimmt und einen formatierten String zurückgibt. Jede Zeile soll aussehen wie: "AAPL: +15.30% (GEWINN)". Nutze einen f-String mit :.2f für die Prozent-Formatierung.
Block 3 – Dictionary-Operationen
Drill 8: Gegeben ist eine Liste von Dictionaries:
pythontransactions = [
    {"ticker": "AAPL", "amount": 500},
    {"ticker": "MSFT", "amount": 300},
    {"ticker": "AAPL", "amount": 200},
    {"ticker": "TSLA", "amount": 100},
    {"ticker": "MSFT", "amount": 400},
]
Summiere die Amounts pro Ticker in ein neues Dictionary: {"AAPL": 700, "MSFT": 700, "TSLA": 100}. Nutze dict.get() mit Default 0.
Drill 9: Schreibe eine Funktion merge_data(portfolio, prices) die zwei Dictionaries zusammenführt. portfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}} und prices = {"AAPL": 300, "MSFT": 420}. Ergebnis: {"AAPL": {"shares": 10, "price": 300}, "MSFT": {"shares": 5, "price": 420}}.
Block 4 – File I/O und JSON
Drill 10: Schreibe eine Funktion save_and_load(data, filepath) die ein Dictionary als JSON speichert, es sofort wieder einliest, und das eingelesene Dictionary zurückgibt. Prüfe mit assert dass Original und eingelesene Version identisch sind.
Drill 11: Schreibe eine Funktion append_to_log(filepath, message) die eine Zeile mit Timestamp an eine Textdatei anhängt (nicht überschreibt). Format: "2026-05-18 14:30:00 - Deine Nachricht". Nutze open() mit Mode "a".
Block 5 – OOP Basics
Drill 12: Schreibe eine Klasse Stock:
pythonclass Stock:
    def __init__(self, ticker, buy_price, shares):
        # speichere die drei Werte als self.ticker, self.buy_price, self.shares
Erstelle zwei Instanzen: stock1 = Stock("AAPL", 150, 10) und stock2 = Stock("MSFT", 300, 5). Printe stock1.ticker und stock2.buy_price.
Eine Klasse ist eine Schablone für Objekte. __init__ ist die Methode die beim Erstellen aufgerufen wird. self ist das Objekt selbst – damit speicherst du Daten am Objekt.
Drill 13: Erweitere die Stock-Klasse um eine Methode:
pythondef total_value(self):
    return self.buy_price * self.shares
Rufe sie auf: print(stock1.total_value()). Eine Methode ist eine Funktion die zu einer Klasse gehört und auf self zugreifen kann.
Drill 14: Füge eine __str__-Methode hinzu:
pythondef __str__(self):
    return f"{self.ticker}: {self.shares} Shares @ {self.buy_price}€"
Jetzt gibt print(stock1) automatisch "AAPL: 10 Shares @ 150€" aus statt <__main__.Stock object at 0x...>. __str__ wird von print() aufgerufen.
Drill 15: Erstelle eine Klasse Portfolio die eine Liste von Stock-Objekten verwaltet:
pythonclass Portfolio:
    def __init__(self):
        self.stocks = []

    def add(self, stock):
        self.stocks.append(stock)

    def total_value(self):
        # summiere total_value() aller Stocks
Erstelle ein Portfolio, füge drei Stocks hinzu, printe den Gesamtwert. Das ist eine Klasse die andere Klassen nutzt – Komposition, ein OOP-Grundkonzept.

Drill-Routine
Mach die 15 Drills durch. Markiere jeden mit einem Emoji:

✅ Aus dem Gedächtnis geschafft
⚠️ Musste kurz nachschauen
❌ Keine Ahnung, komplett nachgeschaut

Wiederhole morgen nur die ⚠️ und ❌. Übermorgen nochmal die verbleibenden ❌. Wenn alles auf ✅ steht, bekommst du den nächsten Satz.



"""


data = {"name" : "Max",
        "test" : "test"  
        }
data["name"]

print(data)

data.update({
        "test" :{
            "test" : "test"
        }})




data.update({
    "test":{
        "test" : "test2",
        "test2" : "test3"
    }
})


data["test"]["test"] = "lol"

data["knewkey"] = "frei"

###data["123"]["123"] = 23
### Keywords lassen sich nicht in verschachtelte Dictionarys hinzufügen 
### Vorher muss es eine definition der Variable vorab geben 

print(data)

f = data.get("knewkey")
print(f)


data.get("name")
data.get("name")
data.get("name")
data.get("name")

data.update({
    "TEST":"TEST",
    "TEST_2":"TEST_2",
    "TEST_3":"TEST_3"
})
   
for key, value in data.items():
    print(F"{key}: {value}")


newdic = {}

newdic.update({
    "new" :"new",
    "nwq":"nwq",
})

for key, value in newdic.items():
    print(f"{key},{value}")


test = {}

test["test"] = "test"
test["zwei"] = "zwei"

print(test)

for key, value in test.items():
    print(f"{key}, {value}")


for key, value in test.items():
    print(f"{key}, {value}")

for key, value in test.items():
    print(f"{key}, {value}")

"""

for key, value in test.items()
for key, vakue in test.items()
for key, value in test.items()
for key ,value in test.items()
for key, value in test.items():
    print(f"{key}, {value}")

for key, value in test.items():
    print(f"{key}, {value}")

for key, value in test.items():
    print(f"{key}, {value}")


test["test"] = 2
test["test"] = 5
test["test"] = 10 
test["test"] = 20
test["test"] = 30

"""
items = [1,2,3,4,5]

result = [x for x in items if x >3] 
results = [x * 2 for x in items]

print(result)
print(results)

result = [x for x in items if x > 3]
# variable = [ iterationsvariable in iterationsvariable im iterationsobjekt bedingung]


test = [2,2,2]
test = [x for x in test if x >1 ]
test = [x * 2 for x in test]
print(test)




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


"""



Drill 2: Schreibe die folgende for-Loop als List Comprehension um:
pythonresult = []
for x in [1, 2, 3, 4, 5]:
    result.append(x * 10)
Drill 3: Schreibe eine List Comprehension die aus einer Liste von Dictionaries nur die Ticker extrahiert:
pythonstocks = [{"ticker": "AAPL", "price": 300}, {"ticker": "MSFT", "price": 420}]
# Ergebnis: ["AAPL", "MSFT"]
Drill 4: Schreibe eine List Comprehension mit if/else: Gegeben ist numbers = [1, 2, 3, 4, 5, 6]. Erstelle eine Liste die "gerade" oder "ungerade" für jede Zahl enthält.
Drill 5: Schreibe eine Funktion die nur eine Zeile hat – eine List Comprehension im Return:
pythondef get_expensive(stocks, min_price):
    # return alle stocks wo price > min_price
Block 2 – Direkt ins Dictionary schreiben (dein Hauptfehler heute)
Drill 6: Gegeben ist ein Dictionary. Ändere den Wert direkt, ohne Zwischenvariable:
pythonstock = {"ticker": "AAPL", "price": 300, "status": "unknown"}
# Setze status auf "UP" – in einer Zeile
Drill 7: Loope durch eine Liste von Dictionaries und füge jedem einen neuen Key hinzu:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]
# Füge jedem Dict den Key "expensive" hinzu: True wenn price > 250, sonst False
Drill 8: Zwei Datensätze mergen über einen gemeinsamen Key, direkt ins Dictionary:
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}}
prices = {"AAPL": 300, "MSFT": 420}
# Ergebnis: {"AAPL": {"shares": 10, "price": 300}, "MSFT": {"shares": 5, "price": 420}}
Block 3 – break und Loop-Kontrolle
Drill 9: Finde den ersten Stock mit Preis über 400 und stoppe den Loop:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "TSLA", "price": 180},
]
# Printe nur MSFT, dann break
Drill 10: Verschachtelter Loop mit break: Finde in welchem Portfolio ein bestimmter Ticker steckt:
pythonportfolios = {
    "tech": ["AAPL", "MSFT", "NVDA"],
    "auto": ["TSLA", "BMW", "VW"],
    "crypto": ["BTC", "ETH", "SOL"],
}
# Finde "TSLA" – printe "TSLA gefunden in auto" und brich beide Loops ab
Drill 11: Loop mit continue: Überspringe alle Einträge die None als Price haben:
pythonstocks = [
    {"ticker": "AAPL", "price": 300},
    {"ticker": "EUNL", "price": None},
    {"ticker": "MSFT", "price": 420},
    {"ticker": "SGLD", "price": None},
]
# Printe nur AAPL und MSFT
Block 4 – json.dump Position und File I/O
Drill 12: Falsch vs. richtig. Korrigiere diesen Code:
pythonfor stock in stocks:
    stock["profit"] = stock["current"] - stock["buy"]
    with open("output.json", "w") as f:
        json.dump(stock, f, indent=4)
Drill 13: Schreibe den kompletten Read-Modify-Write-Zyklus für JSON:
python# 1. JSON einlesen
# 2. Einen Wert im Dictionary ändern
# 3. Gesamte Datei zurückschreiben
Drill 14: Schreibe eine Funktion update_portfolio(filepath, ticker, new_price) die eine JSON-Datei einliest, den Preis eines bestimmten Tickers ändert, und die Datei zurückschreibt.
Block 5 – f-String Formatierung
Drill 15: Formatiere diese Ausgabe exakt: "AAPL:    300.23€  (+12.80%)". Nutze nur f-String-Syntax, kein math-Modul:
pythonticker = "AAPL"
price = 300.2345
change = 12.7956
# :.2f für Dezimalstellen, :>10 für Rechtsbündigkeit
Drill 16: Erstelle eine formatierte Tabelle per Loop:
pythonstocks = [("AAPL", 300.5, 12.8), ("MSFT", 420.123, -3.2), ("TSLA", 180.9, 45.6)]
# Ausgabe:
# AAPL   300.50€   +12.80%
# MSFT   420.12€    -3.20%
# TSLA   180.90€   +45.60%
Block 6 – Funktionen mit sauberem Return
Drill 17: Korrigiere diese Funktion:
pythondef get_total(price, shares):
    total = price * shares
    return print(total)
Drill 18: Schreibe eine Funktion die ein Dictionary zurückgibt, nicht printet:
pythondef analyze(ticker, buy, current, shares):
    # berechne profit und profit_pct
    # return {"ticker": ticker, "profit": ..., "profit_pct": ..., "status": "GEWINN"/"VERLUST"}
Block 7 – dict.get() mit Default
Drill 19: Nutze dict.get() um sicher auf fehlende Keys zuzugreifen:
pythonstock = {"ticker": "AAPL", "price": 300}
# Greife auf "dividend_yield" zu – soll 0 zurückgeben wenn nicht vorhanden
# Greife auf "sector" zu – soll "Unknown" zurückgeben wenn nicht vorhanden
Drill 20: Zähle mit dict.get() Vorkommen in einer Liste:
pythonlogs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "INFO", "ERROR"]
# Erstelle: {"ERROR": 3, "INFO": 3, "WARNING": 1}
# Nutze: counts[level] = counts.get(level, 0) + 1

"""



# Was macht Continue innerhalb eines for loops im if else Statement ?