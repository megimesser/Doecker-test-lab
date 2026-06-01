
"""

Identifizierte Schwachstellen und konzipierte gezielt fünf Übungsaufgaben
5 Drills – Tag 6
OOP Einstieg (du hast noch nie eine Klasse geschrieben)
Drill 1: Schreibe eine Klasse Stock mit __init__, einer Methode, und erstelle zwei Instanzen:

python
# Die Klasse soll ticker, buy_price und shares speichern
# Methode total_value() gibt buy_price * shares zurück
# Erstelle: stock1 = Stock("AAPL", 150, 10)
# Erstelle: stock2 = Stock("MSFT", 300, 5)
# Printe: stock1.ticker, stock2.total_value()
Drill 2: Erweitere deine Stock-Klasse um zwei Dinge:


"""
import math 



# In den Konstuktor gehören immer nur die
# Variablen welche beim erstellen der Klasse bekannt sind 
#  -> Profit ändert sich stänfig, dadurch muss es nicht innehralb der Konstruktors definiert werden 
## _ Buy Price 

class Stock: 
    def __init__(self, ticker,buy_price,shares,actual_price):
        self.ticker = ticker
        self.buy_price = buy_price
        self.shares = shares
        self.actual_price = actual_price
        #self.round = math.floor(actual_price) # test
        

    def total_value(self):
        
        return self.buy_price * self.shares
    

    def profit(self,act_price):
        self.act_price = act_price
        try: 
            return (self.act_price - self.buy_price) * self.shares
        except TypeError: 
            return "falscher Datentyp"
        

    # 2. __str__ Methode die "AAPL: 10 Shares @ 150€" zurückgibt
    # Maximal eine __str__ pro Klasse 

    def __str__(self):
        return f"{self.ticker}: {self.shares} Shares @ {self.buy_price}€"

    

    
"""
Test ohne __str __ 
    def profit(self):
        try:  
            if (self.actual_price - self.buy_price) * self.shares > 0: 
                return  "Gewinn:", (self.actual_price - self.buy_price) * self.shares
            elif (self.actual_price - self.buy_price) * self.shares > 0:
                return "Verlust:", (self.actual_price - self.buy_price) * self.shares 
        except ZeroDivisionError:
            return "ich bin eine Biene"
        except ValueError:
            return print("test")
        except TypeError:
            return print("falscher Datentyp")
        pass
"""

# Test mit __str__ 


    

 





stock1 = Stock("AAPL", 150, 10,200)
stock2 = Stock ("MSFT",300,5,340.3)
stock3 = Stock("AAPL",20,30,"test") # Exceptblocktest

#print(stock1.total_value())
#print(stock2.total_value())
#print(stock1.ticker)

print(stock1.profit(300))
print(stock3.profit(100))


# Offene Fragen zu OOP 
# Gibt es eine Formalität wie man innerhalb des Konstruktors nach best Practice Variablen definiert ? 
# Frage weil bspw. können Variablen auch über mehrere Schritte mit try Exceptblock definiert werden.
# Ist mir aufgefallen weil ich eine neue Variable aus zwei bestehenden definiert habe und dadurch einen TypeError generiert habe. 

# Wann macht es Sinn wie Variablen vergeben werden ? 
# Innerhalb deines Beispiels muss man die Variable über den Aufruf der Method als Parameter mitgeben ? 
#Diese muss dann nicht im Konstruktor definiert sein und wird dadruch auch nicht an andere methods vererbt ? 
#Mir hat innerhalb deines Beispiels nämlich der actual price gefehlt wodurch ich ihn selbst als variable defineirt habe 
"""



python
# 1. Methode profit(current_price) die (current - buy) * shares zurückgibt

# Teste: print(stock1) soll den formatierten String ausgeben
# Teste: print(stock1.profit(300)) soll 1500 ausgeben




Filter-Logik mit bedingter Prüfung (dein Fehler von gestern)
Drill 3: Schreibe filter_stocks nochmal, diesmal korrekt. Der Sector-Filter soll nur greifen wenn ein Sector übergeben wird:

python
stocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech"},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare"},
    {"ticker": "NVDA", "price": 222, "sector": "Tech"},
    {"ticker": "JPM", "price": 190, "sector": "Finance"},
]

# filter_stocks(stocks, min_price=200) → AAPL, NVDA, kein Sector-Filter
# filter_stocks(stocks, sector="Tech") → AAPL, NVDA, kein Preis-Filter
# filter_stocks(stocks, min_price=200, sector="Tech") → AAPL, NVDA
# filter_stocks(stocks) → alle 4
f-String Ausrichtung (muss endlich sitzen)


"""
stocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech"},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare"},
    {"ticker": "NVDA", "price": 222, "sector": "Tech"},
    {"ticker": "JPM", "price": 190, "sector": "Finance"},
    {"ticker": "JPM", "price": 190, "sector": "Tech"}, # Zum testen der dritten if else schleife
]

