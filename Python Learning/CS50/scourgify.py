import csv
import sys

info = {}


def user_input():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many commands-line arguments")
        sys.exit(1)
    elif (
        not (sys.argv[1].startswith("before")) or sys.argv[2].endswith(".csv") == False
    ):
        print("Not a CSV file")
        sys.exit(1)
    else:
        existing_name = sys.argv[1]
        new_name = sys.argv[2]
        split(existing_name, new_name)


def split(existing_name, new_name):
    output = []
    try:
        with open(existing_name) as file:
            mydict = csv.DictReader(file)
            for row in mydict:
                first, last = row["name"].split(",")
                house = row["house"]
                output.append({"first": first, "last": last.lstrip(), "house": house})

        with open(new_name, "w") as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in output:
                writer.writerow(
                    {"first": row["last"], "last": row["first"], "house": row["house"]}
                )
    except Exception as e:
        print(e)


user_input()
