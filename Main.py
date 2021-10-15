import csv
import plotly.graph_objects as pgo
import pandas as pd

df=pd.read_csv('student_result.csv')
print(df.groupby('level')['attempt'].mean())

graph=pgo.Figure(pgo.Bar(
    x=df.groupby('level')['attempt'].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))
graph.show()