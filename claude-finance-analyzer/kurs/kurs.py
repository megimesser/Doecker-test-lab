import yfinance as yf 
from importer.importer import importer, ticker_format


# python -m kurs.kurs -> 
kürzel = ticker_format(importer("finance.xlsx"))
#print(kürzel)



def finance_info(kürzel):
    test = kürzel
    return test

print(finance_info(kürzel))


#def Tickerinfo():
#test




#day = yf.Ticker("XXlkjölkjölk")
#print(day.info)
#print(day.history(period='1mo'))

#tickers = yf.Tickers('MSFT AAPL GOOG')
#yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')