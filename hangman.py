import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

l = []
for letter in chosen_word:
    l += '_'

lives = 6

p = 0

while l.count('_') > 0 and lives > 0:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            l[i] = guess
    if l.count(guess) == 0:
        lives -= 1
        p += 1
        print(stages[p])
        print(f'Remaining lives: {lives}')
    else:
        print(stages[p])
    print(''.join(l),)

if '_' not in l:
    print('You Win!')
else:
    print('You Lose!')
