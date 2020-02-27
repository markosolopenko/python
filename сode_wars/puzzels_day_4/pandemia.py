"""
We should to find infected peoples and uninfected
"""
def infected(s):
    """

    :param s:
    :return:
    """
    infected = ''
    uninfected = ''
    if "0" not in s and "1" not in s:
        return 0
    for char in s.split("X"):
        if "1" in char:
            for people in char:
                people = "1"
                infected += people
        else:
            uninfected += char
    total = len(infected) + len(uninfected)
    return 100 * len(infected) / total

if __name__ == "__main__":
    print(infected("01000000X000X011X0X"))