"""File to visualize code through matplotlib"""

import matplotlib.pyplot as plt
import code_data as cd
import math


# Assume we are given the industry
def display_individual_graphs(industry: str, start_date: str, end_date: str) -> None:
    """Display individual graph of COVID and industry relationship with linear regression

    Preconditions:
        - industry is an industry in the employment data
        - start_date and end_date is within both of the covid and employment dates
    """

    # get the filtered employment and covid data
    employment_data = cd.add_employment_data()
    covid_data = cd.add_covid_data()

    # take all employment rates and dates for the correct industry
    employment_rates = []
    employment_months = []
    for employment_d in employment_data:
        if employment_d.industry == industry:
            employment_rates = employment_d.employment
            employment_months = employment_d.date

    # take all covid dates and cases from the covid data
    covid_dates = []
    covid_rates = []
    # only use the 2 to the last industry
    for i in range(2, len(covid_data) - 1):
        covid_dates.append(covid_data[i].date)
        # divide by 1000 to match the employment relationship
        covid_rates.append(covid_data[i].cases / 1000)

    # visualization period will be the same for covid and employment datasets
    visualization_period = covid_dates[covid_dates.index(start_date): covid_dates.index(end_date)]
    # calculate the employment numbers based on the correct index
    employment_numbers = employment_rates[employment_months.index(start_date): employment_months.index(end_date)]
    # calculate the covid numbers based on the correct index
    covid_numbers = covid_rates[covid_dates.index(start_date): covid_dates.index(end_date)]

    # code to visualize
    # set a window size of 10 inches by 5 inches
    plt.figure(figsize=(10, 5))

    # set customizations for design of our visualization
    font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 15}
    plt.title(f"Association of Covid Cases and {industry} industry from {start_date} to {end_date}", **font)
    plt.xlabel("Covid Cases (x1000 people)")
    plt.ylabel(f"Employment Data for {industry} industry (x1000 people)")

    plt.scatter(covid_numbers, employment_numbers, c='darkblue')

    m, b = linear_regression(x_points=covid_numbers, y_points=employment_numbers)
    add_linear_regression(m, b, min(covid_numbers), max(covid_numbers))
    correlation_calculator(x_points=covid_numbers, y_points=employment_numbers)


def industry_covid_visualization(industry: str) -> None:
    """Display a double scatterplot showing the relationship between COVID and industry by each
     month so far
    """
    employment_data = cd.add_employment_data()
    covid_data = cd.add_covid_data()
    print(len(covid_data))

    employment_rates = []
    for employment_d in employment_data:
        if employment_d.industry == industry:
            employment_rates = employment_d.employment[3:]

    # append dates from the covid data
    covid_dates = []
    covid_cases = []

    # only use the 2 to the last industry
    for i in range(2, len(covid_data) - 1):
        covid_dates.append(covid_data[i].date)
        # divide by 1000 to match the employment relationship
        covid_cases.append(covid_data[i].cases / 1000)

    # set a window size of 10 inches by 5 inches
    plt.figure(figsize=(10, 6))

    # set customizations for design of our visualization
    font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 20}
    plt.title(f"Association of Covid Cases and {industry} industry over time", **font)
    plt.xlabel("Month-Year")
    plt.ylabel(f"COVID & {industry} industry (x1000 people)")

    plt.xticks(rotation=45)

    # plt.gca().legend(('y0','y1'))
    # problem!!! dates will be wrong!
    # TODO: fix employment month which is incorrectly matched with covid months
    plt.scatter(covid_dates, employment_rates, c='darkgreen', label='Employment')
    plt.scatter(covid_dates, covid_cases, c='darkblue', label='Covid Cases')
    plt.legend(loc='best')


def add_linear_regression(m: float, b: float, start_x: float, end_x: float) -> None:
    """Adds a linear regression line to the graph between the two specified points"""
    y_0 = m * start_x + b
    y_1 = m * end_x + b

    plt.plot([start_x, end_x], [y_0, y_1], label='linear regression line')


