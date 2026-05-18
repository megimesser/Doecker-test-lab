import yfinance as yf 
from importer.importer import importer, ticker_format


# python -m kurs.kurs -> 
kürzel = ticker_format(importer("finance.xlsx"))
#print(kürzel)


"""
def finance_info(kürzel):
    analyse_list = []
    test = kürzel
    for i in kürzel:


    return analyse_list


"""
    




#def Tickerinfo():
#test




dat = yf.Ticker("AAPL")
print(dat.info)
print(dat.history(period='1mo'))

#tickers = yf.Tickers('MSFT AAPL GOOG')
#yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')

ticker = yf.Ticker("AAPL")
info = ticker.info

relevant = {
    "name": info.get("shortName"),
    "sector": info.get("sector"),
    "current_price": info.get("currentPrice"),
    "52w_high": info.get("fiftyTwoWeekHigh"),
    "52w_low": info.get("fiftyTwoWeekLow"),
    "pe_ratio": info.get("trailingPE"),
    "dividend_yield": info.get("dividendYield"),
    "recommendation": info.get("recommendationKey"),
    "analyst_target": info.get("targetMeanPrice"),
    "beta": info.get("beta"),
    "market_cap": info.get("marketCap"),
}

print(relevant)