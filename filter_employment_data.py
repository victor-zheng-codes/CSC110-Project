"""Filter employment data from the original dataset employment_data.csv and produce a new
file with the filtered data called filtered_employment_data.csv containing the industry and number
of employed per month"""

import csv

row_list = []
new_dict = {}

# open the employment data csv file
with open('employment_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    # skip the first 13 lines of the code
    [next(reader, None) for item in range(13)]
    # iterate through each row in the reader
    for row in reader:
        # add each row to the row_list
        row_list.append(row)

    # filter only the first 19 rows that we need
    content = row_list[0: 18]
    # open filtered_employment_data.csv to write the filtered data
    file = open('filtered_employment_data.csv', 'w')
    writer = csv.writer(file)
    # iterate through each element in lst and write the content
    for lst in content:
        print(lst)
        writer.writerow(lst)

    # close the file
    file.close()