def filter_stocks(stocks, min_price = 0, sector = None):
    if sector == None and min_price == 0:
        f = [x for x in stocks]
    elif min_price > 0:
       f =  [x for x in stocks if x["price"] > min_price]
    elif sector != None: 
        f =  [x for x in stocks if x["sector"] == sector]
    elif sector != None and min_price > 0: 
        f = [x for x in stocks if x["sector"] == sector and x["price"] > min_price]
    return f
    

    """
    for i in stocks: 
        try: 
            if i["price"] > min_price:
                return f"{i}"
        except TypeError:
            print("falscher Datentyp")
    """

#print(filter_stocks(stocks, min_price=200))
#print(filter_stocks(stocks, sector="Tech"))
#print(filter_stocks(stocks, min_price=200, sector="Tech") )
print(filter_stocks(stocks))


"""

# Wichtig bitte merken - formuliere mir bitte immer neue aufgaben und diese vollständig ! ich habe nicht immer zugriff auf die alten dateien von gestern 


Drill 4: Printe exakt diese Tabelle. Aus dem Kopf, kein Nachschauen:

Ticker      Kurs         Change     Status
--------------------------------------------
AAPL      300.50€       +12.80%     GEWINN
MSFT      420.12€        -3.28%     VERLUST
TSLA      180.90€       +45.67%     GEWINN
NVDA      222.32€        -8.12%     VERLUST
python
data = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
    ("NVDA", 222.32, -8.123),
]
# Header manuell printen, dann Loop
# Ticker links 10, Kurs rechts 10 mit .2f, Change rechts 12 mit Vorzeichen .2f, Status
Alles zusammen

"""

data = [
    ("AAPL", 300.5, 12.8),
    ("MSFT", 420.123, -3.275),
    ("TSLA", 180.9, 45.67),
    ("NVDA", 222.32, -8.123),
]

ticker = "Ticker"
kurs="Kurs"
status="Status"
change="Change"


print(f"{ticker:<10}{kurs:<10}{change:>10}{status:>10}")
print("--------------------------------------------")
for x,y,z in data:
    f = None
    if z > 0:
        f = "GEWINN"
    else:
        f = "VERLUST"

   
    print(f"{x:<10}{y:<10}{z:>10}%{f:>10}"

    )




"""





Drill 5: Baue ein Mini-Script ohne nachzuschauen, das alles kombiniert:

Erstelle 4 Stock-Objekte mit deiner Klasse aus Drill 1
Packe sie in eine Liste
Filtere per List Comprehension alle mit total_value() über 2000


Für jeden gefilterten Stock: berechne Profit mit current_price 300




# Die hier mache ich nichtmehr - hat genau 2 stunden gedauert und ich habe lediglich 1 mal bei der erste nOOP aufgabe gegoogelt :) 
Printe eine formatierte Tabelle mit Ticker, Total Value, Profit
Speichere die Ergebnisse als Liste von Dictionaries in eine JSON-Datei
Timer: 30 Minuten. Bei OOP nicht frustriert sein wenn es beim ersten Mal nicht klappt – das ist komplett neues Terrain für dich.

"""


stock_5_1 = Stock("AAPL", 150, 30,200)
stock_5_2 = Stock("AAPL", 0, 1,200)
stock_5_3 = Stock("AAPL", 0, 3,-100)
stock_5_4 = Stock("AAPL", 2100, 10,300)


test_3 = [stock_5_1,stock_5_2,stock_5_3,stock_5_4]
test = [stock_5_1.total_value(),stock_5_2.total_value(),stock_5_3.total_value(),stock_5_4.total_value()]


test_2 = [ x.profit(300) for x in test_3 if x.total_value() > 2000]
print(test_2)


#test_4 = [f.profit(300) for f in test_2]

# HIer müsste das Objekt zurückgegeben werden 


#print(test)
#test = stock_5_1.profit(200)
#print(type(test))




