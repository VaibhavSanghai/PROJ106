import numpy
import plotly_express as p
import pandas as pd
import csv

def get_data_source(dataPath):
    icecreamsales = []
    temperature  = []
    with open(dataPath) as csv_file:
        csv_display = csv.DictReader(csv_file)
        for row in csv_display:
            icecreamsales.append(float(row['sleep in hours']))
            temperature.append(float(row['Coffee in ml']))
        return {'x': temperature, 'y': icecreamsales}

def file_correlation(argument):
    correlation = numpy.corrcoef(argument['x'], argument['y'])
    print('correlation is', correlation[0, 1])

def setup():
    dataPath = 'coffeevssleep.csv'
    dataSource = get_data_source(dataPath)
    findCorr = file_correlation(dataSource)
    print(findCorr)
setup()