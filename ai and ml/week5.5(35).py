import pandas as p
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print("Before Filling Null values:\n\n",df.isna().sum())
df=df.fillna(0)
print("\n\nAfter Filling Null Values:\n\n",df.isna().sum())
