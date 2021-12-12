import matplotlib.pyplot as plt
import code_data as cd


# Assume we are given the industry
def display_individual_graphs(industry: str) -> None:
    """Display individual graph of COVID and industry relationship

    Preconditions:
        - industry is an industry in the employment data
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
    plt.figure(figsize=(10, 5))

    # set customizations for design of our visualization
    font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 20}
    plt.title(f"Association of Covid Cases and {industry} industry", **font)
    plt.xlabel("Covid Cases (x1000 people)")
    plt.ylabel(f"Employment Data for {industry} industry (x1000 people)")

    plt.scatter(covid_cases, employment_rates, c='darkblue')


def industry_covid_visualization(industry: str) -> None:
    """Display a double scatterplot showing the relationship between COVID and industry by each month so far
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
    plt.scatter(covid_dates, employment_rates, c='darkgreen', label='Employment')
    plt.scatter(covid_dates, covid_cases, c='darkblue', label='Covid Cases')
    plt.legend(loc='best')


if __name__ == "__main__":
    # test code for display_individual_graphs()
    # display_individual_graphs("Agriculture")
    # display_individual_graphs("Utilities")

    # testing code for industry_covid_visualization()
    # industry_covid_visualization("Agriculture")
    industry_covid_visualization("Utilities")
