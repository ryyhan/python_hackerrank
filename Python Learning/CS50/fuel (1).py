def main():
    fraction=input()
    percentage=convert(fraction)
    ans=gauge(percentage)
    print(ans)

def convert(fraction):

    x,y=fraction.split("/")
    if((not(x.isnumeric()) or not(y.isnumeric())) or x>y):
        raise ValueError("ValueError")
    if(y == 0):
        raise ZeroDivisonError("ZeroDivisionError")

    rem=round((int(x)/int(y))*100)
    return(rem)



def gauge(percentage):
    if(percentage<=1):
        return("E")
    elif(percentage>=99):
        return("F")
    else:
        return(str(percentage)+"%")

if __name__ == "__main__":
    main()