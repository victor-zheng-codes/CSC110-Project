"""Dataclass to encapsulate data"""
from dataclasses import dataclass
import csv


@dataclass
class Employeed:
    """Employment numbers every month

    Instance Attributes:
        - industry: the industry (e.g., 'Agriculture')
        - employment: a list containing the number of employed in thousands
    """
    industry: str
    employment: list[float]


@dataclass
class CovidData:
    """Covid data by month

    Instance Attributes:
        - date: the date (e.g., '2020-03') the data is for
        - cases: the number of cases representing the case
    """
    date: str
    cases: int


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

covid_data = []
with open('filtered_covid_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if row != []:
            covid_data.append(CovidData(date=row[0], cases=int(row[1])))
