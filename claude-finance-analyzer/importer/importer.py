import pandas as pd


def importer(filepath):
    df = pd.read_excel(filepath)
    return df

if __name__ == "__main__":
    df = importer("finance.xlsx")
    print(df)

#print(df["Aktie"])

"""
try 
except
finally
"""