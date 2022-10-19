menu = []


def user_input():
    while True:
        try:
            item = str(input())
        except:
            print()
            output()
            break
        else:
            store_data(item)


def output():
    global menu
    myset = set(menu)
    listt = list(myset)
    listt.sort()
    for x in listt:
        print(numberOfTimes(x), x)


def store_data(val):
    global menu
    val = val.upper()
    menu.append(val)


def numberOfTimes(val):
    global menu
    menu.sort()
    # myset=set(menu)
    # listt=list(myset)
    return menu.count(val)


user_input()
