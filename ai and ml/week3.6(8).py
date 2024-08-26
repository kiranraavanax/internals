import pandas as p
t={
'Course':["PY","JV","DBMS","MMA","MMA"],
'Fee':[300,600,21,350,67],
'Complexity':[100,56,32,10,67]
}
d=p.DataFrame(t)
print(d)
print("\n",d.pivot(columns='Course',values='Complexity'))
print("\n",d.melt())
