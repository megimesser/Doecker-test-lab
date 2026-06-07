"""

5 Aufgaben – Tag 8
Keine f-String-Drills, du hast recht dass die dich nicht weiterbringen. Fokus auf das was du im Projekt tatsächlich brauchst.
Drill 1 – Komposition festigen (lief gestern gut, einmal wiederholen):
python# Schreibe Stock und Portfolio aus dem Kopf:
# Stock: __init__(ticker, buy_price, shares), total_value(), profit(current_price)
# Portfolio: __init__(), add(stock), total_value()
#

"""


class Stock:
    def __init__(self, ticker,buy_price,shares):
        self.ticker = ticker
        self.buy_price=buy_price
        self.shares = shares

    def total_value(self):
        return self.buy_price * self.shares 

    def profit(self,current_price):
        profit = 0 
        profit = (self.buy_price - current_price) * self.shares
        return profit 

       

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add(self,stock):
        self.stocks.append(stock)
    
    def total_value(self):
        total = 0
        for stock in self.stocks:
            total += stock.shares * stock.buy_price

            print(stock.ticker)
            print(stock.shares)
            print(stock.buy_price)
        return total
         
         #total += i[1] * i[0]
        #return total
#ich kann mir das konzept hier nicht merken 
# ich habe versucht mit x,y,z in tuple durch den tuple zu loopen mit einem verschachtelten for loop welcher widerrum durch den Array loopt 


# Ok meine Erkenntnis an dieser Stelle : 
# Es wird das gesammte Stockobjekt zum Array hinzugefügt nicht nur ein einzelner wert bzw ein tupple dadurch kann man innerhalb von Profit auch auf stock.ticker zugreifen,
#weil dieser innnerhalb das Objekts vorhanden ist - verstanden - können kann ich es aber trotzdem noch nicht - ich brauche noch ein paar Aufgaben um das zu verinerlichen 
        #return 


# Teste:
p = Portfolio()
s = Stock("AAPL", 150, 10)

p.add(Stock("AAPL", 150, 10))
p.add(Stock("MSFT", 300, 5))
print(p.total_value())


print(s.profit(200))
print(s.total_value())



"""




# Teste:
# p = Portfolio()
# p.add(Stock("AAPL", 150, 10))
# p.add(Stock("MSFT", 300, 5))
# print(p.total_value())    → 3000




Drill 2 – max() mit key (gestern fast, heute sauber):
pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": 250},
    {"ticker": "NVDA", "profit": 3200},
]
# Finde das DICTIONARY mit dem höchsten Profit (nicht nur den Wert):
# best = max(stocks, key=lambda s: s["profit"])
# Ergebnis soll sein: {"ticker": "NVDA", "profit": 3200}
Gestern hast du max() auf das Ticker-Feld angewendet statt auf profit. Heute: nach profit, und das ganze Dictionary zurückgeben.


"""

# Lambda ist eine Kurzschreibweise für eine anonyme funktion also wie bspw. ein Dictionarycomprehension oder 
# dabei hat Lambda immer ein automatisches returnstatement 

pythonstocks = [
    {"ticker": "AAPL", "profit": 1500},
    {"ticker": "MSFT", "profit": 250},
    {"ticker": "NVDA", "profit": 3200},
]

best = max(pythonstocks, key=lambda s: s["profit"])
print(best)






"""







Drill 3 – Praxisnah: Gmail-Daten verarbeiten. Gegeben ist eine Liste von Mail-Dictionaries wie sie deine API liefert:
pythonmails = [
    {"sender": "test@example.com", "subject": "[TEST] Rechnung", "has_pdf": True},
    {"sender": "newsletter@spam.com", "subject": "Angebot", "has_pdf": False},
    {"sender": "test@example.com", "subject": "[TEST] Report", "has_pdf": True},
    {"sender": "info@firma.de", "subject": "Bestätigung", "has_pdf": False},
]
# Filtere per List Comprehension alle Mails die "[TEST]" im Subject haben UND ein PDF enthalten
# Ergebnis: die zwei [TEST]-Mails mit PDF
Drill 4 – Dictionary aus zwei Datenquellen mergen (dein Merger-Thema):
pythonportfolio = {"AAPL": {"shares": 10}, "MSFT": {"shares": 5}, "TSLA": {"shares": 8}}
prices = {"AAPL": 300, "MSFT": 420, "TSLA": 180}
# Füge jedem Portfolio-Eintrag den aktuellen Preis hinzu, ohne zweiten Loop
# Berechne zusätzlich "value" = shares * price
# Ergebnis: {"AAPL": {"shares": 10, "price": 300, "value": 3000}, ...}
Drill 5 – Mini-Pipeline mit JSON (ohne nachschauen):
python# 1. Erstelle eine Liste von 3 Dictionaries (ticker, shares, buy_price)
# 2. Berechne für jedes den total_value (shares * buy_price), schreib ihn direkt ins Dictionary
# 3. Filtere per List Comprehension alle mit total_value > 1000
# 4. Speichere die gefilterten als JSON in eine Datei
# 5. Lies die Datei wieder ein und printe jeden Eintrag als "TICKER: VALUE€"
Timer 7 Minuten pro Drill. Steckst du fest, nachschauen, morgen nochmal. Poste deine Lösungen wenn du durch bist.

"""