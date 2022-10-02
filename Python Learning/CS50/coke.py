amount_due = 50

while amount_due > 0:
    print("Amount Due :", amount_due)
    coins = int(input("Insert Amount : "))
    if coins in [25, 10, 5]:
        amount_due -= coins

change_owed = abs(amount_due)
print("Change Owed :", change_owed)
