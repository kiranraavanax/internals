import pandas as pd
import matplotlib.pyplot as m
import seaborn as s

da=pd.read_csv("C:/Users/kiran/Documents/ai and ml/Boston.csv")
da.info()

m.figure(figsize=(18,10))
s.heatmap(data=da.corr(),annot=True)
m.title('data pre-processing')
m.show()

m.figure(figsize=(18,10))
s.histplot(data=da,x='medv',kde=True)
m.title('Exploration')
m.show()

m.figure(figsize=(18,10))
s.scatterplot(data=da,x='rm',y='medv')
m.title("data splitting")
m.show()

m.figure(figsize=(18,10))
s.scatterplot(data=da,x='lstat',y='medv')
m.title("data splitting")
m.show()
