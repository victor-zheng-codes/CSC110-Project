"""File to filter covid data"""

import csv

filtered_data = {}
with open('covid_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        date = row[1][0:7]
        if date not in filtered_data:
            filtered_data[date] = 0

        filtered_data[date] += 1

    f = open('filtered_covid_cases.csv', "w")
    f.write(str(filtered_data))
    f.close()
