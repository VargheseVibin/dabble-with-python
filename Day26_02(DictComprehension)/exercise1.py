sentence = "What is the Airspeed Velocity of an unladen swallow?"
words = sentence.split()

letter_count_dict = {word:len(word) for word in words}
print(letter_count_dict)