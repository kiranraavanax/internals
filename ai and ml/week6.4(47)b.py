import matplotlib.pyplot as m
import seaborn as s
import pandas as pd

# Read the CSV file
da = pd.read_csv("C:/Users/kiran/Documents/ai and ml/matches.csv")

# Function to create a histogram
def histo(da, col, title, xlabel):
    m.figure(figsize=(8, 6))
    s.histplot(da[col], bins=20, kde=True)
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel('Frequency')
    m.show()

# Function to create a count plot
def count_plot(da, x, title, xlabel):
    m.figure(figsize=(15, 7))
    s.countplot(x=x, data=da, palette='Set2')
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel('Count')
    m.xticks(rotation=90)
    m.tight_layout()
    m.show()

# Function to create a stacked bar chart
def sta_bar(da, x, y, title, xlabel, ylabel, legend_title=None):
    dp = da.groupby([x, y]).size().unstack()
    dp.plot(kind='bar', stacked=True, figsize=(10, 6))
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel(ylabel)
    if legend_title:
        m.legend(title=legend_title)
    m.show()

# DATA_EXPLORATION
histo(da, 'win_by_runs', 'Distribution of Win by Runs', 'Win by Runs')
histo(da, 'win_by_wickets', 'Distribution of Win by Wickets', 'Win by Wickets')
count_plot(da, 'city', 'Count of Matches at Each City', 'City')
count_plot(da, 'winner', 'Count of Winning of Each Team', 'Team')
sta_bar(da, 'toss_decision', 'result', 'Toss Decision vs. Match Result', 'Toss Decision', 'Count', legend_title='Match Result')
sta_bar(da, 'season', 'toss_decision', 'Season-wise Toss Decision', 'Season', 'Count', legend_title='Toss Decision')
