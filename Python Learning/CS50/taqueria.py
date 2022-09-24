total = 0


def user_input():
    while True:
        try:
            item = str(input("Item : "))
        except:
            break
        else:
            totalCalc(item)


def totalCalc(item):
    global total
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    s = item.title()
    if s in menu:
        total += menu[s]
        print("Total : ${:0.2f}".format(total))
    # print("Total : $",round(float(total),2),sep="")


user_input()
