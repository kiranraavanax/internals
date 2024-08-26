import missingno as ms
import pandas as p
import seaborn as s
import matplotlib.pyplot as m
ti_da=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
#Box Plot
ms.bar(ti_da)
m.title("Missing values in Dataset")
m.show()
#Matrix Plot
ms.matrix(ti_da)
m.title('Missing Values Matrix Plot')
m.show()
#Removing Null Objects
print("Before Droping Objects:\n")
ti_da.info()
ti_d=ti_da.dropna(axis=0)
print("\n\nAfter Droping objects:\n")
ti_d.info()
#Removing Null Attributes
print("\nBefore Droping Attributes:\n")
ti_da.info()
ti=ti_da.dropna(axis=1)
print("\n\nAfter Droping Attributes:\n")
ti.info()
#Imputing Missing value of Age column through Mean
print("\n\nAge column before imputing:\n")
ti_da['Age'].info()
ti_ag=ti_da['Age'].fillna(ti_da['Age'].mean())
print("\n\nAfter Imputing:\n")
ti_ag.info()
