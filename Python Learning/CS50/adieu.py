import inflect

p = inflect.engine()
list_Names = []


def user_input():
    while True:
        try:
            names = str(input("Enter a name: "))
        except:
            bidding_Adieu()
            break
        else:
            list_Names.append(names)


def bidding_Adieu():
    global list_Names
    new_list = p.join(list_Names)
    print("Adieu, adieu, to", new_list)


user_input()
