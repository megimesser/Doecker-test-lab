"""


Deine 5 Aufgaben für morgen
Drill 1 – OOP: Klasse Portfolio Schreibe eine Klasse Portfolio die Stock-Objekte verwaltet:
python# __init__ erstellt eine leere Liste self.stocks
# Methode add(stock) fügt einen Stock hinzu
# Methode total_value() summiert total_value() aller Stocks
# Methode best_performer(current_prices) findet den Stock mit dem höchsten Profit
#   current_prices ist ein Dictionary: {"AAPL": 300, "MSFT": 420}
#   Tipp: max() mit key-Parameter

# Teste:
# p = Portfolio()
# p.add(Stock("AAPL", 150, 10))
# p.add(Stock("MSFT", 300, 5))
# p.add(Stock("TSLA", 200, 8))
# print(p.total_value())
# print(p.best_performer({"AAPL": 300, "MSFT": 420, "TSLA": 180}))
Drill 2 – Filter als einzeilige List Comprehension mit kombinierter Bedingung: Gegeben:
pythonstocks = [
    {"ticker": "AAPL", "price": 300, "sector": "Tech", "dividend": True},
    {"ticker": "JNJ", "price": 155, "sector": "Healthcare", "dividend": True},
    {"ticker": "TSLA", "price": 410, "sector": "Auto", "dividend": False},
    {"ticker": "NVDA", "price": 222, "sector": "Tech", "dividend": False},
    {"ticker": "MSFT", "price": 420, "sector": "Tech", "dividend": True},
]
# Filtere: Tech-Aktien über 250€ die Dividende zahlen. Eine Zeile.
# Ergebnis: AAPL, MSFT
Drill 3 – JSON Read-Modify-Write mit Klasse: Schreibe ein Script das:
python# 1. Erstelle 3 Stock-Objekte
# 2. Speichere sie als Liste von Dictionaries in stocks.json
#    Tipp: Du brauchst ein Dict pro Stock: {"ticker": s.ticker, "buy_price": s.buy_price, "shares": s.shares}
# 3. Lies stocks.json wieder ein
# 4. Füge jedem Dict ein Feld "current_value" hinzu (shares * 300 als Dummy-Preis)
# 5. Schreibe die geänderte Version zurück
Drill 4 – f-String Formatierung Drill (10 Mal abtippen):
python# Tippe diese Zeile 10 Mal aus dem Kopf:
print(f"{'AAPL':<10}{'300.50':>10}{'€'} {'+12.80':>10}{'%'}")

# Dann mit Variablen und echtem Format-Spec:
t, p, c = "AAPL", 300.5, 12.8
print(f"{t:<10}{p:>10.2f}€ {c:>+10.2f}%")
Drill 5 – Fehler finden: Finde und fixe alle Fehler in diesem Code (es sind 5):
pythonclass portfolio:
    def __init__(self):
        stocks = []

    def add(self, stock)
        self.stocks.append(stock)

    def total(self):
        total = 0
        for stock in self.stocks
            total += stock.total_value
        return total

    def save(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.stocks, f)

    def __str__(self):
        return f"Portfolio mit {len(self.stocks} Stocks"


"""