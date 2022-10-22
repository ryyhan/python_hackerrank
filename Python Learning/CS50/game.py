import random

level = 0


def user_input():
    global level
    while True:
        try:
            level = int(input("Enter a level :"))
        except:
            user_input()
        else:
            if level < 1:
                continue
            else:
                num_guess()
                break


def guess(n):
    global level
    rnum = random.randrange(0, level)
    if n < rnum:
        print("Too small!")
        num_guess()
    elif n > rnum:
        print("Too large!")
        num_guess()
    elif n == rnum:
        print("Just right!")


def num_guess():
    try:
        gnum = int(input("Guess : "))
    except:
        num_guess()
    else:
        if gnum < 1:
            num_guess()
        else:
            guess(gnum)


user_input()
