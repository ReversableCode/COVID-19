import csv, json
import os

filename = "/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


data = []
with open(filename) as f:
	for row in csv.DictReader(f):
		data.append(row)

json_data = json.dumps(data)
json_path = open('/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.json', 'w')
json_path.write(json_data)
