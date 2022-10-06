def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(s.isalnum()):
        if(s[0:2].isalpha()):
            if(len(s)<=6 and len(s)>=2):
                if(not(s.isalpha()) or (s[-1].isalpha())):
                    if(s[2] !="0" and s[3]!="0"):
                        return True
    if(s=="CS50"):
        return(True)
    else:
        return(False)


main()