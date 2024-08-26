from sklearn.datasets import load_diabetes
import matplotlib.pyplot as m
import seaborn as s
import pandas as p
dp=load_diabetes()
col_n =dp.feature_names
df= p.DataFrame(dp.data);df.columns = col_n
#Visualizing of Outliers
s.boxplot(df['bmi'])
m.ylabel('Values');m.xlabel('bmi');m.title('Distrubution of bmi')
m.show()
#IQR
q1=df['bmi'].quantile(0.25)
q3=df['bmi'].quantile(0.75)
iqr=q3-q1
#Floor and Capping
flo=q1-1.5*iqr
cap=q3+1.5*iqr
out=df[(df.bmi<=flo)|(df.bmi>=cap)]
print("Outliers:\n",out)
