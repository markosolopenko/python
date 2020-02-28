
import random
import numpy as np

def coin_flip_streak():
    """
    We should return amount of heads and tails of coin when we flip it
    :return:
    """

    heads_probabilities = []
    tails_probabilities = []

    for something in range(10000):

        number_of_streaks_heads = 0
        number_of_streaks_tails = 0
        strung = ''
        streaks_list = []

        for experiment_number in range(100):
            if random.randint(0, 1) == 0:
                streaks_list.append("H")
            else:
                streaks_list.append("T")

        for character in streaks_list:
            if character == "H":
                strung += character
                if len(strung) == 6:
                    number_of_streaks_heads += 1
                    strung = ''
            else:
                strung = ""
        for character in streaks_list:
            if character == "T":
                strung += character
                if len(strung) == 6:
                    number_of_streaks_tails += 1
                    strung = ''
            else:
                strung = ""
        heads_probabilities.append((number_of_streaks_heads / 100))
        tails_probabilities.append((number_of_streaks_tails / 100))

    print(np.mean(heads_probabilities))
    print(np.mean(tails_probabilities))


if __name__ == "__main__":
    coin_flip_streak()

