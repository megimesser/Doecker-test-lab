"""

5 Aufgaben – Tag 9
Wiederholung der Schwachstellen von gestern plus eine neue Sache.
Drill 1 – Profit mit korrektem Vorzeichen (gestern vertauscht):
pythonclass Stock:
    # __init__(ticker, buy_price, shares)
    # profit(current_price) → MUSS (current - buy) * shares sein
    # Bei Stock("AAPL", 150, 10).profit(200) → +500 (nicht -500)
    pass

    
"""


class Stock:
    def __init__(self,ticker,buy,share):
        self.share = share
        self.buy = buy 
        self.ticker = ticker

    def profit(self,current_price):
          return (current_price - self.buy)* self.share
         
    

class Profit:
    def __init__(self):
        self.list = []
    
    def add(self,stock):
        self.list.append(stock)
    
    def profit(self,current_price):
          return (current_price - stock.buy)* stock.shares
         
    
s = Stock("AAPL", 150, 10)
#print(s.profit(200))   # +500
#print(s.profit(100))   # -500




"""



# Teste:
s = Stock("AAPL", 150, 10)
print(s.profit(200))   # +500
print(s.profit(100))   # -500





Drill 2 – Filtern mit in statt Regex (gestern Regex-Bug):
pythonmails = [
    {"sender": "test@x.com", "subject": "[TEST] Rechnung", "has_pdf": True},
    {"sender": "spam@y.com", "subject": "Angebot", "has_pdf": False},
    {"sender": "test@x.com", "subject": "[TEST] Report", "has_pdf": True},
    {"sender": "info@z.de", "subject": "[TEST] Leer", "has_pdf": False},
]
# Filtere per List Comprehension: "[TEST]" im Subject UND has_pdf True
# Nutze "in", kein Regex
# Ergebnis: die zwei Mails mit [TEST] und PDF

"""

pythonmails = [
    {"sender": "test@x.com", "subject": "[TEST] Rechnung", "has_pdf": True},
    {"sender": "spam@y.com", "subject": "Angebot", "has_pdf": False},
    {"sender": "test@x.com", "subject": "[TEST] Report", "has_pdf": True},
    {"sender": "info@z.de", "subject": "[TEST] Leer", "has_pdf": False},
]


l = [l for l in pythonmails if "[TEST]" in l["subject"] and l["has_pdf"] is True]

#print(l)







"""




Drill 3 – Merge ohne zweiten Loop (gestern zweiter Loop benutzt):
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}, "TSLA": {"shares": 8}}
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}
# Füge jedem Eintrag "price" und "value" (shares * price) hinzu
# OHNE zweiten Loop — nutze direkten Key-Zugriff: prices[ticker]
# Ergebnis: {"AAPL": {"shares": 10, "price": 300, "value": 3000}, ...}



"""
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}, "TSLA": {"shares": 8}}
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}


#print()

test = pythonportfolio.copy()


#Das ist ist "hartes Brot" - ich verstehe nicht auf anhieb was das Ding macht und musst erstmal selbst dahinter steigen 

#iteration durch ein kopiertes Dic 
for ticker, info in test.items():
     #zuweisung der Variable "preis" welche durch die Iteration der Ticker welcher als Key für prices agiert immer einen anderen wert zurückgibt 
     preis = prices[ticker]
     #zuweisung - zugriff auf value des Dictionarys - der Wert aus orices ist der neue Wert innerhalb von pythonportfolio 
     info["price"] = preis
     #zuweisung neuer wert info.value
     info["value"] = preis * info["shares"]

#print(pythonportfolio)
     
 




"""


Drill 4 – max() und min() auf Objekten (neue Kombination):
pythonclass Stock:
    def __init__(self, ticker, buy_price, shares):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares

    def profit(self, current):
        return (current - self.buy_price) * self.shares

stocks = [
    Stock("AAPL", 150, 10),
    Stock("MSFT", 300, 5),
    Stock("TSLA", 200, 8),
]
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}

# Finde das Stock-OBJEKT mit dem höchsten Profit
# best = max(stocks, key=lambda s: s.profit(prices[s.ticker]))
# Printe best.ticker
Das ist max() mit key auf Objekten statt auf Dictionaries – dein best_performer aus der Portfolio-Klasse, isoliert geübt.


"""

