import pytest 
import pandas as pd

# pytest -v muss immer vom Rootverzeichnis ausgeführt werden 

# Ornder - Datei - Funktion 
from importer.importer import importer

def test_importer():
    df = importer("importer/finance.xlsx")
    assert isinstance(df, pd.DataFrame)