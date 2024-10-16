import pandas as p
import seaborn as s
import matplotlib.pyplot as m
da=p.read_csv("C:/Users/kiran/Documents/ai and ml/fish.csv")
print(da.isna().sum())
x=da.iloc[:,1:]
y=da.loc[:,'Species']
#Scaling
from sklearn.preprocessing import MinMaxScaler
sca=MinMaxScaler()
sca.fit(x)
x_sca=sca.transform(x)
#Transformation of Y
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
y=lb.fit_transform(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_sca,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
mod=LogisticRegression()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
from sklearn.metrics import accuracy_score
print("\nAccuracy:",accuracy_score(y_test,y_pred))
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
s.heatmap(cm,annot=True)
m.xlabel("Prediction"); m.ylabel('Target')
m.title('Confusion Matrix'); m.show()
