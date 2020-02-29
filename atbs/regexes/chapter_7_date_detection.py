def date_ditect():
    days = int(input("Specify the day: "))
    month = (input("Specify the month: "))
    year = int(input("Specify the year: "))
    leap_month = '02'
    month_thirty = ['04','06','09','11']
    month_thirty_one = ['01','03','05','07','08','10','12']
    if month in month_thirty and year in range(1000,2999):
        if days > 30:
            print(f'It is wrong data: {days}/{month}/{year} April, June, September, and November have 30 days')
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 and month == leap_month:
        if days not in range(1,29):
            print(f'It is the leap year!!! {days}/{month}/{year} In the leap year February has 29 days!!!')
    elif year % 4 != 0 and month == leap_month or year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        if days > 28:
            print(f'This date: {days}/{month}/{year} not in the leap year February has only 28 days!!!')
    elif month in month_thirty_one and year in range(1000,2999):
        if days > 31:
            print(f"Wrong data: {days}/{month}/{year} January, March, May, July, August, October, December have 31 days")




if __name__ == "__main__":
    date_ditect()
