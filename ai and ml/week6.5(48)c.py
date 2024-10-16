from sklearn.model_selection import train_test_split
import pandas as p
da=p.read_csv("C:/Users/kiran/Documents/ai and ml/dhoni.csv")
X = da.drop('Average', axis=1) 
y = da['Average']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42)
print("Train set:", X_train.shape, y_train.shape)
print("Test set:", X_test.shape, y_test.shape)