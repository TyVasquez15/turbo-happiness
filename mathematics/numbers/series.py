def sum(*, list):
    total = 0

    for value in list:
        total += value

    return total


def average(*, list):
    return sum(list=list) / len(list)