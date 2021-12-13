"""File to visualize code through matplotlib"""
from typing import Optional

import matplotlib.pyplot as plt
import extract as cd


class Visualization:
    """Class for visualizations"""

    def get_visualization_data(self, industry: str, start_date: Optional[str] = '2020-01',
                               end_date: Optional[str] = '2021-11') -> \
            list[list[str], list[float], list[float]]:
        """Return the visualization months, employment numbers, and covid numbers
        for the correct time period. Time period is from Jan 2020 to Nov 2021 if it is not provided
        """
        # get the filtered employment and covid data
        employment_data = cd.add_employment_data()
        covid_data = cd.add_covid_data()

        # take all employment rates and dates for the correct industry
        employment_rates = []
        employment_months = []
        for employment_d in employment_data:
            # check if the industry provided matches the first letter or matches it with a comma
            if employment_d.industry.split()[0] == industry or \
                    employment_d.industry.split()[0] == industry + ',':
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
        visualization_period = \
            covid_dates[covid_dates.index(start_date): covid_dates.index(end_date)]
        # calculate the employment numbers based on the correct index
        employment_numbers = \
            employment_rates[employment_months.index(start_date): employment_months.index(end_date)]
        # calculate the covid numbers based on the correct index
        covid_numbers = covid_rates[covid_dates.index(start_date): covid_dates.index(end_date)]

        return [visualization_period, employment_numbers, covid_numbers]

    def get_benefited_industries(self) -> list[str]:
        """Returns the five industries with the steepest linear regression slopes (positive)
        """
        employment_data = cd.add_employment_data()

        industries = []
        for employment_d in employment_data:
            # skip over the total industries b/c they don't count as an industry
            if 'Total' not in employment_d.industry:
                # check if the industry provided matches the first letter or matches it with a comma
                striped_industries = employment_d.industry.replace(',', '')
                industries.append(striped_industries.split()[0])

        industry_employment_slopes = {}
        for industry in industries:
            _, e_nums, c_nums = self.get_visualization_data(industry)
            m, _ = self.linear_regression_model(c_nums, e_nums)
            industry_employment_slopes[industry] = m

        top_scores = []
        for _ in range(5):
            highest_score = max(industry_employment_slopes, key=industry_employment_slopes.get)
            industry_employment_slopes.pop(highest_score)
            top_scores.append(highest_score)

        return top_scores

    def get_struggling_industries(self) -> list[str]:
        """Returns the five industries with the steepest linear regression slopes (negative)
        """
        employment_data = cd.add_employment_data()

        industries = []
        for employment_d in employment_data:
            # skip over the total industries b/c they don't count as an industry
            if 'Total' not in employment_d.industry:
                # check if the industry provided matches the first letter or matches it with a comma
                striped_industries = employment_d.industry.replace(',', '')
                industries.append(striped_industries.split()[0])

        industry_employment_slopes = {}
        for industry in industries:
            _, e_nums, c_nums = self.get_visualization_data(industry)
            m, _ = self.linear_regression_model(c_nums, e_nums)
            industry_employment_slopes[industry] = m

        lowest_scores = []
        for _ in range(5):
            highest_score = min(industry_employment_slopes, key=industry_employment_slopes.get)
            industry_employment_slopes.pop(highest_score)
            lowest_scores.append(highest_score)

        return lowest_scores

    def get_best_association(self) -> list[str]:
        """Returns the 5 industries with the highest correlations (cor closest to
        plus or minus 1)"""
        employment_data = cd.add_employment_data()

        industries = []
        for employment_d in employment_data:
            if 'Total' not in employment_d.industry:
                # check if the industry provided matches the first letter or matches it with a comma
                striped_industries = employment_d.industry.replace(',', '')
                industries.append(striped_industries.split()[0])

        industry_correlations = {}
        for industry in industries:
            _, e_nums, c_nums = self.get_visualization_data(industry)
            cor = self.correlation_calculator(c_nums, e_nums)
            # get the absolute value because we are looking for highest association, which could
            # be negative or positive
            industry_correlations[industry] = abs(cor)

        print(industry_correlations)

        # calculate the 5 highest correlations in the dictionary
        highest_cor = []
        for _ in range(5):
            # use the key tool to get the iterable
            highest_score = max(industry_correlations, key=industry_correlations.get)
            # remove the highest score from the dictionary
            industry_correlations.pop(highest_score)
            # append the name of the highest score into the dictionary
            highest_cor.append(highest_score)

        return highest_cor

    def get_worst_association(self) -> list[str]:
        """Returns the 5 industries with the smallest correlations (cor closest to zero)"""
        employment_data = cd.add_employment_data()

        industries = []
        for employment_d in employment_data:
            if 'Total' not in employment_d.industry:
                # check if the industry provided matches the first letter or matches it with a comma
                striped_industries = employment_d.industry.replace(',', '')
                industries.append(striped_industries.split()[0])

        industry_correlations = {}
        for industry in industries:
            _, e_nums, c_nums = self.get_visualization_data(industry)
            cor = self.correlation_calculator(c_nums, e_nums)
            industry_correlations[industry] = abs(cor)

        print(industry_correlations)

        # calculate the 5 lowest correlations in the dictionary
        lowest_correlations = []
        for _ in range(5):
            # use the key tool to get the iterable
            highest_score = min(industry_correlations, key=industry_correlations.get)
            # remove the highest score from the dictionary
            industry_correlations.pop(highest_score)
            # append the name of the highest score into the dictionary
            lowest_correlations.append(highest_score)

        return lowest_correlations

    def display_multiple_associations(self, industries: list[str], criteria: str) -> None:
        """Displays more than 1 scatterplot on top of one another industries provided"""

        # code to visualize
        # set a window size of 10 inches by 5 inches
        plt.figure(figsize=(12, 6))

        # set customizations for design of our visualization
        font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 15}
        plt.title(f"Association of Covid Cases and "
                  f"top 5 industries with criteria: {criteria}", **font)
        plt.xlabel("Covid Cases (x1000 people)")
        plt.ylabel("Employment Data (x1000 people)")

        plt_colors = ['green', 'blue', 'red', 'orange', 'brown']

        for industry in industries:
            _, employment_numbers, covid_numbers = self.get_visualization_data(industry)
            color = plt_colors[industries.index(industry)]
            plt.scatter(covid_numbers, employment_numbers, c=color, label=industry)

            m, b = self.linear_regression_model(x_points=covid_numbers, y_points=employment_numbers)
            self.add_linear_regression_model(m, b, min(covid_numbers),
                                             max(covid_numbers), color=color)

        plt.legend(loc='best')
        plt.show()

    def display_individual_graphs(self, industry: str, start_date: Optional[str] = '2020-01',
                                  end_date: Optional[str] = '2021-11') -> None:
        """Display individual graph of COVID and industry relationship with linear regression

        Preconditions:
            - industry is an industry in the employment data
            - start_date and end_date is within both of the covid and employment dates
        """

        _, employment_numbers, covid_numbers = self.get_visualization_data(industry,
                                                                           start_date, end_date)

        # code to visualize
        # set a window size of 10 inches by 5 inches
        plt.figure(figsize=(12, 6))

        # set customizations for design of our visualization
        font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 15}
        plt.title(f"Association of Covid Cases and {industry} industry "
                  f"from {start_date} to {end_date}", **font)
        plt.xlabel("Covid Cases (x1000 people)")
        plt.ylabel(f"Employment Data for {industry} industry (x1000 people)")

        plt.scatter(covid_numbers, employment_numbers, c='darkblue')

        m, b = self.linear_regression_model(x_points=covid_numbers, y_points=employment_numbers)
        self.add_linear_regression_model(m, b, min(covid_numbers), max(covid_numbers))
        cor = self.correlation_calculator(x_points=covid_numbers, y_points=employment_numbers)

        print(f'Correlation of {industry} and COVID cases: ', cor)
        plt.show()

    def industry_covid_visualization(self, industry: str, start_date: Optional[str] = '2020-01',
                                     end_date: Optional[str] = '2021-11') -> None:
        """Display a double scatterplot showing the relationship between COVID and industry from the
        start to the end date
        """
        visualization_dates, employment_numbers, covid_numbers = \
            self.get_visualization_data(industry, start_date, end_date)

        # set a window size of 10 inches by 6 inches
        plt.figure(figsize=(12, 6))

        # set customizations for design of our visualization
        font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 15}
        plt.title(f"Association of Covid Cases and {industry} industry "
                  f"from {start_date} to {end_date}", **font)
        plt.xlabel("Year-Month")
        plt.ylabel(f"COVID & {industry} industry (x1000 people)")

        # rotate the x ticks so that they are visible
        plt.xticks(rotation=45)

        plt.scatter(visualization_dates, employment_numbers, c='darkgreen', label='Employment')
        plt.scatter(visualization_dates, covid_numbers, c='darkblue', label='Covid Cases')
        # find the best position to plot the legend
        plt.legend(loc='best')
        plt.show()

    def add_linear_regression_model(self, m: float, b: float, start_x: float, end_x: float,
                                    color: Optional[str] = 'red') -> None:
        """Adds a linear regression line to the graph between the two specified points"""
        y_0 = m * start_x + b
        y_1 = m * end_x + b

        plt.plot([start_x, end_x], [y_0, y_1], c=color)

    def linear_regression_model(self, x_points: list[float], y_points: list[float]) -> \
            tuple[float, float]:
        """Returns a tuple of two integers containing the formula for the linear regression line for
        the given points using the least least squares regression line formula. The first point is
        m, the slope of the line. The second point is b, the intercept of the line.

        This helps us form an equaltion using the formula y = mx + b

        slope m = (N Σ(xy) − Σx Σy) / (N Σ(x**2) − (Σx)**2), where N is the number of points
        source: https://www.mathsisfun.com/data/least-squares-regression.html

        Preconditions:
            - length of y_points and x_points are the same

        >>> x_points = [2,3,5,7,9]
        >>> y_points = [4,5,7,10,15]
        >>> v = Visualization()
        >>> m, b = v.linear_regression_model(x_points, y_points)
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
        b = (sum_y - m * sum_x) / n

        return m, b

    def correlation_calculator(self, x_points: list[float], y_points: list[float]) -> float:
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
        >>> v = Visualization()
        >>> round(v.correlation_calculator(x_p, y_p), 4) == 0.7559
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
        numer = (n * sum_xy - sum_x * sum_y)
        denom = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5
        r = numer / denom

        return r


if __name__ == "__main__":
    import python_ta

    # test code for display_individual_graphs()
    v = Visualization()
    # v.display_individual_graphs("Utilities")
    association = v.get_worst_association()
    v.display_multiple_associations(association, 'Worst Association')
    # testing code for industry_covid_visualization()
    # industry_covid_visualization("Utilities", '2020-01', '2021-05')

    python_ta.check_all(config={
        'allowed-io': ['industry_covid_visualization', 'display_individual_graphs',
                       'get_best_association', 'get_worst_association'],
        'extra-imports': ['matplotlib.pyplot', 'extract'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
