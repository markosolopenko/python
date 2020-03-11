import random
import math
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
print(word_scores('ten',6))