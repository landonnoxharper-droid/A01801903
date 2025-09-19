from datetime import datetime

age = 0
birth = 0
valid = False
bday = 0

while not valid:

    age = int(input("Whats your age?\n"))
    current_year = datetime.now().year
    bday = current_year - age
    
    if age >= 18:
        print("You are an adult!")

    else:
        print("You are underage!")

    if age < 19 and age > 13:
        print ("You are a teenager")

    print(f"Your birth year is at {birth}")

    bday = input("Did you already had your birthday?\n")
    if bday.lower() == "yes":
        print ("Good!")
    else:
        print ("Well, happy early birth day!")
    valid = True
