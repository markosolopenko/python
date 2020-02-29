def hangman(word_to_guess):
    amount_of_guesses = 0
    real_word = ''
    final_exeplare = ''
    true_answers = 0
    hidden_word = len(word_to_guess)*"_"
    hidden = []
    for sel in hidden_word:
        hidden.append(sel)

    while true_answers < len(word_to_guess):
        if amount_of_guesses >= 5:
            break
        player_try = str(input("Please put letter: "))
        if player_try in word_to_guess and player_try not in hidden:
            if word_to_guess.count(player_try) > 1:
                true_answers+=1
            true_answers+=1
            for char in range(len(hidden)):
                if word_to_guess[char] == player_try:
                    hidden[char] = player_try
                else:
                    continue
            for a in hidden:
                real_word += a + "|"
            print("Good your letter exist: " + '[' + str(real_word) + ']')
            final_exeplare = real_word
            real_word = ''
        else:
            amount_of_guesses+=1
            print("Oops, here is no one letter like this")
    if final_exeplare == word_to_guess:
        print("My congratulation you win!!!!!")
    else:
        print("Sorry but not today!!")

if __name__ == "__main__":
    hangman('congretulations')