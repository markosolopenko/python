from pprint import pprint
import random
def word_scores(player_word: str,available_letters_in_hand: int):
    scrabble_letter_points = {1: 'aeioulnstr',
                             2: 'dg',
                             3: 'bcmp',
                             4: 'fhvwy',
                             5: 'k',
                             8: 'jx',
                             10: 'qz'}
    sum_point_of_letters = 0
    for key,value in scrabble_letter_points.items():
        for letter in player_word:
            if letter in value:
                sum_point_of_letters += key
    full_sum_of_point = (7 * len(player_word) - 3*(available_letters_in_hand - len(player_word))) * sum_point_of_letters
    #print(full_sum_of_point)
def player_choice():
    word = input("Compose the word from this letters \n")
def deal_hand(amount_of_letters: int):
    with open('WordsForGames.txt', 'r') as file:
        content = file.read()
    hand = ''
    a = 0
    while a < amount_of_letters:
        random_letter = random.choice(content)
        if random_letter.isalpha():
            hand += random_letter.lower()
            a += 1
    letters_dict = {}
    for keys in hand:
        if keys in letters_dict:
            letters_dict[keys] += 1
        else:
            letters_dict[keys] = 1
    print(letters_dict)
    print(display_hand(letters_dict))
    print(update_hand(letters_dict))
def display_hand(letters_in_hand):
    view_the_hand = ''
    for keys in letters_in_hand.keys():
        if letters_in_hand[keys] > 1:
            view_the_hand += (letters_in_hand[keys]-1)*keys
        view_the_hand += keys
    print(' '.join(view_the_hand))
def update_hand(refresh_dict):
    dictionary = refresh_dict.copy()
    player_word = str(player_choice())
    for key in player_word:
        if key in dictionary:
            del dictionary[key]
    print('Updated dictionary: ', dictionary)
if __name__ == "__main__":
    #Scrable_game()
    #word_scores('weed',6)
    #representing_hands_as_dictionary('aqlmuli')
    deal_hand(6)