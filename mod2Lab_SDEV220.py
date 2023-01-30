# Wayne Bell at College Ivy Tech Community College
# mod2Lab_SDEV220 - 2023-01-30
# This program asks for a users last and first name. It then asks for the users GPA as a float. IF the last name entered is "ZZZ" the program exits. 
# If the users GPA is greater than or equal to 3.5, the student is on the Dean's List.
# If the users GPA is greater than or equal to 3.25, the student is on the Honor Roll.

last_name = input("Enter your last name: ")
if last_name == "ZZZ":
    print("Goodbye!")
    quit()  
# This if statement is used to exit the program if the last name entered is "ZZZ"
first_name = input("Enter your first name: ")
gpa = float(input("Enter your GPA: ")) # THis line asks for the users input and converts it to a float
if gpa >= 3.5:
    print("Congratulations, ", first_name, last_name,"!", "You are on the Dean's List") 
    # This line prints the users first and last name and the message that they are on the Dean's List
elif gpa >= 3.25:
    print("Congratulations,",first_name, last_name,"!", "You are on the Honor Roll")
    # This line prints the users first and last name and the message that they are on the Honor Roll
else:
    print(first_name, last_name, ", you are not on the Dean's List or the Honor Roll")
    # This line prints the users first and last name and the message that they are not on the Dean's List or the Honor Roll