class Stock:
    def __init__(self): #ticker, buy_price, shares):
        #self.ticker = ticker
        #self.buy_price = buy_price
        #self.shares = shares
        self.stocklist = []

    def profit(self, current):
        return (current - self.buy_price) * self.shares
    
    def test(self):
        print("test")
    
    def add(self,ticker,price,share):
        self.ticker = ticker
        self.buy_price = price
        self.shares = share
        # Wenn man das dic = {ticker,price,share} nutzt entsteht ein ungeordnetes Set und keine Dictionary
        dic = {"ticker" : self.ticker , "price": self.buy_price , "share" : self.shares}
        self.stocklist.append(dic)

    def profit_2(self, prices): # -> Die hier habe ich mit ki geschribeben , kam nicht darauf 
        self.prices = prices

        for stock in self.stocklist:
            ticker = stock["ticker"]

            if ticker in self.prices:
                current = self.prices[ticker]

                profit = (current - self.buy_price) * self.shares

                stock["profit"] = profit   # 👈 hier wird der Value hinzugefügt
                print(stock)
                        
                    
    
    def max(self):
        best = max(self.stocklist, key=lambda s: s["profit"])
        return best



                    
                    


           
            #print(prices)
            
            #print(i)

#Ich weiß gerade nicht weiter 
# ich versuche folgendes 
# Ich breche das Problem herunter auf seine einzelnen Schritte 
####

# Was ist das Endergebnis ? 
#Stockobjekt mit höchsten Profit 
# Was ist der Anspruch - ich möchte alles als OOP lösen ohne Kombination mit Fuktionen > ich weiß dass das nicht die aufgabe ist - ist aber schwerer als Übung als das 
#ganze mit einer Lambda funktion zu machen 

# Was ist der Erste Schritt - eine liste von allen Stockobjekten erstellen 
# 2 : der liste den profit hinzufügen 
# 3 : die list filtern nach dem höchsten Stock objekt 


s = Stock()
s.add("AAPL", 150, 10)
s.add("MSFT", 300, 5)
s.add("TSLA", 200, 8)

prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}
l = s.profit_2(prices)


x = s.max()
print(x, "bester Ticker")
"""
stocks = [
    Stock("AAPL", 150, 10),
    Stock("MSFT", 300, 5),
    Stock("TSLA", 200, 8),
]
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}




# Finde das Stock-OBJEKT mit dem höchsten Profit
# best = max(stocks, key=lambda s: s.profit(prices[s.ticker]))
# Printe best.ticker
#Das ist max() mit key auf Objekten statt auf Dictionaries – dein best_performer aus der Portfolio-Klasse, isoliert geübt.














Drill 5 – Komplette Pipeline mit Klasse (Festigung):
python# 1. Stock-Klasse: __init__(ticker, buy_price, shares), total_value(), to_dict()
#    to_dict() gibt {"ticker": ..., "buy_price": ..., "shares": ..., "total": ...} zurück
# 2. Erstelle 4 Stocks
# 3. Filtere per List Comprehension alle mit total_value() > 1500
# 4. Wandle die gefilterten mit to_dict() in Dictionaries um (List Comprehension)
# 5. Speichere als JSON
# 6. Lies ein und printe jeden als "TICKER: TOTAL€"
Der neue Teil ist to_dict() – eine Methode die das Objekt in ein Dictionary umwandelt. Das brauchst du ständig, weil du Objekte nicht direkt als JSON speichern kannst, nur Dictionaries. Genau das Problem hattest du beim Finance-Analyzer.
Timer 7 Minuten pro Drill. Poste wenn du durch bist.


"""


stocks = [
    {"name": "test_1", "buy": 20, "share": 5},
    {"name": "test_2", "buy": 50, "share": 5},
    {"name": "test_3", "buy": 1000, "share": 5},
]


class Stock:
    def __init__(self,ticker,buy_price,shares):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares 
        self.list = []

    def total_value(self):
        l = [x for x in ] 

    def add(self):
        

# Ich bin gerade geistig ausgestiegen - mache für heute schluss 