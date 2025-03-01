import random

word_list = ["arrdvark","baboon","camel"]

random_word = random.choice(word_list)

user_letter = input("Guess a letter\n").lower()

response = ""

for letter in random_word:
    if user_letter == letter:
        response+=user_letter
    else:
        response+="_"

print(response)