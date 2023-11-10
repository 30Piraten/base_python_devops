import csv
import json

path_to_file = "sample.csv"

csv_contents = open(path_to_file).readlines()
convert = json.dumps(list(csv.reader(csv_contents)), indent=4)

print(convert)
