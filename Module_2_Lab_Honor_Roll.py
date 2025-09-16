# Henry Barcalow's Totally Awesome Honor Roll Checker that Totally
# Wasn't Copied From My Lecture Lab Work

# This app accepts a student name and a GP, then checks if the GPA is good
# enough to make the Dean's List or the Honor Roll.
# The gradebook has temporary memory; you can recall any grades from this
# session, but there is no permanent storage.

# (The code was in fact copied from my lecture lab code, mostly so I
# wouldn't have to retype all the if statements and try statements. It is
# my code, after all.)

gradebook = {}

while True:
    last_name = input("Enter a last name (type 'zzz' to quit): ")

    if last_name == "zzz":
        print("Goodbye.")
        break

    first_name = input("Enter a first name (type 'zzz' to quit): ")

    if first_name == "zzz":
        print("Goodbye.")
        break

    student = f"{last_name}, {first_name}"

    if student not in gradebook:
        gpa = input(f"Enter {first_name} {last_name}'s GPA: ")
        try:
            gradebook[student] = float(gpa)
        except ValueError:
            print("Invalid GPA. Enter a number.\n")
            continue

    gpa = gradebook[student]

    print(f"\n{first_name} {last_name}'s GPA is {gpa}.")

    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll!")
    elif gpa >= 0:
        print(f"{first_name} {last_name} did not make the Dean's List or the "
              f"Honor Roll.")
    else:
        print(f"There is a mistake with {first_name} {last_name}'s GPA.")

    change = input("\nDo you wish to change this GPA (y/n)? ")

    if change == "y":
        gpa = input(f"Enter {first_name} {last_name}'s GPA: ")
        try:
            gradebook[student] = float(gpa)
        except ValueError:
            print("Invalid GPA. Enter a number.\n")

    print("Returning...\n")