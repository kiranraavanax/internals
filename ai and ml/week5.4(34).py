import pandas as p
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print("\nBefore Droping:\n")
df.info()
df=df.dropna(axis=1)
#OR
#df=df.drop(columns=df.columns[df.isnull().any()])
print('\n\nAfter Droping:\n')
df.info()
