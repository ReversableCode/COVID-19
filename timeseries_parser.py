import csv, json
import os

dir = "/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"

for file in os.listdir(dir):
	filename = "%s%s" % (dir, file)

	data = []
	with open(filename) as f:
		for row in csv.DictReader(f):
			data.append(row)

	json_data = json.dumps(data)
	json_path = open(filename + '.json', 'w')
	json_path.write(json_data)