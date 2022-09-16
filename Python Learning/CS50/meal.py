def main():
    String=str(input("Enter the time "))
    converted=convert(String)

    if(converted>=7.00 and converted<=8.00):
        print("breakfast time")
    elif(converted>=12.00 and converted<=13.00):
        print("lunch time")
    elif(converted>=18.00 and converted<=19.00):
        print("dinner time")



def convert(time):
    hours,minute=time.split(":")
    conversion=float((int(hours)*60+int(minute))/60)
    return conversion

if __name__ == "__main__":
    main()