def convert(emoji):
    print(emoji.replace(":)","🙂").replace(":(","🙁"))

def main():
    emoji=input()
    convert(emoji)

main()