import pytest 
import pandas as pd

# Ornder - Datei - Funktion 
from importer.importer import importer

def test_importer():
    df = importer("importer/finance.xlsx")
    assert isinstance(df, pd.DataFrame)