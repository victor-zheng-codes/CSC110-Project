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

    employment_rates = []
    for employment_d in employment_data:
        if employment_d.industry == industry:
            employment_rates = employment_d.employment[3:]

    # industry = employment_data[0].industry
    # employment_rates = employment_data[0].employment[3:]

    # employment_for_now = []
    # for rates in employment_rates:
    #     employment_for_now.append(rates * 10)

    # append dates from the covid data
    covid_dates = []
    covid_cases = []

    for i in range(2, 25):
        covid_dates.append(covid_data[i].date)
        covid_cases.append(covid_data[i].cases / 10)

    font = {'fontname': 'Poppins', 'family': 'sans-serif', 'color': 'darkblue', 'size': 20}

    plt.title(f"Association of Covid Cases and {industry}", **font)
    plt.xlabel("Covid Cases")
    plt.ylabel(f"Employment Data for {industry}")

    plt.scatter(covid_cases, employment_rates)


if __name__ == "__main__":
    display_individual_graphs("Agriculture")
