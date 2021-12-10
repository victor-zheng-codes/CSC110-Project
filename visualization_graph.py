import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import code_data as cd

employment_data = cd.add_employment_data()
covid_data = cd.add_covid_data()

industry = employment_data[0].industry
employment_rates = employment_data[0].employment[3:]

employment_for_now = []
for rates in employment_rates:
    employment_for_now.append(rates * 1)

dates = []
cases = []

for data in range(2, 25):
    dates.append(covid_data[data].date)
    cases.append(covid_data[data].cases)

employment_graph = plt.scatter(dates, employment_for_now)
covid_graph = plt.scatter(dates, cases)
