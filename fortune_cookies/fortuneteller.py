from random import choice

fortune = input('input number for the day: ')
fortunes = ['You got 10 for your life! Great Job!', 'Bad day would happen if you did not pray',
            'You will get a billion dollars!', 'Not a bad day', 'not good yet',
            'Flat journey', 'Lucky Vickiy:D']

fortune = choice(fortunes)
print(fortune)