def linear_regression(x_points: list[float], y_points: list[float]) -> tuple[float, float]:
    """Returns a tuple of two integers containing the formula for the linear regression line for the
     given points using the least least squares regression line formula. The first point is m, the
     slope of the line. The second point is b, the intercept of the line.

    This helps us form an equaltion using the formula y = mx + b

    slope m = (N Σ(xy) − Σx Σy) / (N Σ(x**2) − (Σx)**2), where N is the number of points
    source: https://www.mathsisfun.com/data/least-squares-regression.html

    Preconditions:
        - length of y_points and x_points are the same

    >>> x_points = [2,3,5,7,9]
    >>> y_points = [4,5,7,10,15]
    >>> m, b = linear_regression(x_points, y_points)
    >>> assert round(m, 3) == 1.518
    >>> assert round(b, 3) == 0.305
    """
    n = len(x_points)

    sum_x = 0
    sum_x_squared = 0
    # Calculate the sum for x points and x squared points
    for val in x_points:
        sum_x += val
        sum_x_squared += val ** 2
    # Calculate the sum for y points
    sum_y = 0
    for val in y_points:
        sum_y += val
    # Calculate the sum for x points times y points
    sum_xy = 0
    for i in range(n):
        sum_xy += x_points[i] * y_points[i]

    # print(sum_x, sum_y, sum_x_squared, sum_xy)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x)/n

    return m, b


def correlation_calculator(x_points: list[float], y_points: list[float]) -> float:
    """Return a correlation of the association between the x and y variables

    We can use this to judge the association between our x and y variables to determine if
    we can even use linear regression. Linear regression assumes that there is some sort of
    association between the x and y variables.

    We will use the Pearson Correlation Coeficient Formula, the most commonly used correlation
    formula.

    Sources (cite later): https://www.questionpro.com/blog/pearson-correlation-coefficient/,
    https://www.wallstreetmojo.com/pearson-correlation-coefficient/

    r = (n(Σxy) - (Σx)(Σy)) / ((nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)) ** 0.5

    r = Pearson Coefficient
    n= number of the pairs of the stock
    ∑xy = sum of products of the paired scores
    ∑x = sum of the x scores
    ∑y= sum of the y scores
    ∑x^2 = sum of the squared x scores
    ∑y^2 = sum of the squared y scores

    Precondition:
        - Length of x_p and y_p are the same

    >>> x_p = [6,8,10]
    >>> y_p = [12,10,20]
    >>> round(correlation_calculator(x_p, y_p), 4) == 0.7559
    True
    """
    # calculate n, the number of pairs
    n = len(x_points)

    # Calculate the sum for x points and x squared points
    sum_x = 0
    sum_x_squared = 0
    for val in x_points:
        sum_x += val
        sum_x_squared += val ** 2

    # Calculate the sum for y points and y squared poionts
    sum_y = 0
    sum_y_squared = 0
    for val in y_points:
        sum_y += val
        sum_y_squared += val ** 2

    # Calculate the sum for x points times y points
    sum_xy = 0
    for i in range(n):
        sum_xy += x_points[i] * y_points[i]

    # print(sum_x, sum_y, sum_x_squared, sum_y_squared, sum_xy)

    r = (n * sum_xy - sum_x * sum_y) / ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5

    return r


if __name__ == "__main__":
    import python_ta
    # test code for display_individual_graphs()
    display_individual_graphs("Agriculture", '2020-01', '2021-05')
    # display_individual_graphs("Utilities")

    # testing code for industry_covid_visualization()
    # industry_covid_visualization("Agriculture")

    # python_ta.check_all(config={
    #     'allowed-io': ['industry_covid_visualization', 'display_individual_graphs'],
    #     'extra-imports': ['matplotlib.pyplot', 'code_data'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })

    # industry_covid_visualization("Utilities")
