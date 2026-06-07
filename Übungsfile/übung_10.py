
"""
Zusammenfassung Tag 7
OOP-Grundlagen verstanden und angewendet – erster Versuch, funktioniert. List Comprehension mit drei Bedingungen korrekt. JSON Read-Modify-Write sitzt. Hauptschwächen: Komposition (Klassen die andere Klassen nutzen), is vs ==, self. vergessen, Methodenaufruf vs Referenz.
5 Aufgaben für morgen
Drill 1 – Komposition: Portfolio mit Stock-Objekten. Schreibe beide Klassen komplett aus dem Kopf und lass sie zusammenarbeiten:
python# Stock: __init__(ticker, buy_price, shares), total_value(), profit(current_price), __str__
# Portfolio: __init__(), add(stock), total_value(), best_performer(current_prices)
#

"""


class Test:
    def __init__(self,test):
        self.test = test 
    


class Test_2:
    def __init__(self):
        self.test_2 = []

    def add(self,testi):
        self.test_2.append(testi)
        
        return self.test_2



p = Test_2()

# Wird von innen nach außen gelesen -> erst der Konstruktoraufruf durch Test und anschließend der Methodenaufruf durch .add
print(p.add(Test(200)))
print(p.test_2[0].test)   # 200

# Stock: __init__(ticker, buy_price, shares), total_value(), profit(current_price), __str__

class Stock:
    def __init__(self,ticker,buy_price,shares):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares

    def value(self):
        return self.buy_price * self.shares
    
    def profit(self,current_price):
        return self.shares * (current_price - self.buy_price)

    
        



    
        
# Portfolio: __init__(), add(stock), total_value(), best_performer(current_prices)
# 
class Portfolio: 
    def __init__(self):
        self.stock = []

    def add(self,stock):
        self.stock.append(stock)
    
    def total_value(self):
        return sum([i.shares * i.buy_price for i in self.stock])
    
    def best_performers(self, current_prices):
        # Dictionarys müssen vordefiniert sein
        best_performer = {
        "ticker": "",
        "value": float("-inf")
    }

        for i in self.stock:
            for x, y in current_prices.items():
             if i.ticker == x:
                f = y - i.buy_price

                if f > best_performer["value"]:
                    best_performer = {
                        "ticker": x,
                        "value": f
                    }

        return best_performer

        
    
        

        #return self.stock

p = Portfolio()

p.add(Stock("test",20,10))
p.add(Stock("AAPL", 150, 10))
p.add(Stock("MSFT", 300, 5))
p.add(Stock("TSLA", 200, 8))

s = Stock("AAPL", 150, 10)
print(s.profit(200))
#zugriff auf die variable von stock
print(p.stock[0].ticker)



print(p.total_value())                                      
print(p.best_performers({"AAPL": 300, "MSFT": 3500, "TSLA": 180, "Test":3000})) 


"""
class Portfolio:
    def __init__(self):#ticker, buy_price, shares):
        #self.ticker = ticker
        #self.buy_price = buy_price
        #self.shares = shares
        self.stocks = []

    def total_value(self):
        try:
            total_value = self.buy_price * self.shares
            return total_value
        except ValueError:
            print("Datentyp ist falsch")

    def add(self,Stock):
        try:
            self.stocks.append(Stock)
        except TypeError:
            print("Datentyp falsch")
 


p = Portfolio()
p.add(Stock("AAPL", 150, 10))
p.add(Stock("MSFT", 300, 5))
p.add(Stock("TSLA", 200, 8))


"""
"""


# Erstelle:
# p = Portfolio()
# p.add(Stock("AAPL", 150, 10))
# p.add(Stock("MSFT", 300, 5))
# p.add(Stock("TSLA", 200, 8))
# print(p.total_value())                                        → 4100
# print(p.best_performer({"AAPL": 300, "MSFT": 350, "TSLA": 180}))  → AAPL (Profit 1500)
Drill 2 – max() mit key-Parameter (neues Konzept):
pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": 250},
    {"ticker": "TSLA", "profit": -160},
    {"ticker": "NVDA", "profit": 3200},
]
# Finde den Stock mit dem höchsten Profit. Eine Zeile mit max().
# Finde den Stock mit dem niedrigsten Profit. Eine Zeile mit min().
# Finde den Stock mit dem längsten Ticker-Namen. Eine Zeile mit max().
Hinweis zur Syntax: max(liste, key=lambda x: x["feld"]) gibt das Element zurück bei dem x["feld"] am größten ist.

"""
pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": 250},
    {"ticker": "TSLA", "profit": -160},
    {"ticker": "NVDAS", "profit": 3200},
]


