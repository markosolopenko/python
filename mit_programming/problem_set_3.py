from pprint import pprint
import random
import math
def Scrable_game():
    a = 0
    players = int(input("Enter total number of hands: "))
    all_hands_count = 0
    vowels = 'aeiou'
    while a < players:
        hand = load_words()
        n = len(hand)
        dict_from_letters = get_frequency_dict(hand)
        print(f'Current Hand: {hand}')
        ask = input(f'Would you like to substitute a letter?')
        if ask == 'yes':
            with open('WordsForGames.txt', 'r') as file:
                content = file.read()
            letter_to_replace = input(f'Which letter would you like to replace: ')
            rand = random.choice(content)
            if rand.isalpha():
                hand = hand.replace(letter_to_replace, rand)
                dict_from_letters = get_frequency_dict(hand)
                print(f'Current hand: {hand}')
        else:
            print(f'Current hand: {hand}')
        while True:
            player_word = input(f'Please enter a word or "!!" to indicate you are done: ')
            if '*' in player_word:
                rep = input('Vowel: ')
                player_word = player_word.replace('*', rep, 1)
            if player_word == '!!':
                print(f'Total score for this hand: {all_hands_count}')
                s = input(f'Would you like to replay the hand? ')
                if s == 'yes':
                    break
                else:
                    print(f'Total score: {all_hands_count}')
                    a += 1
                    break
            else:
                check_if_valid = is_valid_word(player_word,hand)
                if check_if_valid is False:
                    print(f'That is not a valid word. Please choose another word.')
                    refresh = update_hand(dict_from_letters,player_word)
                    dict_from_letters = get_frequency_dict(refresh)
                    if not refresh:
                        a+=1
                        print(f'Ran out of letters. Total score: {all_hands_count} points')
                        break
                    else:
                        print(f"Current hand: ", ' '.join(refresh))

                else:
                    count = word_scores(player_word,n)
                    all_hands_count += count
                    print(f'"{player_word}" earned {count} points. Total: {all_hands_count}')
                    refresh = update_hand(dict_from_letters, player_word)
                    dict_from_letters = get_frequency_dict(refresh)
                    if len(refresh) == 0:
                        a += 1
                        print(f'Ran out of letters. Total score: {all_hands_count} points')
                        break
                    else:
                        print(f"Current hand: ", ' '.join(refresh))











##### Make a list of random letters
def load_words():
    with open('WordsForGames.txt', 'r') as file:
        content = file.read()
    hand = ''
    a = 0
    amount_of_letters = random.randint(4, 10)
    while a < amount_of_letters:
        random_letter = random.choice(content)
        if random_letter.isalpha():
            hand += random_letter.lower()
            a += 1
    hand = hand.replace(random.choice(hand), '*',1)
    hand = hand.lower()
    return hand

#### make a dict from letters
def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


##### Count score of word #####
def word_scores(word,n):
    scrabble_letter_points = {1: 'aeioulnstr',
                              2: 'dg',
                              3: 'bcmp',
                              4: 'fhvwy',
                              5: 'k',
                              8: 'jx',
                              10: 'qz'}
    sum_point_of_letters = 0
    for key,value in scrabble_letter_points.items():
        for letter in word.lower():
            if letter in value:
                sum_point_of_letters += key
    full_sum_of_point = (7 * len(word) - 3*(n - len(word))) * sum_point_of_letters
    return int(abs(full_sum_of_point))


#### Display a hand
def display_hand(hand):
    s = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            s += letter + " "
    return s



#### Show remainder letters after player choose word ####
def update_hand(refresh_dict,word):
    dictionary = refresh_dict.copy()
    for key in word.lower():
        if key in refresh_dict and key in dictionary:
            refresh_dict[key] = refresh_dict[key] - 1
            if dictionary[key] > 1:
                dictionary[key] = dictionary[key] - 1
            else:
                del dictionary[key]
    hand = ''
    for a in dictionary.keys():
        if dictionary[a] > 1:
            hand += (dictionary[a]-1) * a
        else:
            hand += a
    return hand


###### Word valid or not
def is_valid_word(word,hand):
    with open('words.txt', 'r') as file:
        content = file.read()
    content = content.lower()
    if word not in content.split():
        return False
    for a in word:
        if a not in hand:
            return False
    return True


####### DO not understand why
def deal_hand(n):
    hand = {}
    VOWELS = 'aeiou'
    num_vowels = int(math.ceil(n / 3))
    with open('WordsForGames.txt', 'r') as file:
        CONSONANTS = file.read()
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        if x.isalpha():
            hand[x] = hand.get(x, 0) + 1

    return hand



if __name__ == "__main__":
    Scrable_game()



