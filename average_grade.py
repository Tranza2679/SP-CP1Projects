# Average Grade Calculator, Santiago Pineda


print("Hello! Welcome to average grade calculator!")
print("")
while True:
    try:
        grade_one = float(input("What is the grade of your first class as a number: "))
        grade_two = float(input("What is the grade of your second class as a number: "))
        grade_three = float(input("What is the grade of your third class as a number: "))
        grade_four = float(input("What is the grade of your fourth class as a number: "))
        grade_five = float(input("What is the grade of your fifth class as a number: "))
        grade_six = float(input("What is the grade of your sixth class as a number: "))
        grade_seven = float(input("What is the grade of your seventh class as a number: "))
    except: 
        print("That's not a number!")
    else: 
        break 
average_grade = grade_one + grade_two + grade_three + grade_four + grade_five + grade_six + grade_seven