x = max([i["profit"] for i in pythonstocks])
f = min([i["profit"] for i in pythonstocks])
best = max(pythonstocks, key=lambda i: i["ticker"])
print(best)
print(x)
print(f)









"""





Drill 3 – self. vergessen erkennen. Fixe alle Fehler:
pythonclass Analyzer:


"""
class test:
    def __init__(self, name):
        self.name = name
        self.results = []

    def add_result(self, value):
        self.results.append(value)

    def average(self):
        total = 0
        for r in self.results:
            total += r
        return total / len(self.results)

    def summary(self):
        return f"{self.name}: {len(self.results)} Ergebnisse, Schnitt {self.average():.2f}"

"""



Drill 4 – f-String Drill (diesmal wirklich abtippen). Printe exakt diese Tabelle:
Name           Gehalt      Bonus   Gesamt
----------------------------------------------
Müller      3,850.00€   +385.00€  4,235.00€
Schmidt     5,200.00€   +520.00€  5,720.00€
Weber       2,900.00€   +290.00€  3,190.00€
pythondata = [
    ("Müller", 3850),
    ("Schmidt", 5200),
    ("Weber", 2900),
]
# Bonus = 10% vom Gehalt, Gesamt = Gehalt + Bonus
# Name links 12, Gehalt rechts 12 mit Tausendertrenner und .2f
# Bonus rechts 10 mit Vorzeichen und .2f, Gesamt rechts 12

Nä diese f string aufgaben bringen nichts weil ich sie innerhalb der praxis nie verwende 

"""
"""


Drill 5 – Alles zusammen ohne nachschauen:
python# 1. Erstelle Stock-Klasse und Portfolio-Klasse aus dem Kopf
# 2. Erstelle 4 Stocks, füge sie zum Portfolio hinzu
# 3. Filtere per List Comprehension alle Stocks mit total_value > 2000
# 4. Finde den best_performer mit current_prices {"AAPL": 300, "MSFT": 420, "TSLA": 180, "NVDA": 250}
# 5. Speichere die gefilterten Stocks als JSON (Dict pro Stock)
# 6. Printe eine formatierte Tabelle der gefilterten Stocks

"""


stocks = [
    {"name":"test", "value": 200},
    {"name":"test_2", "value": 300},
    {"name":"test_3", "value": 400},
]
    



import json
stock_2 = {"AAPL": 300, "MSFT": 420, "TSLA": 180, "NVDA": 250}

class stock:
    def __init__(self):
        self.stock = []
    
    def filter(self, stocks):
        self.stock.append(stocks)
        return self.stock


class Portfolio:
    def __init__(self):
        self.stock = []

    def add_new(self,stocks):
        self.stock.append()

    def best_perf(self,stocks):
        best_perf = 0
        best_perf_n = ""
        for key,value in stocks.items():
            if value > best_perf:
                best_perf = value
                best_perf_n = key
        return best_perf_n, best_perf
    
    # ich probiere es mal mit einer Dicitonarycomporehension 
    #def best_perf_2(self,stocks):
       # max({k2: v1 for k2, v1 in stocks})

    def json_safer(self):
        with open("test.json", "w") as f:
            json.dump(self.stock, f, indent=4)

    def printer(self):
        pass
        


p = Portfolio()
k = stock()
x = p.best_perf(stock_2)
print(x)

#f= p.best_perf_2(stock_2)
print(f)

ll = k.filter(stocks)

print(ll)