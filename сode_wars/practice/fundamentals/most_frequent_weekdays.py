import operator
import datetime


def most_frequent_days(year):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    most = (datetime.date(year, 1, 1).weekday(), datetime.date(year, 12, 31).weekday())
    return [days[i] for i in sorted(set(most))]


if __name__ == '__main__':
    print(most_frequent_days(2019))
