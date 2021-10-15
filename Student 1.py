import csv
import plotly.graph_objects as pgo
import pandas as pd

df=pd.read_csv('student_result.csv')
data=df.loc[df['student_id']=='TRL_xsl']
print(data.groupby('level')['attempt'].mean())

graph=pgo.Figure(pgo.Bar(
    x=data.groupby('level')['attempt'].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))
graph.show()