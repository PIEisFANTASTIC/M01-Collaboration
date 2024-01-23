'''
Alexander Smith
deans_list_test.py
This program will take inputs for a students last and first names, and also request their GPA.
Then, it will check their GPA to check their placement in honor roll, and/or dean's list.
'''
# We need to check these 'illegal characters' because they are not valid in names or floats.
illegal_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", "_", "=", "+", "<", ">"
                      "{", "}", "[", "]", "\\", "|", "`", "~", "?", "/", "-"]

def check_for_illegal_characters(string_to_check):
    for char in string_to_check:
        # We found an illegal character, return True
        if char in illegal_characters:
            return True
    # We've gotten through the string with no bad characters, return false.
    return False

# This loop will only break if the last_name input is ZZZ.
while True:
    # We will keep trying until we get a valid last name.
    last_name = ""
    while not last_name:
        last_name = input("What is the student's last name? (Type ZZZ to end the program.) ")

        # Let's strip hyphons and periods from the input string for the check, otherwise will fail the sanity check.
        stripped_last_name = last_name.replace('-', '')
        stripped_last_name = last_name.replace('.', '')

        # Last names are only alphabetical, no numbers or illegal chars.
        if not stripped_last_name.isalpha() or check_for_illegal_characters(stripped_last_name):
            print("Invalid last name input, try again.")
            # Reset the last_name value so the loop will run again for name input.
            last_name = ""
            continue

    if last_name == "ZZZ":
        print("Thank you for using the Dean's List and Honor Role Checker, have a nice day!")
        break

    # We will keep trying until we get a valid first name.
    first_name = ""
    while not first_name:
        first_name = input("What is the student's first name? ")

        # Let's strip hyphons and periods from the input string for the check, otherwise will fail the sanity check.
        stripped_first_name = first_name.replace('-', '')
        stripped_first_name = first_name.replace('.', '')

        # First names are only alphabetical, no numbers
        if not stripped_first_name.isalpha() or check_for_illegal_characters(stripped_first_name):
            print("Invalid first name input, try again.")
            # Reset the first_name value so the loop will run again for name input.
            first_name = ""
            continue

    # We will keep trying until we get a valid GPA.
    grade_point_average = None
    while not grade_point_average:
        grade_point_average = input("What is the student's GPA? ")

        # We can only convert the input to a float if the input is entirely non-alpha.
        for char in grade_point_average:
            # If ANY character is alpha, or an illegal char get a new input.
            if char.isalpha() or char in illegal_characters:
                print("Invalid GPA input, try again.")
                # Reset the grade_point_average value so the loop will run again for GPA input.
                grade_point_average = None
                continue

        # Now we know the GPA is all numeric, make it a float
        grade_point_average = float(grade_point_average)

        # Let's make sure our GPA is logical first.
        if grade_point_average < 0 or grade_point_average > 4:
            print("GPA out of range (0-4), please try again.")
            # Reset the grade_point_average value so the loop will run again for GPA input.
            grade_point_average = None
            continue

    # Okay, with all of the inputs and sanity checking out of the way, we can now formulate our outputs!
    # First, let's have our strings ready ahead of time.
    deans_list = "Awesome! %s %s has a GPA of %.3f and is on the Dean's List!"
    honor_role = "Good job! %s %s has a GPA of %.3f and has made the Honor Roll!"
    no_reward = "%s %s has a GPA of %.3f, they did not make the Dean's List or Honor Roll."
    if grade_point_average > 3.5:
        print(deans_list % (first_name, last_name, grade_point_average))
    elif grade_point_average > 3.25:
        print(honor_role % (first_name, last_name, grade_point_average))
    else:
        print(no_reward % (first_name, last_name, grade_point_average))