import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
for i in range(n):
    w = input()
    words.append(w)
inputted_word = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

temp_max_score = 0
definitely_max_score = 0
highest_score_word = ''

points_for_letters = {
    1: "eaionrtlsu",
    2: 'dg',
    3: 'bcmp',
    4: 'fhvwy',
    5: 'k',
    8: 'jx',
    10: 'qz'
}


def is_possible_to_make_word(w, inputted_word):
    for letter in w:
        if letter not in inputted_word:
            return False
        inputted_word = inputted_word.replace(letter, '', 1)
    return True

def get_word_score(w):
    score = 0
    for letter in w:
        for key, value in points_for_letters.items():
            if letter in value:
                score += key
                break
    return score

for w in words:
    if is_possible_to_make_word(w, inputted_word):
        word_score = get_word_score(w)
        if word_score > definitely_max_score:
            highest_score_word = w
            definitely_max_score = word_score

print(highest_score_word)
