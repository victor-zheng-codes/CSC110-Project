"""Filtered employment_data.csv"""

import csv

new_lst = []
new_dict = {}

with open('employment_data.csv') as f:
    reader = csv.reader(f, delimiter=',')

    [next(reader, None) for item in range(13)]

    for row in reader:
        new_lst.append(row)

    content = new_lst[0: 18]
    file = open('filtered_employment_data.csv', 'w')
    writer = csv.writer(file)
    for lst in content:
        row = lst
        print(row)
        writer.writerow(row)
    file.close()
