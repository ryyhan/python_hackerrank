String=str(input("Enter the name of the file : "))
newString=String.lower().strip()

if (newString.endswith(".gif")):
    print("image/gif")

elif (newString.endswith(".jpg")):
    print("image/jpeg")

elif (newString.endswith(".jpeg")):
    print("image/jpeg")

elif (newString.endswith(".png")):
    print("image/png")

elif (newString.endswith(".pdf")):
    print("application/pdf")

elif (newString.endswith(".txt")):
    print("text/plain")

elif (newString.endswith(".zip")):
    print("application/zip")
else:
    print("application/octet-stream")