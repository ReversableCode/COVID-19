import csv, json
import time
import re 
import os

dir = "/Users/Nab/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

for file in os.listdir(dir):
	filename = "%s%s" % (dir, file)
	csv_path = open(filename, 'r')
	json_path = open(filename + '.json', 'w')

	fields = ("Province/State", "Country/Region", "Last Update", "Confirmed", "Deaths", "Recovered")

	reader = csv.DictReader(csv_path, fields)
	out = json.dumps( [ row for row in reader ] )
	json_path.write(out)
