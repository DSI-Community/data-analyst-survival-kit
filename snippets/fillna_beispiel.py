import pandas as pd
daten={"werte":[10,20, None, 40]}
df=pd.DataFrame(daten)
print(df)
mittelwert=df["werte"].mean()
df["werte"]=df["werte"].fillna(mittelwert)
print(df)