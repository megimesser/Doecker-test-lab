import pandas as pd

def importer(filepath):
    #import von Excel
    #Zuweisung Variable 
    df = pd.read_excel(filepath, header=0)
    return df

def format_portfolio(df):
    portfolio_text = "Mein Portfolio:\n"
    portfolio_list = []
    # _, -> erster Wert wird ignoriert Index 
    for _, row in df.iterrows():
        #Buyin soll hier noch hinzugefügt werden
        portfolio_text += f"{row["Ticker"]} - {row['Aktie']} - Einlage: {row['Menge']} \n"
    for _, row in df.iterrows():
        portfolio_list.append({row["Ticker"],row["Menge"],row["Aktie"]})
    return portfolio_list

#Aktienticker extrahieren 
def ticker_format(df):
    ticker = []
    for _, row in df.iterrows():
        ticker.append(row['Ticker'])
    return ticker

        

# Sogenannter "Guard" - Block wird nur ausgeführt wenn Script direkt gestartet wird 
if __name__ == "__main__":
    df = importer("finance.xlsx")
    #print(df.columns.tolist())
    print(format_portfolio(df))
   
    #print(ticker_format(df))