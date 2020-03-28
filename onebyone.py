import csv, json
import os

dir = "/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
#dir = "/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_time/"

filename = dir + 'time_series_covid19_confirmed_global.csv'
#filename = dir + '03-24-2020.csv'

data = []
with open(filename) as f:
	for row in csv.DictReader(f):
		data.append(row)

json_data = json.dumps(data)
#json_path = open(filename + '.json', 'w')
json_path = open(dir + 'time_series_covid19_confirmed_global.json', 'w')

json_path.write(json_data)


