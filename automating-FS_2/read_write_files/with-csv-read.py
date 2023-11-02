import csv

file_path_or_name = "registered_user_count_ytd.csv"

with open(file_path_or_name, newline="") as csv_file:
    off_reader = csv.reader(csv_file, delimiter=",")

    for _ in range(3):
        print(next(off_reader))

print("....................")
# loading the file at once
# if not too large

# initialize a list to store the data
data = []

# read the csv file and store the data
# in a list of dictionaries
with open(file_path_or_name, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        data.append(row)
        # print(row)

# display the loaded data
for row in data:
    print(row)
