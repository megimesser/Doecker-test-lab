
"""
5 Aufgaben – Tag 10
Heute mit OOP-Schwerpunkt, weil das dein aktuelles Lernthema ist. Eine neue Sache dabei: Vererbung.
Drill 1 – to_dict() Methode (gestern nicht geschafft, heute der Fokus):
pythonclass Stock:
    # __init__(ticker, buy_price, shares)
    # total_value() → buy_price * shares
    # to_dict() → gibt ein Dictionary zurück mit allen Werten PLUS total
    #   {"ticker": ..., "buy_price": ..., "shares": ..., "total": ...}

# Teste:
# s = Stock("AAPL", 150, 10)
# print(s.to_dict())
# → {"ticker": "AAPL", "buy_price": 150, "shares": 10, "total": 1500}

"""


class Stock:
    def __init__(self,ticker,buy_price,shares):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares

    def total_value(self):
        self.total = self.shares* self.buy_price
        

    def dict(self):
        x = {
            "ticker": self.ticker,
            "buy_price": self.buy_price,
            "shares": self.shares,
            "total": self.total
        }
        return x
    
    def profit(self, stocks, prices):
        self.stocks = stocks

        pass
    

s = Stock("AAPL", 150, 10)
f = Stock("BBL", 250, 10)
s.total_value()
f.total_value()
s.dict()
print(f.dict())
print(s.dict())

pythonstocks = [
    Stock("AAPL", 150, 10),
    Stock("MSFT", 300, 5),
    Stock("TSLA", 200, 8),
]
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}


# Variablen welche innerhalb von Loops geändert werden, müssen außerhalb des loops stehen 
highest_ticker = ""
highest_value = 0

test_dic = {}

for i in pythonstocks:
    #print(prices[i.ticker]) 
    


    price =  prices[i.ticker] #### - ist das hier etwa eun Dictionary lookup ? :D 
    endval = (price - i.buy_price) * i.shares
    test_dic 


    if highest_value < endval:
        highest_value = endval 
        highest_ticker = i.ticker
    


    #print(i.ticker, endval)
print(highest_ticker, highest_value)

    


    #print(i.ticker)




#best = max(pythonstocks, key=lambda s: s.profit(prices[s.ticker]))

# Ich habe es erstmal nicht mit max gemacht - verstehe die funktion  wenn man es mit max machen wöllte würde ich vorhab ein Dicitonary bauen - mach ich jetzt mal 


"""

Drill 2 – max() mit Lambda, die einfache Version (gestern überkompliziert):
pythonstocks = [
    Stock("AAPL", 150, 10),
    Stock("MSFT", 300, 5),
    Stock("TSLA", 200, 8),
]
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}

# Finde das Stock-Objekt mit dem höchsten Profit – EINE ZEILE
# best = max(stocks, key=lambda s: s.profit(prices[s.ticker]))
# print(best.ticker)
Diesmal genau so, eine Zeile mit Lambda. Nicht in eine Klasse packen. Übe die einfache Lösung.


"""

pythonstocks = [
    Stock("AAPL", 150, 10),
    Stock("MSFT", 300, 5),
    Stock("TSLA", 200, 8),
]
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}





#best = max(pythonstocks, key=lambda s: s.profit(prices[s.ticker]))
#print(best.ticker)

# Ich verstehe hier ein paar Dinge grundsätzlich nicht - 
# muss ich erst ein stockobjekt erstellen ? s.profit existiert nicht, weil ich keinen gegenwert habe also einen aktuellen marktpreis usw 


"""





Drill 3 – Vererbung (neues Konzept):
python# Elternklasse Asset mit __init__(name) und einer Methode describe() die "Asset: {name}" zurückgibt
# Kindklasse Stock(Asset) mit __init__(name, price)
#   - super().__init__(name) aufrufen
#   - eigenes Attribut self.price
#   - describe() überschreiben: "Stock: {name} @ {price}€"

# Teste:
# a = Asset("Gold")
# s = Stock("AAPL", 300)
# print(a.describe())   # Asset: Gold
# print(s.describe())   # Stock: AAPL @ 300€





Drill 4 – from_dict() als classmethod (Gegenstück zu to_dict):
pythonclass Stock:
    def __init__(self, ticker, buy_price, shares):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares

    @classmethod
    def from_dict(cls, data):
        # erstelle ein Stock-Objekt aus einem Dictionary
        # return cls(...)
        pass

# Teste:
# data = {"ticker": "AAPL", "buy_price": 150, "shares": 10}
# s = Stock.from_dict(data)
# print(s.ticker)   # AAPL





Drill 5 – Komplette Pipeline mit to_dict und from_dict:
python# 1. Stock-Klasse mit __init__, total_value(), to_dict(), from_dict() (classmethod)
# 2. Erstelle 3 Stock-Objekte
# 3. Wandle sie per List Comprehension in Dictionaries um: [s.to_dict() for s in stocks]
# 4. Speichere als JSON
# 5. Lies die JSON wieder ein
# 6. Wandle die Dictionaries zurück in Stock-Objekte: [Stock.from_dict(d) for d in data]
# 7. Printe jeden als "TICKER: TOTAL€"
Drill 5 schließt den Kreis: Objekte → Dictionaries → JSON → Dictionaries → Objekte. Das ist genau das Pattern das du beim Finance-Analyzer gebraucht hättest. Wenn du das kannst, hast du das Serialisierungs-Problem für immer gelöst.
Timer 7 Minuten pro Drill. Bei Vererbung (Drill 3) ruhig kurz in die OOP-Übersicht schauen, das ist neu.
"""