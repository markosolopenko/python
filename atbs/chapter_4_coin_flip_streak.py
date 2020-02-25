

import random
def coin_flip_streak():
    """
    We should to return amount of heads and tails of coin when we flip it
    :return:
    """
    numberOfStreaksheads = 0
    numberOfStreakstails = 0
    strung = ''
    streaks_list = []
    for experimentNumber in range(10000):
        if random.randint(0,1) == 0:
            streaks_list.append("H")
        else:
            streaks_list.append("T")

    for character in streaks_list:
        if character == "H":
            strung += character
            if len(strung) == 6:
                numberOfStreaksheads += 1
                strung = ''
        else:
            strung = ""
    for character in streaks_list:
        if character == "T":
            strung += character
            if len(strung) == 6:
                numberOfStreakstails += 1
                strung = ''
        else:
            strung = ""
    return 'Chance of streak heads: %s%%' % (numberOfStreaksheads / 100),'Chance of streak tails: %s%%' % (numberOfStreakstails / 100)
if __name__ == "__main__":
    print(coin_flip_streak())

