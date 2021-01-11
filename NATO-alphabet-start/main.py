# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

# TODO 1. Create a dictionary in this format:
data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("What's the word: ")
    try:
        phonetic_words = [nato_dict[letter.upper()] for letter in user_word]
    except KeyError:
        print("Only letters.")
        generate_phonetic()
    else:
        print(phonetic_words)

generate_phonetic()
