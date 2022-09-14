String=str(input("DO you want the answer to Great Question of Life?"))
newString=String.strip()
if (newString== "42"or newString.lower() == "forty-two" or newString.lower()=="forty two"):
    print("Yes")
else:
    print("No")
