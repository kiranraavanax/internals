import pandas as p
df=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMedian of Age Column:",df['Age'].median())
dp=df['Age'].fillna(df['Age'].median())
print("\nAfter Replacing with Mean:\n\n",dp.head(7))
