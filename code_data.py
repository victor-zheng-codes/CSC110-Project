"""Dataclass to encapsulate data"""
from dataclasses import dataclass
from datetime import datetime
import csv


@dataclass
class Employeed:
    industry: str
    employment: list[float]


e = []
with open('filtered_employment_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if row != []:
            filter_data = []
            for i in range(1, len(row)):
                filter_data.append(float(row[i].replace(',', '')))
            object = Employeed(industry=row[0], employment=filter_data)
            e.append(object)
