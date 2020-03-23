import random


def hangman():
    # Random word from file
    lines = open("words.txt").readlines()
    line = lines[0]
    words = [word.lower().strip() for word in line.split()]

    words = []

    with open('words.txt', 'r') as file:
        for line in file:
            words_in_line = line.split()
            words.extend(words_in_line)

    words = [word.lower().strip() for word in words]
    word_to_guess = random.choice(words)
    length_of_word = len(word_to_guess)

    print(f"Welcome to the game Hangman! "
          f"I am thinking of a word that is {length_of_word} letters long")

    amount_of_guesses = 0
    real_word = ''
    final_example = ''
    true_answers = 0
    hidden_word = len(word_to_guess) * "_"
    hidden = []
    for sel in hidden_word:
        hidden.append(sel)

    while true_answers < len(word_to_guess):
        if amount_of_guesses >= 5:
            break
        player_try = str(input("Please put letter: "))
        if player_try in word_to_guess and player_try not in hidden:
            if word_to_guess.count(player_try) > 1:
                true_answers += 1
            true_answers += 1
            for char in range(len(hidden)):
                if word_to_guess[char] == player_try:
                    hidden[char] = player_try
                else:
                    continue
            for a in hidden:
                real_word += a + ' '

            print(f"Good your letter exist: [{str(real_word)}]")
            final_example = real_word.replace(' ', '')

            real_word = ''
        else:
            amount_of_guesses += 1
            print("Oops, here is no one letter like this")


    if final_example == word_to_guess:
        print("My congratulation you win!!!!!")
    else:
        print(word_to_guess)
        print("Sorry but not today!!")


if __name__ == "__main__":
    hangman()
