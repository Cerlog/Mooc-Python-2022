# Helper function for one average
def average(person: dict):
    ex_sum = person["result1"] + person["result2"] + person["result3"]

    return ex_sum / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    return smallest