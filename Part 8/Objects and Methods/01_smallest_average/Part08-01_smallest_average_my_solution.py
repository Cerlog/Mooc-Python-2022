def smallest_average(person1: dict, person2: dict, person3: dict):
    average1= 0
    number = len(person1)-1
    average2= 0
    average3= 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for key, value1 in person1.items():
        if type(value1) == str:
            continue
        else:
            sum1 = sum1 + value1
            average1 = sum1 / number
    for key, value2 in person2.items():
        if type(value2) == str:
            continue
        else:
            sum2 = sum2 + value2
            average2 = sum2 / number
    for key, value3 in person3.items():
        if type(value3) == str:
            continue
        else:
            sum3 = sum3 + value3
            average3 = sum3 / number
    print(average1)
    print(average2)
    print(average3)
    if average1 < average2 and average1 < average3:
        return person1
    elif average2 < average1 and average2 < average3:
        return person2
    else:
        return person3