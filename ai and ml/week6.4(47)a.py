import pandas as p
da=p.read_csv("C:/Users/kiran/Documents/ai and ml/matches.csv")
da.info()
#PRE_PROCESSING
miss=da.isna().sum()
print("\nMissing Values:\n",miss)
da.drop('umpire3', axis=1, inplace=True)
da.dropna(axis=0,inplace=True)
# da.drop('date',axis=1,inplace=True)
print("\nMissing Values:\n",da.isna().sum())
