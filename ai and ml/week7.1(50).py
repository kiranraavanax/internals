import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Load dataset
data = pd.read_csv("C:/Users/kiran/Documents/ai and ml/week7th.csv")

# Drop the 'id' column
data.drop(["id"], axis=1, inplace=True)

# Drop the column with all NaN values
data.drop(["Unnamed: 32"], axis=1, inplace=True)

# Encode the 'diagnosis' column: 1 for malignant, 0 for benign
data.diagnosis = [1 if i == "M" else 0 for i in data.diagnosis]

# Separate features and target variable
x = data.drop(["diagnosis"], axis=1)
y = data.diagnosis.values

# Handle missing values
imputer = SimpleImputer(strategy='mean')  # You can choose other strategies based on your needs
x = imputer.fit_transform(x)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("\nAccuracy of the model using Decision Tree Classifier is ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Random Forest Classifier
model1 = RandomForestClassifier()
model1.fit(x_train, y_train)
y_pred1 = model1.predict(x_test)
print("\nAccuracy of the model using Random Forest Classifier is ", accuracy_score(y_test, y_pred1))
print(classification_report(y_test, y_pred1))

# Support Vector Classifier
model2 = SVC(kernel='rbf')
model2.fit(x_train, y_train)
y_pred2 = model2.predict(x_test)
print("\nAccuracy of the model using Support Vector Classifier is ", accuracy_score(y_test, y_pred2))
print(classification_report(y_test, y_pred2))

# Optional: Print confusion matrix
print("\nConfusion Matrix for Decision Tree Classifier:")
print(confusion_matrix(y_test, y_pred))

print("\nConfusion Matrix for Random Forest Classifier:")
print(confusion_matrix(y_test, y_pred1))

print("\nConfusion Matrix for Support Vector Classifier:")
print(confusion_matrix(y_test, y_pred2))