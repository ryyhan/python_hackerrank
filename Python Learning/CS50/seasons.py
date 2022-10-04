from datetime import date
import sys
import re
import inflect


flect=inflect.engine()


def main():
    bdate=input("Date of Birth : ")

    try:
        year, month, day=validate(bdate)

    except:
        sys.exit("invalid")

    dob=date(int(year), int(month), int(day))
    today=date.today()

    difference = today - dob
    total_minutes=difference.days * 24 * 60
    output= flect.number_to_words(total_minutes, andword="")
    print(output.capitalize()+ " minutes")


def validate(bdate):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",bdate):
        year, month, day=bdate.split("-")
        return year, month, day






if __name__ == "__main__":
    main()