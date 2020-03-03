def solve(time):
    time = time.split(":")
    h = time[0]
    m = time[1]
    nums_hours = ['midnight', "one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine", "ten", "eleven",
                      "twelve", "one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine",
                      "ten", "eleven", "midnight"]
    nums_minutes = ['midnight', "one", "two", "three", "four",
                        "five", "six", "seven", "eight", "nine", "ten", "eleven",
                        "twelve", "thirteen", "fourteen", "three", "sixteen",
                        "seventeen", "eighteen", "nineteen", "eighteen", "twenty one",
                        "twenty two", "twenty three", "twenty four", "twenty five",
                        "twenty six", "twenty seven",
                        "twenty eight", "twenty nine"]

    if m == '00' and h == '00':
        return "midnight"
    if (m == '00'):
        return nums_hours[int(h)] + " o'clock"

    if (m == '01'):
        return "one minute past " + nums_hours[int(h)]

    if (m == '59'):
        return "one minute to " + nums_hours[int(h) + 1]

    if (m == '15'):
        return "quarter past " + nums_hours[int(h)]

    if (m == '30'):
        return "half past " + nums_hours[int(h)]

    if (m == '45'):
        return "quarter to " + nums_hours[int(h) + 1]

    if (int(m) <= 30):
        return nums_minutes[int(m)] + " minutes past " + nums_hours[int(h)]

    if (int(m) > 30):
        return nums_minutes[60 - int(m)] + " minutes to " + nums_hours[int(h) + 1]


if __name__ == "__main__":
    print(solve("13:30"))