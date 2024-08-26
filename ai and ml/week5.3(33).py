import pandas as p
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print("\nBefore Droping:\n")
df.info()
#drops Entier row data if as nan values in any coloumn
df=df.dropna()
#OR
#dp=dp.dropna(axis=0)
print('\n\nAfter Droping:\n')
df.info()
