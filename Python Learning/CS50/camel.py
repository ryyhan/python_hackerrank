camel=str(input("Enter your input here :"))

for c in camel:
    if(c.isupper()):
        print(f"_{c.lower()}", end="")
    else:
        print(c,end="")