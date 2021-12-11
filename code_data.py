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


def add_employment_data() -> list[Employed]:
    """Return employment data in a list containing Employment objects read from
    filtered_employment_data.csv
    """
    employment_list = []
    with open('data/filtered_employment_data.csv') as f:
        # read the entire csv file
        reader = csv.reader(f, delimiter=',')
        # skip the first line
        next(reader, None)
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

    return employment_list


def add_covid_data() -> list[CovidData]:
    """Add covid data to a list containing CovidData objects read from filtered_covid_data.csv"""
    covid_data = []

    with open('data/filtered_covid_data.csv') as csv_file:
        # read the entire csv file
        reader = csv.reader(csv_file, delimiter=',')
        # skip the first line
        next(reader, None)
        # iterate through each line in the reader
        for row in reader:
            # check if the row is not empty
            if row != []:
                # append the covid_data to the CovidData data class
                covid_data.append(CovidData(date=row[0], cases=int(row[1])))

    return covid_data