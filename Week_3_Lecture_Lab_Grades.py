gradebook = {}

while True:
    student = input("Enter a student name (q to quit): ")

    if student == "q":
        print("Goodbye!")
        break

    if student not in gradebook:
        grade = input(f"Enter {student}'s grade: ")
        try:
            gradebook[student] = int(grade)
        except ValueError:
            print("Invalid grade. Enter a whole number 0-100.\n")

    else:
        grade = gradebook[student]
        print(f"{student}'s grade is {grade}%.")

        if 0 <= grade < 60:
            print(f"{student} has an F in this class.\n")
        elif 60 <= grade < 70:
            print(f"{student} has a D in this class.\n")
        elif 70 <= grade < 80:
            print(f"{student} has a C in this class.\n")
        elif 80 <= grade < 90:
            print(f"{student} has a B in this class.\n")
        elif 90 <= grade:
            print(f"{student} has an A in this class.\n")
        else:
            print(f"There is a mistake with {student}'s grade.")

        change = input("Do you wish to change this grade (y/n)? ")

        if change == "y":
            grade = input(f"Enter {student}'s grade: ")
            try:
                gradebook[student] = int(grade)
            except ValueError:
                print("Invalid grade. Enter a whole number 0-100.\n")

    print("Returning...\n")