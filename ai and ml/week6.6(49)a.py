import pandas as p
da=p.read_csv("C:/Users/kiran/Documents/ai and ml/crop_pre.csv")
da.info()
#PRE_PROCESSING
miss=da.isna().sum()
print("\nMissing Values:\n",miss)
da.dropna(inplace=True)
print("\nMissing Values:\n",da.isna().sum())