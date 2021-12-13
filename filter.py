"""Filter covid data from the original dataset covid_data.csv and produce a new file called
filtered_covid_cases.csv data with the date and the number of cases"""

import csv


def filter_covid() -> None:
    """To do
    """
    filtered_data = {}
    # read the covid_data.csv file. This file is too large to submit or put onto GitHub.
    with open('data/covid_data.csv') as csv_file:
        # read through each line in covid_data.csv
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip the first line with variable names
        next(csv_reader)
        # open filtered_covid_data.csv to write
        with open('filtered_covid_data.csv', 'w') as file:
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


def filter_employment_data() -> None:
    """Filter employment data from the original dataset employment_data.csv and produce a new
    file with the filtered data called filtered_employment_data.csv containing the industry and
    number of employed per month"""

    row_list = []

    # open the employment data csv file
    with open('employment_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        # skip the first 13 lines of the code
        _ = [next(reader, None) for _ in range(11)]

        # open filtered_employment_data.csv to write the filtered data
        with open('filtered_employment_data.csv', 'w') as file:
            writer = csv.writer(file)

            header_row = next(reader)
            items = header_row[1:]

            # convert calendar to the correct format
            converted_cal = convert_date_format(items)
            # insert to the beginning of the header an industry descriptor
            converted_cal.insert(0, 'Industry')
            writer.writerow(converted_cal)

            next(reader, None)

            # iterate through each row in the reader
            for row in reader:
                row_list.append(row)

            # filter only the first 19 rows that we need
            content = row_list[0: 18]

            # iterate through each element in lst and write the content
            for lst in content:
                # remove numeric numbers at the end
                list_el = lst[0].split()
                if list_el[-1].isnumeric():
                    list_el.pop()
                    lst[0] = ' '.join(list_el)

                # for some reason, some industries have more than 1 trailing digit
                if list_el[-1].isnumeric():
                    list_el.pop()
                    lst[0] = ' '.join(list_el)

                writer.writerow(lst)


def convert_date_format(input_dates: list[str]) -> list[str]:
    """Return a list containing the completed employment data month year to match the covid data.
    ('October 2019' -> '2019-19')
    >>> convert_date_format(['December 2020', 'April 2021'])
    ['2020-12', '2021-04']
    """

    calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December']

    # add a csv header with all months
    new_cal = []

    for item in input_dates:
        for month in calendar:
            m, y = item.split()
            if month == m and calendar.index(m) < 9:
                new_cal.append(y + '-0' + str(calendar.index(m) + 1))
            elif month == m:
                new_cal.append(y + '-' + str(calendar.index(m) + 1))

    return new_cal


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['filter_covid', 'filter_employment_data, convert_date_format'],
        'extra-imports': ['python_ta.contracts', 'csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
