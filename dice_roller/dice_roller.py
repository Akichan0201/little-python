import random


def rolldice():
    dice = random.randint(1, 6) 
    print('Your rolled ',dice)

if __name__=='__main__':
    rolldice()