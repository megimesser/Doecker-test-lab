import yfinance as yf 
from importer.importer import ticker_format, importer

d = ticker_format(importer())
print(d)


#def Tickerinfo():




#day = yf.Ticker("XXlkjölkjölk")
#print(day.info)
#print(day.history(period='1mo'))

#tickers = yf.Tickers('MSFT AAPL GOOG')
#yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')