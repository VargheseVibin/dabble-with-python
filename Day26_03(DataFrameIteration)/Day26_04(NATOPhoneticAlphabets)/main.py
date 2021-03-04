#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

with open("nato_phonetic_alphabet.csv") as file:
    alphabet_lines = file.read().splitlines()

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data_frame)

nato_dict = {row.letter:row.code for(index, row) in nato_data_frame.iterrows()}
# nato_dict = {line.split(",")[0]:line.split(",")[1] for line in alphabet_lines if line.split(",")[0] != 'letter'}
print(nato_dict)

word = input("Enter the word for which you need the NATO code generated:")

phonetic_code = [nato_dict[letter] for letter in word.upper()]
print(phonetic_code)


