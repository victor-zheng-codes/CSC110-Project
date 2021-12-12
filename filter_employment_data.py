"""Filter employment data from the original dataset employment_data.csv and produce a new
file with the filtered data called filtered_employment_data.csv containing the industry and number
of employed per month"""

import csv


def filter_employment_data() -> None:
    """Filter employment data from the original dataset employment_data.csv and produce a new
    file with the filtered data called filtered_employment_data.csv containing the industry and number
    of employed per month"""

    row_list = []

    # open the employment data csv file
    with open('employment_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        # skip the first 13 lines of the code
        [next(reader, None) for item in range(11)]

        # f = open('data/employment_months.csv', 'w')
        # writer = csv.writer(f)

        # open filtered_employment_data.csv to write the filtered data
        file = open('filtered_employment_data.csv', 'w')
        writer = csv.writer(file)

        header_row = next(reader)
        items = [item for item in header_row[1:]]
        print(items)

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

            print(lst)
            writer.writerow(lst)

        # close the file
        file.close()


def convert_date_format(input_dates: list[str]) -> list[str]:
    """Return a list containing the completed employment data month year to match the covid data.
    ('October 2019' -> '2019-19')
    >>> convert_date_format(['December 2020', 'April 2021'])
    ['2020-12', '2021-04']
    """

    calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December']

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
    filter_employment_data()
