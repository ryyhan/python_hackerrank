def user_input():
    while True:
        frac = str(input("Fraction : "))
        try:
            x, y = frac.split("/")
            x = int(x)
            y = int(y)
        except (ValueError):
            pass
        else:
            percentage(x, y)
            break


def percentage(num1, num2):
    if num2 == 0 or num1 > num2:
        user_input()
    rem = round((num1 / num2) * 100)
    if rem <= 1:
        print("E")
    elif rem >= 99:
        print("F")
    else:
        print(rem, "%", sep="")


user_input()
