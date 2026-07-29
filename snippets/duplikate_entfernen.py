import pandas as pd

def entferne_duplikate(df, subset=None):
    """
    Issue #17

    Entfernt doppelte Zeilen aus einem DataFrame und behält den jeweils ersten Eintrag.
    
    Parameter:
    df (pd.DataFrame): Der Eingabe-Datensatz.
    subset (list, optional): Liste von Spalten, auf die die Duplikat-Suche beschränkt werden soll.
    
    Rückgabe:
    pd.DataFrame: Der bereinigte Datensatz.
    """
    # keep='first' ist hier explizit gesetzt, auch wenn es der Standardwert ist
    return df.drop_duplicates(subset=subset, keep='first')