import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
t = pd.read_csv('C:/Users/kiran/Documents/tested.csv', parse_dates=['day'], index_col='day')
a = t.plot(color='k', linewidth=1)
plt.xticks(rotation=25)
a.set_ylabel('Temp')
plt.xlabel('Date')
plt.show()
