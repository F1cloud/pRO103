import pandas as pd
import plotly.express as px
df = pd.read_csv("Copy+of+data+-+data.csv")
print(df)

fig = px.line(df,x = "date", y = "cases", color = "country", title = "Number of Covid Cases per country")
fig.show()