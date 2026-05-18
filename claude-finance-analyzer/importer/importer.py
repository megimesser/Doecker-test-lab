import pandas as pd

def importer(filepath):
    df = pd.read_excel(filepath, header=0)
    return df

def format_portfolio(df):
    portfolio_text = "Mein Portfolio:\n"
    for _, row in df.iterrows():
        portfolio_text += f"{row['Aktie']} - Menge: {row['Menge']}\n"
    return portfolio_text

if __name__ == "__main__":
    df = importer("finance.xlsx")
    print(df.columns.tolist())
    print(format_portfolio(df))