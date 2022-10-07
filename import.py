# TODO
from sys import argv, exit
from cs50 import SQL
import csv

# gives access to the db.
db = SQL("sqlite:///students.db")

# Import CSV file as a command line arg
if len(argv) != 2:
    # incorrect number print error and exit
    print(f"Error there should be 1 argv, you have {argv}")
    exit(1)

    # assume CSV file exists and columns name, house and birth present
    # open the CSV file
with open(argv[1], "r") as inputfile:
    reader = list(csv.reader(inputfile))
    char_list = []
    # add each entry to the list name , house,  birth
    for row in reader:
        char_list.append(row)
    # for each entry in char_list row[0] is the two or three names, split splits these into individual strings. [1] is the house [2] is the birth year.
    for row in char_list:
        name = row[0].split(' ')
        house = row[1]
        birth = row[2]
        # now to if to figure out if len = 2 first and last names only, if len = 3 first midddle last. The following then adds the names to the db
        if len(name) == 2:
            #No middle name
            firstName = name[0]
            middleName = None
            lastName = name[1]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?,?,?,?)", firstName, middleName, lastName, house, birth)
        elif len(name) == 3:
            #Middle name
            firstName = name[0]
            middleName = name[1]
            lastName = name[2]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?,?,?,?)", firstName, middleName, lastName, house, birth)