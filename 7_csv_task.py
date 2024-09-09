import pandas as pd

data = pd.read_csv('rosstat_2020.csv')
with open('input.txt', 'r') as queries:
    query_number = int(queries.readline())
    for i in range(query_number):
        name = queries.readline()
        subject = queries.readline()
        data[data.]
