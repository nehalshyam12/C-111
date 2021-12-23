import plotly.express as px
import plotly.figure_factory as ff
import csv 
import pandas as pd 
import random
import statistics

df = pd.read_csv("studentMarks.csv")

data = df("Math_score ").tolist()

fig = ff.create_displot([data],["Math scores"],show_hist = False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print(mean,std_deviation)