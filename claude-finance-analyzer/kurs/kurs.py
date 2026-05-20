import yfinance as yf 
from importer.importer import importer, ticker_format
import json 

# python -m kurs.kurs -> 
kürzel = ticker_format(importer("finance.xlsx"))
#print(kürzel)


# Exception einbauen, falls die Aktie nicht gefunden wird 
def finance_info(kürzel):
    global analyse_list
    analyse_list = []
    for i in kürzel:
        ticker = yf.Ticker(i)
        hist = ticker.history(period='10d')
        if hist.empty:
            monthly_change = None
        else:
            monthly_change = round(
                (hist["Close"].iloc[-1] - hist["Close"].iloc[0]) / hist["Close"].iloc[0] * 100, 2
            )
        info = ticker.info

        relevant = {
            
            "ticker": i,
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
            "monthly_change": monthly_change,
            "Eigenkapital": 0 

        }
      

        analyse_list.append(relevant)


    return analyse_list


finance_info(kürzel)

print(analyse_list)


with open("finance.json", "w", encoding="utf-8") as file:
    json.dump(analyse_list, file, indent=4, ensure_ascii=False)

