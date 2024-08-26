import matplotlib.pyplot as m
import missing as ms
import pandas as pd
ti_data=pd.read_csv("C:/Users/kiran/Downloads/tested.csv")

#bar plot
ms.bar(ti_data)
m.title("missing value dataset")
m.show()

#matrix plot
ms.metrics(ti_data)
m.title("missing value matrix plot")
m.show()

#Removing plot objects
print("\n before droping objects:\n")
ti_data.info()
ti_data1=ti_data.dropna(axis=0)
print("\n\n after droping objects :\n\n")
ti_data1.info()

#Removing attributes
print("\n before droping attributes: \n")
ti_data.info()
to=ti_data.dropna()
print("\n\n after droping attributes: \n")
to.info()

#Imputing missing values
print("\n\n Age column before imputing :\n")
ti_data['Age'].info()
ti_data2=ti_data['Age'].fillna(ti_data['Age'].mean())
print("\n\n After imputing :\n\n")
ti_data2.info()

