def list_years(dates: list):
    list_of_years = []
    for i in dates:
        list_of_years.append(i.year)
    sorting_years = sorted(list_of_years)
    return sorting_years
