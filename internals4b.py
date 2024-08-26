from matplotlib import pyplot as m
import seaborn as s
import pandas as p

data=p.read_csv("C:/Users/kiran/Downloads/tested.csv")
print(data)
c=data['Pclass'].value_counts() 
co=['k','g']
#bar
m.bar(c.index,c.values,color=co,width=0.3) 
m.xticks([0,1],['0-Automatic','1-Manual']) 
m.xlabel("survived");m.ylabel("No of passengers") 
m.title("bar ") 
m.show()

#boxplot
s.boxplot(c,color='c') 
m.xlabel(" no of pass");m.ylabel("survived") 
m.title("BOX plot of pclass Values")
m.show()

#scatter plot
ak=data['Pclass'] 
iv=range(len(data)) 
m.scatter(iv,ak,color='k',label='c') 
m.scatter(iv,ak,color='g',label='ak') 
m.title("scatter") 
m.legend() 
m.show()

#pie chart
sv = data['Pclass'].value_counts()

m.pie(sv, labels=sv.index, startangle=90, autopct="%1.0f%%")
m.title("Passenger Class Distribution")
m.show()
