"""Dataclass to encapsulate data"""
from dataclasses import dataclass
import csv


@dataclass
class Employed:
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


employment_list = []
with open('filtered_employment_data.csv') as f:
    # read the entire csv file
    reader = csv.reader(f, delimiter=',')
    # iterate through each line in the reader
    for row in reader:
        # check if the line is not empty
        if row != []:
            filter_data = []  # create a list to store the employment numbers
            for i in range(1, len(row)):  # iterate through the employment numbers
                # append to filter data with correct format
                filter_data.append(float(row[i].replace(',', '')))
            # add the Employed object to the employment list
            employment_list.append(Employed(industry=row[0], employment=filter_data))


covid_data = []
with open('filtered_covid_data.csv') as csv_file:
    # read the entire csv file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # iterate through each line in the reader
    for row in csv_reader:
        # check if the row is not empty
        if row != []:
            # append the covid_data to the CovidData data class
            covid_data.append(CovidData(date=row[0], cases=int(row[1])))
