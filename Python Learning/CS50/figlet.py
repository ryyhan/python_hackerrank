import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    randomFont = True

elif len(sys.argv) == 3 and (sys.argv[1] == "-f") or (sys.arg[1] == "-font"):
    randomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

figlet.getFonts()

if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])

    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


output = input("Enter Text: ")


print(figlet.renderText(output))
