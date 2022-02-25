import csv
import pandas as pd
import plotly_express as p

with open('coffeevssleep.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = p.scatter(df, x="sleep in hours", y="Coffee in ml")
    fig.show()
