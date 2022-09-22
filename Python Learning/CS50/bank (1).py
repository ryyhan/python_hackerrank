def main():
    String=str(input("Greeting :"))
    newString=String.lower().strip()
    converted=value(newString)
    print("$"+converted)


def value(greeting):
    greet=greeting.lower().strip()
    if (greet.startswith("hello")):
        return(0)

    elif (greet.startswith("h") and greeting !="hello"):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()