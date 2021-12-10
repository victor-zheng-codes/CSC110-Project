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

    for lst in content:
        new_dict[lst[0]] = lst[1:]

    print(new_dict)
