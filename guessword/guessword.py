import random


Words = ['rizz', 'hello', 'indonesia', 'sigma', 'anomali']
word = random.choice(Words)

guess_words = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('current guess: ' + ' '.join(guess_words))
    guess = input('Guess a Letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_words[i] = guess
        print('Great Guess!')
    else:
        attempts -= 1
        print('Wrong guess! your attempts left: ', str(attempts))
    if '_' not in guess_words:
        print('\nCongratulations!! You guess the word: ', word)
        break
    else:
        ('\nYou have run out of attempts! The word is: ', word)