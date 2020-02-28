import re
# def date_ditect():
#     date = int(input("Specify the day: "))
#     month = int(input("Specify the month: "))
#     year = int(input("Specify the year: "))
#     date_month_year = re.compile(r'\d\d/\d\d/\d\d\d\d')
#     example = date_month_year.search('12/11/1000')
#     print(example.group())
#
# if __name__ == "__main__":
#     date_ditect()
numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))
