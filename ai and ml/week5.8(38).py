import pandas as p
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMode of Age Column:",df['Age'].mode()[0])
dp=df['Age'].fillna(df['Age'].mode()[0])
print("\nAfter Replacing with Mode:\n\n",dp.head(7))
