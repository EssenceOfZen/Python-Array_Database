# Array Database
#   Made for learning and practicing and giving others something to mess around on.
# Basic List(array) practice code.

import EoZ
import os
import time

EoZ.EoZ_Logo()

# Global variables
DATABASE = []
DATABASENAME = ""
DATE = time.strftime("%Y %b %d")
VERSION = "1.0.5"

# Initialize System ============================================
if not os.path.exists("logs"): # if the logs folder doesn't exist make it
    os.mkdir("Logs")



# Functions ====================================================
def menu():
    print("Welcome to the database!")
    print("Commands: ")
    print("[load] : Loads a database via file.")
    print("[save] : Saves a database to a storage file.")
    print("[display] : Displays current database.")
    print("[add] : Adds an entry.")
    print("[remove] : Removes an entry.")
    print("[edit] : Edits an entry.")
    print("[search] : Searches for an entry.")
    print("[version] : Gives you the version of the program.")
    print("[quit] : Ends the program.")
    print()


def load():  # load from a .pydb file
    global DATABASENAME
    global DATABASE
    file_name = input("What is the filename of the database?: ")
    DATABASENAME = file_name
    pass


def save():
    global DATABASENAME
    if DATABASENAME == "":
        DATABASENAME = input("Please enter database name:")

    # Proceed to exporting the data files

    pass


def display(database):
    print("Displaying current Database:")
    temp = 0
    for line in database:
        print("Index:" + "{" + str(temp) + "}", line)
        temp += 1


def remove():
    global DATABASE
    display(DATABASE)
    entry = int(input("Please choose your entry: "))
    DATABASE.remove(entry)


def edit():
    global DATABASE
    display(DATABASE)
    entry = int(input("Please choose your entry: "))
    print(DATABASE[entry])
    print("What do you want to edit? | [name] [id] [label] [age] [site]")
    pass


# Searching Functions ===================================================================
def search(database_array):
    print("You can search via: [name] [id] [label] [age] [site]")
    switch = 1
    while switch == 1:
        user_input = input("Search which field?: ")
        if user_input == "name":
            searchName(database_array)
            switch = 0
        if user_input == "id":
            pass
        if user_input == "label":
            pass
        if user_input == "age":
            pass
        if user_input == "site":
            pass


def searchName(database_array):
    # I would like to change this function to search for strings of 3 - 5 character matching in sequential order
    user_input = input("What name are you searching for?: ").lower().strip()
    number = 0
    for entry in database_array:  # what this does is check each name in each inner array
        if entry[0] == user_input:  # 0=name index, so for every index[0] in the indexes inside the main index
            user_name = str(entry)  # Make an instance of the object as a string
            print("Result #" + str(number) + ": " + user_name)
            number += 1


def searchID(database_array):
    user_input = input("What ID are you searching for?: ").lower().strip()
    number = 0
    for entry in database_array:
        if entry[1] == user_input:
            user_id = str(entry)
            print("Result #" + str(number) + ": " + user_id)
            number += 1


def searchLabel(database_array):
    user_input = input("What label are you searching for?: ").lower().strip()
    number = 0
    for entry in database_array:
        if entry[2] == user_input:
            user_label = str(entry)
            print("Result #" + str(number) + ": " + user_label)
            number += 1


# ==========================================================================================

def addEntry(database_array):  # Create an empty entry
    new_entry = [0, 0, 0, 0, 0]
    database_array.append(new_entry)


def add(database_array):  # Create a new entry
    # global DATABASE

    name = str(input("Please input name: "))
    id = str(input("Please input id: "))
    label = str(input("Please input label: "))
    age = int(input("Please input age: "))
    site = str(input("Please input site: "))

    array = [name, id, label, age, site]
    # DATABASE.append(array)
    database_array.append(array)

def getDate(): # Simply prints the date that was set at the beginning of the code
    global DATE
    print(DATE)

def getVersion():
    global VERSION
    print(VERSION)


def main():
    # Creating variables
    global DATABASE
    DATABASE = [[0 for x in range(5)] for x in range(5)]  # creates a 2 dimensional array

    # print("gonna display the database!")
    display(DATABASE)
    # print("Displayed it!")

    # Imagine we wanted [0] = name [1] = ID [2] = Label [3] = Age and [4] = site

    print()

    # print("Gonna print menu!")
    menu()
    # print("printed it!")

    # User commands, each input should be a function.
    switch = 1
    while switch == 1:
        user_input = input("Please enter command: ").lower().strip()
        if user_input == "load":
            load()
        elif user_input == "save":
            save()
        elif user_input == "display":
            display(DATABASE)
        elif user_input == "add":
            add(DATABASE)
        elif user_input == "remove":
            remove()
        elif user_input == "search":
            search(DATABASE)
        elif user_input == "edit":
            edit()
        elif user_input == "date":
            getDate()
        elif user_input == "version":
            getVersion()
        elif user_input == "quit":
            switch = 0

        # Extra commands
        elif user_input == "zenookami":
            print("Zen is love, Zen is life!")

        else:
            print("Invalid input, please try again.")

        print()


main()
