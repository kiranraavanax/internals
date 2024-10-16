import pandas as p
import seaborn as s
import matplotlib.pyplot as m

da=p.read_csv("C:/Users/kiran/Documents/ai and ml/Boston.csv")
da.info()
print(da.describe())

m.figure(figsize=(18,10))
s.heatmap(data=da.corr(),annot=True,cmap='coolwarm')
m.show()

m.figure(figsize=(18,10))
s.histplot(data=da,x='medv',bins=30,kde=True)
m.title('Distribution of Pricing')
m.show()

m.figure(figsize=(18,10))
s.scatterplot(data=da,x='rm',y='medv')
m.title('Number of rooms to pricing')
m.show()

m.figure(figsize=(18,10))
s.scatterplot(data=da,x='lstat',y='medv')
m.title('Lower status Population and Pricing')
m.show()