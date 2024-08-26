from sklearn.datasets import load_diabetes
import matplotlib.pyplot as m
import seaborn as s
import pandas as p
dp=load_diabetes()
col_n =dp.feature_names
df= p.DataFrame(dp.data)
df.columns = col_n
m.figure(figsize=(18,10))
s.boxplot(data=df)
m.title('Multivariate Outliers')
m.ylabel('Values')
m.show()
