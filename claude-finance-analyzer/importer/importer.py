import pandas as pd

def importer(filepath):
    #import von Excel
    #Zuweisung Variable 
    df = pd.read_excel(filepath, header=0)
    return df

def format_portfolio(df):
    portfolio_text = "Mein Portfolio:\n"
    # _, -> erster Wert wird ignoriert Index 
    for _, row in df.iterrows():
        portfolio_text += f"{row['Aktie']} - Einlage: {row['Menge']}\n"
    return portfolio_text

def ticker_format(df):
    ticker = []
    for _, row in df.iterrows():
        ticker.append(row['Ticker'])
    return ticker

        

# Sogenannter "Guard" - Block wird nur ausgeführt wenn Script direkt gestartet wird 
if __name__ == "__main__":
    df = importer("finance.xlsx")
    print(df.columns.tolist())
    print(format_portfolio(df))
    print(ticker_format(df))