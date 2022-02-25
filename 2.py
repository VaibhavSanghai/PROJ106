import csv
import pandas as pd
import plotly_express as p

with open('StudentvsDays.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = p.scatter(df, x="Marks In Percentage", y="Roll No")
    fig.show()
