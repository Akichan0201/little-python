print('========================================================================')
print('                                QUIZ GAME')
print('========================================================================')
print('                                  RULES')
print('1. You will be asked 10 questions')
print('2. You will have 3 attempts to answer all question')
print('3. If you answer the question correctly, you will get 10 point')
print('4. If you answer the question incorrectly, you will lose 10 attempt')
print('5. The game will end if you run out of attempts')
start = input('are you ready to play?, SAY YEY TO START: ')
if start == 'yey'.lower():
    print('Good Luck!')

print('1. What is the capital of Indonesia?')
print('a. Jakarta')
print('b. Bandung')
print('c. Surabaya')
answer1 = input('Your answer: ')
if answer1 == 'a'.lower():
    print('Correct!')
    score = 10
else:
    print('Wrong!')
    score = 0