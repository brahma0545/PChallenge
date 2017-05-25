import datetime

years = list(range(1016, 1996, 20))
selected_years = [year for year in years if datetime.date(year, 1, 26).isoweekday() == 1]

print(selected_years)
