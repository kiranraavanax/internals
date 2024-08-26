import numpy as n
import pandas as p
import matplotlib.pyplot as m
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
x=df.items
y=df.day
m.figure(figsize=(18,10))
m.scatter(x,y,label="values of x & y")
m.xlabel("Temp")
m.ylabel("date")
m.title("Scatter plot")
m.show()
S
