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
    # We've gotten through the string with no bad characters, return False.
    return False

def name_input(name_string):
    # We will keep trying until we get a valid name.
    name = ""
    while not name:
        if name_string == "last":
            name = input("What is the student's last name? (Type ZZZ to end the program.) ")
        else:
            name = input("What is the student's first name? ")

        # Let's strip hyphons and periods from the input string for the check, otherwise will fail the sanity check.
        stripped_name = name.replace('-', '')
        stripped_name = name.replace('.', '')

        # Names are only alphabetical, no numbers or illegal chars.
        if not stripped_name.isalpha() or check_for_illegal_characters(stripped_name):
            print("Invalid %s name input, try again. " % name_string)
            # Reset the last_name value so the loop will run again for name input.
            name = ""
            continue
    return name

def gpa_input():
    gpa = None
    while not gpa:
        gpa = input("What is the student's GPA? ")

        # We can only convert the input to a float if the input is entirely non-alpha and no illegal characters.
        if gpa.isalpha() or check_for_illegal_characters(gpa) or (gpa.count(".") > 1):
            print("Invalid GPA input, try again.")
            # Reset the gpa value so the loop will run again for GPA input.
            gpa = None
            continue

        # Now we know the GPA is all numeric, make it a float
        gpa = float(gpa)

        # Let's make sure our GPA is logical first.
        if gpa < 0 or gpa > 4:
            print("GPA out of range (0-4), please try again.")
            # Reset the gpa value so the loop will run again for GPA input.
            gpa = None
            continue
    return gpa

# This loop will only break if the last_name input is ZZZ.
while True:
    last_name = name_input("last")

    if last_name == "ZZZ":
        print("Thank you for using the Dean's List and Honor Role Checker, have a nice day!")
        break

    first_name = name_input("first")

    grade_point_average = gpa_input()

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
