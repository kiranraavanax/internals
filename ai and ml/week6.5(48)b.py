import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
da = pd.read_csv("C:/Users/kiran/Documents/ai and ml/dhoni.csv")

# Plot histogram
plt.figure(figsize=(18,10))
sns.histplot(da['Runs'], bins=15, kde=True)
plt.title('Distribution of Runs Scored')
plt.show()

# Plot barplot
plt.figure(figsize=(18,10))
sns.barplot(data=da, x='Year', y='Runs', palette='viridis', hue=None)
plt.title('Batting Scores Over the Years')
plt.xlabel('Year')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()

# Filter numeric columns for correlation
numeric_data = da.select_dtypes(include=[float, int])

# Plot heatmap
plt.figure(figsize=(18,10))
sns.heatmap(data=numeric_data.corr(), annot=True, cmap='crest')
plt.title("Heatmap on DHONI's stats")
plt.show()