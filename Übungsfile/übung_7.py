

# Für morgen bitte mal nur 5 Aufgaben - brauche die restliche Zeit um ein paar Tutorials zu binchen :) 


"""
5 Aufgaben für morgen
Drill 1 – Set-Operationen (muss sitzen nach heute):
pythonlist_a = ["AAPL", "MSFT", "TSLA", "NVDA"]
list_b = ["MSFT", "NVDA", "AMD", "CRWD"]
# Berechne: Was ist in beiden? Was ist nur in a? Was ist in a oder b? Alles mit &, -, |
"""

pythonlist_a = ["AAPL", "MSFT", "TSLA", "NVDA"]
list_b = ["MSFT", "NVDA", "AMD", "CRWD"]

watchlist_1 = set(pythonlist_a)
watchlist_2 = set(list_b)

print(watchlist_1)
print(watchlist_2)

already_owned = watchlist_1 & watchlist_2 # Schnittmenge
to_research = watchlist_1 - watchlist_2   # Differenz
all_tickers = watchlist_1| watchlist_2 # Beide Listen zusammen


print(already_owned)
print(to_research)
print(all_tickers)
"""
Drill 2 – String split/strip/replace Pipeline:
pythonraw = "  AAPL ; 300.5 ; +12.8% \n MSFT;420.1 ;-3.2%  "
# Splitte an \n, dann an ;, strip jedes Feld, entferne % und + aus dem letzten Feld
# Ergebnis: [{"ticker": "AAPL", "price": 300.5, "change": 12.8}, {"ticker": "MSFT", "price": 420.1, "change": -3.2}]
"""
pythonraw = "  AAPL ; 300.5 ; +12.8% \n MSFT;420.1 ;-3.2%  "

result = []

# 1. Zeilen splitten
rows = pythonraw.split("\n")



for row in rows:
    # 2. aufräumen + splitten
    parts = row.strip().split(";")
    
    ticker = parts[0].strip()
    price = float(parts[1].strip())
    change = float(parts[2].strip().replace("%", ""))

    # 3. Dict bauen
    result.append({
        "ticker": ticker,
        "price": price,
        "change": change
    })

#print(result)




#Ergebnis: [{"ticker": "AAPL", "price": 300.5, "change": 12.8}, {"ticker": "MSFT", "price": 420.1, "change": -3.2}]



"""
Drill 3 – Funktion mit Default-Parametern:
python# Schreibe filter_stocks(stocks, min_price=0, max_price=99999, sector=None)
# Gibt alle Stocks zurück die zwischen min und max liegen
# Wenn sector angegeben, nur diesen Sektor
stocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech"},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare"},
    {"ticker": "NVDA", "price": 222, "sector": "Tech"},
]
# Teste: filter_stocks(stocks, min_price=200, sector="Tech") → AAPL, NVDA

"""
stocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech"},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare"},
    {"ticker": "NVDA", "price": 222, "sector": "Tech"},
]





def filter_stocks(stocks, min_price=0, max_price=99999, sector=None):
    zwischenliste = []
    for i in stocks:
        
        if i["price"] > min_price and i["price"] < max_price:
            if i["sector"] is not None:
                print(i["sector"])
                zwischenliste.append(i)
            #return i["ticker"]

    return zwischenliste



print(filter_stocks(stocks, min_price=200, sector="Tech"))






"""
Drill 4 – f-String Formatierung Kombi-Drill. Printe exakt diese Ausgabe:
AAPL         300.50€    +12.80%    UP
MSFT         420.12€     -3.28%    DOWN
TSLA         180.90€    +45.67%    UP
pythondata = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
]


"""

pythondata = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
]

for i,b,c in pythondata:
    d = ""
    if c > 0:
        d = "UP"
    else:
        d = "DOWN"
    print(f"{i:<12}{b:<10}{c:+,.2f}{d:>10}")


"""
# Ticker links 12, Preis rechts 10 mit .2f, Change rechts 10 mit Vorzeichen .2f, Status
Drill 5 – Alles zusammen: Schreibe ein Mini-Script ohne nachzuschauen:

Erstelle eine Liste von 4 Stock-Dictionaries (ticker, price, sector)
Filtere per List Comprehension alle Tech-Stocks
Berechne den Durchschnittspreis der gefilterten Stocks
Speichere das Ergebnis als JSON
Lies es wieder ein und printe formatiert mit f-String

Viel Spaß beim Tutorial-Bingen, und die 5 Drills wenn du Zeit hast.Opus 4.6 Medium

"""
import json

test_dic =[
    {"ticker": "test_1", "price": 100, "sector": "tech"},
    {"ticker": "test_2", "price": 200, "sector": "tech_2"},
    {"ticker": "test_3", "price": 300, "sector": "tech"},
    {"ticker": "test_4", "price": 400, "sector": "tech_4"},
]


list_clean = [x["price"] for x in test_dic if x["sector"] == "tech"]


list_clean_filter = [x for x in test_dic if x["sector"] == "tech"]

gesamt = 0
for i in list_clean: 
    gesamt += i  

gesamt_new = gesamt / len(list_clean)
print(gesamt_new)
    

print(list_clean)

print(list_clean_filter)
with open("test.json", "w") as f:
    json.dump(list_clean_filter, f)


# Also ich saß hier gefühlt zwei Stunden dran und bin noch nciht fertig :( )