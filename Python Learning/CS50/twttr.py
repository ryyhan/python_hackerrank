def main():
    String=input("Input : ")
    op=shorten(String)
    print("Output :",op)


def shorten(word):
    op=""
    for c in word:
        if(c=='a' or c=='A'
        or c=='e' or c=='E'
        or c=='i' or c=='I'
        or c=='o' or c=='O'
        or c=='u' or c=='U'):
            continue
        else:
            op=op+c
    return(op)


if __name__ == "__main__":
    main()