"""CSC110 Fall 2021 Final Project Data Extraction

File Description
===============================
This file contains the Employed class, responsible for extracting and transforming data
from the filtered csv files to their corresponding data classes.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of students, TA, and professors
within the CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Daniel Xu, Nicole Leung, Kirsten Sutantyo, and Victor Zheng.
"""
from dataclasses import dataclass
import csv


@dataclass
class Employed:
    """A data class representing the number of employment in an industry per month for a range
    of months

    Instance Attributes:
        - industry: the name of the industry as a string (e.g., 'Agriculture')
        - employment: a list containing the number of employees employed in thousands as a float
        - date: a list containing the dates for the employment numbers as a string (e.g., '2020-10')

    Representation Invariants:
      - self.employment != {}
      - self.date != {}
      - len(self.date) == len(self.employment)
      - len(self.industry) > 0
    """
    industry: str
    employment: list[float]
    date: list[str]


@dataclass
class CovidData:
    """A data class representing the number of covid cases in a specific month.

    Instance Attributes:
        - date: the date formatted as a string (e.g., '2020-03') that corresponds to the number of \
        cases during that month
        - cases: the number of cases as an integer representing the number of cases during that
        month

    Representation Invariants:
      - len(self.data) == 7
      - self.cases >= 0
    """
    date: str
    cases: int


def add_employment_data() -> list[Employed]:
    """Return employment data in a list containing Employment objects read from
    filtered_employment_data.csv
    """
    employment_list = []
    with open('filtered_employment_data.csv') as f:
        # read the entire csv file
        reader = csv.reader(f, delimiter=',')
        # skip the first line
        first_line = next(reader, None)
        months = first_line[1:]
        # print(months)
        # iterate through each line in the reader
        for row in reader:
            # check if the line is not empty
            if row != []:
                filter_data = []  # create a list to store the employment numbers
                for i in range(1, len(row)):  # iterate through the employment numbers
                    # append to filter data with correct format
                    filter_data.append(float(row[i].replace(',', '')))
                # add the Employed object to the employment list
                employment_list.append(Employed(industry=row[0],
                                                employment=filter_data,
                                                date=months))

    return employment_list


def add_covid_data() -> list[CovidData]:
    """Add covid data to a list containing CovidData objects read from filtered_covid_data.csv"""
    covid_data = []

    with open('filtered_covid_data.csv') as csv_file:
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


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    import doctest
    doctest.testmod()

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['add_employment_data', 'add_covid_data'],
        'extra-imports': ['python_ta.contracts', 'csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
