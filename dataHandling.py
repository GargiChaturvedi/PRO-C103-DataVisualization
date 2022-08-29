import pandas
import plotly.express as px

df = pandas.read_csv("covidData.csv")
fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()