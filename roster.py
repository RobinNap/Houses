# TODO
from sys import argv, exit
from cs50 import SQL
import csv

db = SQL("sqlite:///students.db")
# accept the name of a hogwarts house as a command-line argument.
    # If the incorrect number of command-line arguments are provided,  print an error and exit.
if len(argv) != 2:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)

people = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1] )
# query the students table in the students.db database for all of the students in the specified house and print these.
for person in people:
    if person['middle'] == None:
        print(f"{person['first']} {person['last']}, born {person['birth']}")
    else:
        print(f"{person['first']} {person['middle']} {person['last']}, born {person['birth']}")