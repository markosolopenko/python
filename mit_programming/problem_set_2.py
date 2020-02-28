def hangman(word_to_guess):
    amount_of_guesses = 0
    real_word = ''
    while amount_of_guesses < len(word_to_guess):
        player_try = str(input("Please put letter: "))
        if player_try in word_to_guess:
            real_word += player_try
            amount_of_guesses += 1
            print("OOh nice your letter is: " + str(word_to_guess.index(player_try)) + " in the word")
        else:
            amount_of_guesses+=1
            print("Oops, here is no one letter like this")
    if len(real_word) == len(word_to_guess):
        print("My congratulation you win!!!!!")
    else:
        print("Sorry but not today!!")

if __name__ == "__main__":
    hangman('computer')