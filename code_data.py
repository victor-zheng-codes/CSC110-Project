"""Dataclass to encapsulate data"""
from dataclasses import dataclass
from datetime import datetime
import csv

# filtered_data = {}
# with open('covid_data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#
#     for row in csv_reader:
#         date = row[1][0:7]
#         if date not in filtered_data:
#             filtered_data[date] = 0
#
#         filtered_data[date] += 1

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


@dataclass
class CovidData:
    """"""

    date: datetime
    cases: int
    employed: int
    industry: str
