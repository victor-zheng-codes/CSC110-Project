"""Filter covid data from the original dataset covid_data.csv and produce a new file called
filtered_covid_cases.csv data with the date and the number of cases"""

import csv

filtered_data = {}
# read the covid_data.csv file. This file is too large to submit or put onto GitHub.
with open('data/covid_data.csv') as csv_file:
    # read through each line in covid_data.csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the first line with variable names
    next(csv_reader)
    # open filtered_covid_data.csv to write
    file = open('filtered_covid_data.csv', 'w')
    # initialize built in csv writer method to write to file
    writer = csv.writer(file)
    # iterate through each row in the file
    for row in csv_reader:
        # find the "Accurate_Episode_Date" variable and record the date
        date = row[1][0:7]
        # check if the date is in the dictionary currently
        if date not in filtered_data:
            # if date is not currently in dictionary, initialize the date
            filtered_data[date] = 0
        # increase the accumulator of covid cases for that month
        filtered_data[date] += 1

    writer.writerow(('Date', 'Number of COVID cases'))
    # iterate through each date in and write to file the date and the number of covid cases
    for date in filtered_data:
        writer.writerow([date, filtered_data[date]])

    # close the file
    file.close()
