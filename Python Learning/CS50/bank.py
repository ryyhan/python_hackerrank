String=str(input("Greeting :"))
newString=String.lower().strip()

if (newString.startswith("hello")):
    print("$0")

elif (newString.startswith("h") and newString !="hello"):
    print("$20")
else:
    print("$100")
